from pydantic import BaseModel, Field
from typing import Union
from ..interface import Agent, SimulatedUser, PureRAGAgent, Moderator, CoStormExpert


class TurnPolicySpec(BaseModel):
    """Policy specifications for conversation turn behavior."""

    should_reorganize_knowledge_base: bool = False
    should_update_experts_list: bool = False
    should_polish_utterance: bool = False
    agent: Union[SimulatedUser, PureRAGAgent, Moderator, CoStormExpert] = None