from typing import List, Union, Dict
from .lm_configs import CollaborativeStormLMConfigs
from .runner_args import RunnerArgument
from .turn_policy import TurnPolicySpec
from .modules.co_storm_agents import SimulatedUser, PureRAGAgent, Moderator, CoStormExpert
from .modules.expert_generation import GenerateExpertModule
from ..interface import Agent, ConversationTurn

from ..encoder import Encoder
from .modules.callback import BaseCallbackHandler
from ..logging_wrapper import LoggingWrapper
from ..rm import BingSearch


class DiscourseManager:
    """Manages discourse flow and agent interactions in Co-STORM."""

    def __init__(
        self,
        lm_config: CollaborativeStormLMConfigs,
        runner_argument: RunnerArgument,
        logging_wrapper: LoggingWrapper,
        rm: 'BingSearch',
        encoder: Encoder,
        callback_handler: 'BaseCallbackHandler',
    ):
        self.lm_config = lm_config
        self.runner_argument = runner_argument
        self.logging_wrapper = logging_wrapper
        self.callback_handler = callback_handler
        self.rm = rm
        self.encoder = encoder
        self.experts: List[CoStormExpert] = []
        self.next_turn_moderator_override = False
        self._initialize_agents()
        self.generate_expert_module = GenerateExpertModule(engine=self.lm_config.discourse_manage_lm)

    def _initialize_agents(self) -> None:
        """Initialize core agents."""
        common_args = {
            "topic": self.runner_argument.topic,
            "lm_config": self.lm_config,
            "runner_argument": self.runner_argument,
            "logging_wrapper": self.logging_wrapper,
            "callback_handler": self.callback_handler,
        }
        self.simulated_user = SimulatedUser(role_name="Guest", role_description="", intent=None, **common_args)
        self.pure_rag_agent = PureRAGAgent(role_name="PureRAG", role_description="", rm=self.rm, **common_args)
        self.moderator = Moderator(role_name="Moderator", role_description="", encoder=self.encoder, **common_args)
        self.general_knowledge_provider = CoStormExpert(
            role_name="General Knowledge Provider",
            role_description="Focus on broadly covering basic facts.",
            rm=self.rm,
            **common_args,
        )

    def serialize_experts(self) -> List[Dict]:
        """Serialize experts to dictionaries."""
        return [{"topic": e.topic, "role_name": e.role_name, "role_description": e.role_description} for e in self.experts]

    def deserialize_experts(self, data: List[Dict]) -> None:
        """Deserialize experts from dictionaries."""
        common_args = {
            "lm_config": self.lm_config,
            "runner_argument": self.runner_argument,
            "logging_wrapper": self.logging_wrapper,
            "rm": self.rm,
            "callback_handler": self.callback_handler,
        }
        self.experts = [
            CoStormExpert(topic=d["topic"], role_name=d["role_name"], role_description=d["role_description"], **common_args)
            for d in data
        ]

    def _should_generate_question(self, conversation_history: List[ConversationTurn]) -> bool:
        """Check if a question should be generated based on turn history."""
        consecutive_non_questioning = 0
        for turn in reversed(conversation_history):
            if turn.utterance_type not in ["Original Question", "Information Request"]:
                consecutive_non_questioning += 1
            else:
                break
        return consecutive_non_questioning >= self.runner_argument.moderator_override_N_consecutive_answering_turn

    def _parse_expert_names_to_agent(self, expert_descriptions: Union[str, List[str]]) -> List[CoStormExpert]:
        """Parse expert descriptions into agents."""
        if isinstance(expert_descriptions, str):
            expert_descriptions = [expert_descriptions]
        common_args = {
            "topic": self.runner_argument.topic,
            "lm_config": self.lm_config,
            "runner_argument": self.runner_argument,
            "logging_wrapper": self.logging_wrapper,
            "rm": self.rm,
            "callback_handler": self.callback_handler,
        }
        agents = []
        for desc in expert_descriptions:
            name, description = desc.split(":", 1)
            agents.append(CoStormExpert(role_name=name.strip(), role_description=description.strip(), **common_args))
        return agents

    def _update_expert_list_from_utterance(self, focus: str, background_info: str) -> None:
        """Update expert list based on conversation context."""
        expert_names = self.generate_expert_module(
            topic=self.runner_argument.topic,
            background_info=background_info,
            focus=focus,
            num_experts=self.runner_argument.max_num_round_table_experts,
        ).experts
        self.experts = self._parse_expert_names_to_agent(expert_names)

    def _is_last_turn_questioning(self, conversation_history: List[ConversationTurn]) -> bool:
        """Check if the last turn was a question."""
        return bool(conversation_history and conversation_history[-1].utterance_type in ["Original Question", "Information Request"])

    def get_next_turn_policy(
        self,
        conversation_history: List[ConversationTurn],
        dry_run: bool = False,
        simulate_user: bool = False,
        simulate_user_intent: str = None,
    ) -> TurnPolicySpec:
        """Determine policy for the next conversation turn."""
        policy = TurnPolicySpec()
        if simulate_user:
            self.simulated_user.intent = simulate_user_intent
            policy.agent = self.simulated_user
        elif self.runner_argument.rag_only_baseline_mode:
            assert conversation_history[-1].role == "Guest"
            policy.agent = self.pure_rag_agent
        elif self.next_turn_moderator_override:
            policy.agent = self.moderator
            if not dry_run:
                self.next_turn_moderator_override = False
        elif not self.runner_argument.disable_moderator and self._should_generate_question(conversation_history):
            policy.agent = self.moderator
            policy.should_reorganize_knowledge_base = True
        else:
            policy.agent = self.general_knowledge_provider
            if not self._is_last_turn_questioning(conversation_history) and not self.runner_argument.disable_multi_experts:
                policy.agent = self.experts[0] if dry_run else self.experts.pop(0)
                if not dry_run:
                    self.experts.append(policy.agent)
            policy.should_update_experts_list = self._is_last_turn_questioning(conversation_history) and not self.runner_argument.disable_multi_experts
            policy.should_polish_utterance = True
        return policy