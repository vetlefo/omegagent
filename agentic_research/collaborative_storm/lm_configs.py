import os
from typing import Literal, Optional, Dict
from ..interface import LMConfigs
from ..lm import LitellmModel


class CollaborativeStormLMConfigs(LMConfigs):
    """Configurations for LLMs used in Co-STORM, balancing quality and efficiency."""

    def __init__(self):
        self.question_answering_lm = None
        self.discourse_manage_lm = None
        self.utterance_polishing_lm = None
        self.warmstart_outline_gen_lm = None
        self.question_asking_lm = None
        self.knowledge_base_lm = None

    def init(
        self,
        lm_type: Literal["openai", "azure", "together"],
        temperature: float = 1.0,
        top_p: float = 0.9,
    ) -> None:
        """Initialize LLM configurations based on provider type."""
        providers = {
            "openai": self._init_openai,
            "azure": self._init_azure,
            "together": self._init_together,
        }
        if lm_type not in providers:
            raise ValueError(
                f"Unsupported LM provider: {lm_type}. Must be 'openai', 'azure', or 'together'."
            )
        providers[lm_type](temperature, top_p)

    def _init_openai(self, temperature: float, top_p: float) -> None:
        kwargs = {
            "api_key": os.getenv("OPENAI_API_KEY"),
            "temperature": temperature,
            "top_p": top_p,
            "api_base": None,
        }
        self.question_answering_lm = LitellmModel(model="gpt-4o-2024-05-13", max_tokens=1000, **kwargs)
        self.discourse_manage_lm = LitellmModel(model="gpt-4o-2024-05-13", max_tokens=500, **kwargs)
        self.utterance_polishing_lm = LitellmModel(model="gpt-4o-2024-05-13", max_tokens=2000, **kwargs)
        self.warmstart_outline_gen_lm = LitellmModel(model="gpt-4-1106-preview", max_tokens=500, **kwargs)
        self.question_asking_lm = LitellmModel(model="gpt-4o-2024-05-13", max_tokens=300, **kwargs)
        self.knowledge_base_lm = LitellmModel(model="gpt-4o-2024-05-13", max_tokens=1000, **kwargs)

    def _init_azure(self, temperature: float, top_p: float) -> None:
        kwargs = {
            "api_key": os.getenv("AZURE_API_KEY"),
            "temperature": temperature,
            "top_p": top_p,
            "api_base": os.getenv("AZURE_API_BASE"),
            "api_version": os.getenv("AZURE_API_VERSION"),
        }
        azure_model = "azure/gpt-4o"
        self.question_answering_lm = LitellmModel(model=azure_model, max_tokens=1000, model_type="chat", **kwargs)
        self.discourse_manage_lm = LitellmModel(model=azure_model, max_tokens=500, model_type="chat", **kwargs)
        self.utterance_polishing_lm = LitellmModel(model=azure_model, max_tokens=2000, model_type="chat", **kwargs)
        self.warmstart_outline_gen_lm = LitellmModel(model=azure_model, max_tokens=300, model_type="chat", **kwargs)
        self.question_asking_lm = LitellmModel(model=azure_model, max_tokens=300, model_type="chat", **kwargs)
        self.knowledge_base_lm = LitellmModel(model=azure_model, max_tokens=1000, model_type="chat", **kwargs)

    def _init_together(self, temperature: float, top_p: float) -> None:
        kwargs = {"api_key": os.getenv("TOGETHER_API_KEY"), "temperature": temperature, "top_p": top_p}
        together_model = "together_ai/meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
        self.question_answering_lm = LitellmModel(model=together_model, max_tokens=1000, model_type="chat", **kwargs)
        self.discourse_manage_lm = LitellmModel(model=together_model, max_tokens=500, model_type="chat", **kwargs)
        self.utterance_polishing_lm = LitellmModel(model=together_model, max_tokens=2000, model_type="chat", **kwargs)
        self.warmstart_outline_gen_lm = LitellmModel(model=together_model, max_tokens=500, model_type="chat", **kwargs)
        self.question_asking_lm = LitellmModel(model=together_model, max_tokens=300, model_type="chat", **kwargs)
        self.knowledge_base_lm = LitellmModel(model=together_model, max_tokens=1000, model_type="chat", **kwargs)

    def set_lm(self, lm_name: str, model: 'LitellmModel') -> None:
        """Set a specific LM by name."""
        if hasattr(self, lm_name):
            setattr(self, lm_name, model)
        else:
            raise AttributeError(f"Unknown LM attribute: {lm_name}")

    def collect_and_reset_lm_usage(self) -> Dict[str, dict]:
        """Collect and reset usage stats for all LMs."""
        lm_usage = {}
        for attr in self.__dict__:
            lm = getattr(self, attr)
            if lm and hasattr(lm, "get_usage_and_reset"):
                usage = lm.get_usage_and_reset()
                if any(v["prompt_tokens"] != 0 or v["completion_tokens"] != 0 for v in usage.values()):
                    lm_usage[attr] = usage
        return lm_usage

    def to_dict(self) -> Dict[str, dict]:
        """Convert config to dictionary."""
        return {attr: getattr(self, attr).kwargs for attr in self.__dict__}