"""Utility classes for testing the DiscourseManager."""

class MockBingSearch:
    """Mock search implementation."""
    def __init__(self, api_key=None):
        self.api_key = api_key

    def search(self, query: str) -> str:
        return f"Mock search result for: {query}"

class MockEncoder:
    """Mock encoder implementation."""
    def encode(self, text: str) -> list:
        return [0.1, 0.2, 0.3]  # Mock embedding

class MockCallbackHandler:
    """Mock callback handler implementation."""
    def on_llm_start(self, *args, **kwargs):
        pass

    def on_llm_end(self, *args, **kwargs):
        pass

    def on_llm_error(self, *args, **kwargs):
        pass

class MockLoggingWrapper:
    """Mock logging wrapper implementation."""
    def log(self, *args, **kwargs):
        pass

    def info(self, *args, **kwargs):
        pass

    def error(self, *args, **kwargs):
        pass

    def warning(self, *args, **kwargs):
        pass