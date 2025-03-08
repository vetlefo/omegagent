from pydantic import BaseModel, Field


class RunnerArgument(BaseModel):
    """Arguments for controlling the Co-STORM pipeline."""

    topic: str = Field(..., description="Topic of discourse")
    retrieve_top_k: int = Field(default=10, description="Top k results for retriever queries")
    max_search_queries: int = Field(default=2, description="Max search queries per question")
    total_conv_turn: int = Field(default=20, description="Max conversation turns")
    max_search_thread: int = Field(default=5, description="Max parallel threads for retriever")
    max_search_queries_per_turn: int = Field(default=3, description="Max search queries per turn")
    warmstart_max_num_experts: int = Field(default=3, description="Max experts in warm start QA")
    warmstart_max_turn_per_experts: int = Field(default=2, description="Max turns per expert in warm start")
    warmstart_max_thread: int = Field(default=3, description="Max threads for warm start QA")
    max_thread_num: int = Field(default=10, description="Max total threads")
    max_num_round_table_experts: int = Field(default=2, description="Max active experts in round table")
    moderator_override_N_consecutive_answering_turn: int = Field(default=3, description="Turns before moderator override")
    node_expansion_trigger_count: int = Field(default=10, description="Trigger node expansion for large snippet counts")
    disable_moderator: bool = Field(default=False, description="Disable moderator if True")
    disable_multi_experts: bool = Field(default=False, description="Disable multi-experts if True")
    rag_only_baseline_mode: bool = Field(default=False, description="Switch to RAG-only mode if True")

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return self.model_dump()