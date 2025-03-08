from pydantic import BaseModel
from ..interface import Agent


class TurnPolicySpec(BaseModel):
    """Policy specifications for conversation turn behavior."""

    should_reorganize_knowledge_base: bool = False
    should_update_experts_list: bool = False
    should_polish_utterance: bool = False
    agent: Agent = None