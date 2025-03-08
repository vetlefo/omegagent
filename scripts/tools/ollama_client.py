"""Ollama client for local LLM support in Agentic-Reasoning."""

import os
import json
import logging
import requests
from typing import Dict, List, Optional, Union, Any

logger = logging.getLogger(__name__)

class OllamaClient:
    """
    Client for interacting with Ollama locally installed models.
    
    This allows running local LLMs via Ollama's API, providing a cost-free
    alternative to cloud-based models for development and testing.
    """
    
    def __init__(
        self, 
        model: str = "llama3",
        base_url: str = "http://localhost:11434",
        temperature: float = 0.7,
        max_tokens: int = 2000,
        timeout: int = 60,
        system_prompt: Optional[str] = None,
    ):
        """
        Initialize the Ollama client.
        
        Args:
            model: The model name to use (must be available in your Ollama installation)
            base_url: The base URL for the Ollama API
            temperature: Temperature for generation
            max_tokens: Maximum tokens to generate
            timeout: Request timeout in seconds
            system_prompt: Optional system prompt for the model
        """
        self.model = model
        self.base_url = base_url
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.system_prompt = system_prompt
        self.history = []
        self.total_tokens = {"prompt": 0, "completion": 0}
        
        # Validate connection to Ollama
        self._validate_connection()
    
    def _validate_connection(self):
        """Check if we can connect to the Ollama API."""
        try:
            response = requests.get(f"{self.base_url}/api/version", timeout=5)
            if response.status_code == 200:
                logger.info(f"Connected to Ollama API: {response.json()}")
                # Check if the model is available
                self._validate_model()
            else:
                logger.warning(f"Ollama API returned status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to connect to Ollama API: {e}")
            logger.info("Make sure Ollama is installed and running on your system")
            raise ConnectionError("Failed to connect to Ollama API")
    
    def _validate_model(self):
        """Check if the specified model is available in Ollama."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                available_models = [model["name"] for model in response.json().get("models", [])]
                
                if not available_models:
                    logger.warning("No models found in Ollama. You may need to pull a model first.")
                    logger.info(f"Try running: ollama pull {self.model}")
                    return
                
                if self.model not in available_models:
                    logger.warning(f"Model '{self.model}' not found in available models: {available_models}")
                    logger.info(f"Try running: ollama pull {self.model}")
                else:
                    logger.info(f"Model '{self.model}' is available")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to check available models: {e}")
    
    def chat(self, 
             prompt: str, 
             temperature: Optional[float] = None, 
             max_tokens: Optional[int] = None,
             system: Optional[str] = None) -> Dict[str, Any]:
        """
        Send a chat request to the Ollama API.
        
        Args:
            prompt: The user prompt
            temperature: Optional temperature override
            max_tokens: Optional max tokens override
            system: Optional system prompt override
            
        Returns:
            Dict containing the response and metadata
        """
        url = f"{self.base_url}/api/chat"
        
        # Prepare the request payload
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "options": {
                "temperature": temperature if temperature is not None else self.temperature,
                "num_predict": max_tokens if max_tokens is not None else self.max_tokens,
            }
        }
        
        # Add system prompt if provided
        if system or self.system_prompt:
            payload["system"] = system or self.system_prompt
            
        try:
            response = requests.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Update token usage
            self.total_tokens["prompt"] += data.get("prompt_eval_count", 0)
            self.total_tokens["completion"] += data.get("eval_count", 0)
            
            # Store in history
            history_entry = {
                "prompt": prompt,
                "response": data,
                "system": system or self.system_prompt,
            }
            self.history.append(history_entry)
            
            return data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error during Ollama chat request: {e}")
            raise
    
    def generate(self, 
               prompt: str, 
               temperature: Optional[float] = None, 
               max_tokens: Optional[int] = None,
               system: Optional[str] = None) -> str:
        """
        Generate text from a prompt, returning just the content.
        
        This is a simplified interface that just returns the generated text.
        
        Args:
            prompt: The user prompt
            temperature: Optional temperature override
            max_tokens: Optional max tokens override
            system: Optional system prompt override
            
        Returns:
            The generated text
        """
        result = self.chat(prompt, temperature, max_tokens, system)
        if "message" in result:
            return result["message"]["content"]
        return ""
    
    def get_usage_stats(self):
        """Get token usage statistics."""
        return {
            "model": self.model,
            "prompt_tokens": self.total_tokens["prompt"],
            "completion_tokens": self.total_tokens["completion"],
            "total_tokens": self.total_tokens["prompt"] + self.total_tokens["completion"],
        }
    
    def reset_usage_stats(self):
        """Reset usage statistics."""
        self.total_tokens = {"prompt": 0, "completion": 0}
        
    def get_and_reset_usage(self):
        """Get the token usage and reset the counter."""
        stats = self.get_usage_stats()
        self.reset_usage_stats()
        return stats

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # Create client
    client = OllamaClient(model="llama3")
    
    # Generate some text
    result = client.generate("Write a hello world program in Python")
    print(f"Response: {result}")
    
    # Get usage stats
    print(f"Usage: {client.get_usage_stats()}")