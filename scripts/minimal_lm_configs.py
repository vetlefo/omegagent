"""Minimal LM configurations for testing without full dependencies."""

class LitellmModel:
    def __init__(self, model: str, max_tokens: int, **kwargs):
        self.model = model
        self.max_tokens = max_tokens
        self.kwargs = kwargs

class MinimalLMConfigs:
    def __init__(self):
        self.question_answering_lm = None
        self.discourse_manage_lm = None
        self.utterance_polishing_lm = None
        self.warmstart_outline_gen_lm = None
        self.question_asking_lm = None
        self.knowledge_base_lm = None

    def init(self, lm_type: str = "openai", temperature: float = 1.0, top_p: float = 0.9) -> None:
        kwargs = {
            "temperature": temperature,
            "top_p": top_p,
            "api_base": None,
        }
        model_name = "gpt-4o-2024-05-13"
        self.question_answering_lm = LitellmModel(model=model_name, max_tokens=1000, **kwargs)
        self.discourse_manage_lm = LitellmModel(model=model_name, max_tokens=500, **kwargs)
        self.utterance_polishing_lm = LitellmModel(model=model_name, max_tokens=2000, **kwargs)
        self.warmstart_outline_gen_lm = LitellmModel(model=model_name, max_tokens=500, **kwargs)
        self.question_asking_lm = LitellmModel(model=model_name, max_tokens=300, **kwargs)
        self.knowledge_base_lm = LitellmModel(model=model_name, max_tokens=1000, **kwargs)