"""Minimal version of DiscourseManager without graph dependencies."""

from typing import List, Dict
from agentic_research.collaborative_storm.lm_configs import CollaborativeStormLMConfigs
from agentic_research.search import BingSearch
from agentic_research.collaborative_storm.runner_args import RunnerArgument
from agentic_research.encoder import Encoder
from agentic_research.dataclass import ConversationTurn
from agentic_research.logging_wrapper import LoggingWrapper
from agentic_research.callback_handler import BaseCallbackHandler

class TurnPolicySpec:
    """Specification for the next conversation turn."""
    def __init__(self):
        self.agent = None
        self.should_reorganize_knowledge_base = False
        self.should_update_experts_list = False
        self.should_polish_utterance = False

    def __str__(self):
        return f"Using {self.agent.role_name} with polish={self.should_polish_utterance}"

class Agent:
    """Base agent class."""
    def __init__(self, role_name: str, role_description: str, **kwargs):
        self.role_name = role_name
        self.role_description = role_description
        self.topic = kwargs.get('topic')
        self.lm_config = kwargs.get('lm_config')
        self.runner_argument = kwargs.get('runner_argument')
        self.logging_wrapper = kwargs.get('logging_wrapper')
        self.callback_handler = kwargs.get('callback_handler')

class SimulatedUser(Agent):
    """User agent implementation."""
    def __init__(self, intent=None, **kwargs):
        super().__init__(**kwargs)
        self.intent = intent

class Moderator(Agent):
    """Moderator agent implementation."""
    def __init__(self, encoder=None, **kwargs):
        super().__init__(**kwargs)
        self.encoder = encoder

class PureRAGAgent(Agent):
    """RAG agent implementation."""
    def __init__(self, rm=None, **kwargs):
        super().__init__(**kwargs)
        self.rm = rm

class CoStormExpert(Agent):
    """Expert agent implementation."""
    def __init__(self, rm=None, **kwargs):
        super().__init__(**kwargs)
        self.rm = rm

class MinimalDiscourseManager:
    """Minimal version of DiscourseManager without graph dependencies."""

    def __init__(
        self,
        lm_config: CollaborativeStormLMConfigs,
        runner_argument: RunnerArgument,
        logging_wrapper: LoggingWrapper,
        rm: BingSearch,
        encoder: Encoder,
        callback_handler: BaseCallbackHandler,
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

    def _should_generate_question(self, conversation_history: List[ConversationTurn]) -> bool:
        """Check if a question should be generated based on turn history."""
        consecutive_non_questioning = 0
        for turn in reversed(conversation_history):
            if turn.utterance_type not in ["Original Question", "Information Request"]:
                consecutive_non_questioning += 1
            else:
                break
        return consecutive_non_questioning >= self.runner_argument.moderator_override_N_consecutive_answering_turn

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
            policy.should_polish_utterance = True
        return policy