import os
from typing import Optional, List, Dict
from .lm_configs import CollaborativeStormLMConfigs
from .runner_args import RunnerArgument
from .discourse_manager import DiscourseManager
from ..interface import ConversationTurn, KnowledgeBase
from ..encoder import Encoder
from ..logging_wrapper import LoggingWrapper
from ..rm import BingSearch
from agentic_research.collaborative_storm.modules.callback import BaseCallbackHandler


class CoStormRunner:
    """Runs the Co-STORM pipeline for collaborative discourse."""

    def __init__(
        self,
        lm_config: CollaborativeStormLMConfigs,
        runner_argument: RunnerArgument,
        logging_wrapper: LoggingWrapper,
        rm: Optional['BingSearch'] = None,
        callback_handler: Optional['BaseCallbackHandler'] = None,
    ):
        self.runner_argument = runner_argument
        self.lm_config = lm_config
        self.logging_wrapper = logging_wrapper
        self.callback_handler = callback_handler
        self.rm = rm if rm else BingSearch(k=runner_argument.retrieve_top_k)
        self.encoder = Encoder()
        self.conversation_history: List[ConversationTurn] = []
        self.warmstart_conv_archive: List[ConversationTurn] = []
        self.knowledge_base = KnowledgeBase(
            topic=self.runner_argument.topic,
            knowledge_base_lm=self.lm_config.knowledge_base_lm,
            node_expansion_trigger_count=self.runner_argument.node_expansion_trigger_count,
            encoder=self.encoder,
        )
        self.discourse_manager = DiscourseManager(
            lm_config=self.lm_config,
            runner_argument=self.runner_argument,
            logging_wrapper=self.logging_wrapper,
            rm=self.rm,
            encoder=self.encoder,
            callback_handler=self.callback_handler,
        )

    def to_dict(self) -> Dict:
        """Serialize runner state to dictionary."""
        return {
            "runner_argument": self.runner_argument.to_dict(),
            "lm_config": self.lm_config.to_dict(),
            "conversation_history": [turn.to_dict() for turn in self.conversation_history],
            "warmstart_conv_archive": [turn.to_dict() for turn in self.warmstart_conv_archive],
            "experts": self.discourse_manager.serialize_experts(),
            "knowledge_base": self.knowledge_base.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: Dict, callback_handler: Optional['BaseCallbackHandler'] = None) -> 'CoStormRunner':
        """Deserialize runner from dictionary."""
        lm_config = CollaborativeStormLMConfigs()
        lm_config.init(lm_type=os.getenv("OPENAI_API_TYPE", "openai"))
        runner = cls(
            lm_config=lm_config,
            runner_argument=RunnerArgument(**data["runner_argument"]),
            logging_wrapper=LoggingWrapper(lm_config),
            callback_handler=callback_handler,
        )
        runner.encoder = Encoder()
        runner.conversation_history = [ConversationTurn.from_dict(turn) for turn in data["conversation_history"]]
        runner.warmstart_conv_archive = [ConversationTurn.from_dict(turn) for turn in data.get("warmstart_conv_archive", [])]
        runner.discourse_manager.deserialize_experts(data["experts"])
        runner.knowledge_base = KnowledgeBase.from_dict(
            data["knowledge_base"],
            knowledge_base_lm=runner.lm_config.knowledge_base_lm,
            node_expansion_trigger_count=runner.runner_argument.node_expansion_trigger_count,
            encoder=runner.encoder,
        )
        return runner

    def warm_start(self) -> None:
        """Warm start the system with background info search (stub implementation)."""
        with self.logging_wrapper.log_pipeline_stage(pipeline_stage="warm start stage"):
            if not self.runner_argument.rag_only_baseline_mode:
                # Placeholder for warm-start logic integration with AI Codepilot
                self.logging_wrapper.log_info("Warm start initiated (to be implemented)")