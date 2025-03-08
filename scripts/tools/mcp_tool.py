"""
Model Control Protocol (MCP) Tool for Agentic-Reasoning.

This tool provides a unified interface to various LLM backends (OpenAI, Azure, Ollama, etc.)
allowing for flexible model selection and fallback strategies.
"""

import os
import json
import logging
import time
from typing import Dict, List, Optional, Union, Any, Literal

# Import model clients
from agentic_research.lm import LitellmModel
from scripts.tools.ollama_client import OllamaClient

logger = logging.getLogger(__name__)

class MCPTool:
    """
    Model Control Protocol Tool for managing and interacting with various LLM providers.
    
    This tool provides:
    1. A unified interface for different LLM backends
    2. Automatic fallback between models
    3. Connection health monitoring
    4. Performance tracking
    5. Cost estimation
    """
    
    def __init__(
        self,
        primary_provider: str = "openai",
        primary_model: str = "gpt-4o",
        fallback_provider: Optional[str] = "ollama",
        fallback_model: Optional[str] = "llama3",
        temperature: float = 0.7,
        max_tokens: int = 2000,
        system_prompt: Optional[str] = None,
    ):
        """
        Initialize the MCP Tool.
        
        Args:
            primary_provider: The primary LLM provider (openai, azure, ollama)
            primary_model: The primary model to use
            fallback_provider: Optional fallback provider if primary fails
            fallback_model: Optional fallback model if primary fails
            temperature: Generation temperature
            max_tokens: Maximum tokens to generate
            system_prompt: Optional system prompt
        """
        self.primary_provider = primary_provider
        self.primary_model = primary_model
        self.fallback_provider = fallback_provider
        self.fallback_model = fallback_model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.system_prompt = system_prompt
        
        self.primary_client = None
        self.fallback_client = None
        self.primary_available = False
        self.fallback_available = False
        self.total_tokens = {"prompt": 0, "completion": 0}
        
        # Initialize clients
        self._initialize_clients()
        
        # Track performance metrics
        self.performance_metrics = {
            "requests": 0,
            "primary_success": 0,
            "fallback_success": 0,
            "failures": 0,
            "avg_response_time": 0,
        }
    
    def _initialize_clients(self):
        """Initialize the primary and fallback clients."""
        # Initialize primary client
        try:
            if self.primary_provider.lower() == "openai":
                self.primary_client = LitellmModel(
                    model=self.primary_model,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                )
                self.primary_available = True
                logger.info(f"Initialized OpenAI client with model: {self.primary_model}")
                
            elif self.primary_provider.lower() == "azure":
                self.primary_client = LitellmModel(
                    model=f"azure/{self.primary_model}",
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    model_type="chat"
                )
                self.primary_available = True
                logger.info(f"Initialized Azure client with model: {self.primary_model}")
                
            elif self.primary_provider.lower() == "ollama":
                try:
                    self.primary_client = OllamaClient(
                        model=self.primary_model,
                        temperature=self.temperature,
                        max_tokens=self.max_tokens,
                        system_prompt=self.system_prompt
                    )
                    self.primary_available = True
                    logger.info(f"Initialized Ollama client with model: {self.primary_model}")
                except ConnectionError:
                    logger.error("Failed to connect to Ollama API")
                    self.primary_available = False
            
            else:
                logger.error(f"Unsupported primary provider: {self.primary_provider}")
                self.primary_available = False
                
        except Exception as e:
            logger.error(f"Error initializing primary client: {e}")
            self.primary_available = False
        
        # Initialize fallback client if specified
        if self.fallback_provider and self.fallback_model:
            try:
                if self.fallback_provider.lower() == "openai":
                    self.fallback_client = LitellmModel(
                        model=self.fallback_model,
                        temperature=self.temperature,
                        max_tokens=self.max_tokens,
                    )
                    self.fallback_available = True
                    logger.info(f"Initialized OpenAI fallback client with model: {self.fallback_model}")
                    
                elif self.fallback_provider.lower() == "azure":
                    self.fallback_client = LitellmModel(
                        model=f"azure/{self.fallback_model}",
                        temperature=self.temperature,
                        max_tokens=self.max_tokens,
                        model_type="chat"
                    )
                    self.fallback_available = True
                    logger.info(f"Initialized Azure fallback client with model: {self.fallback_model}")
                    
                elif self.fallback_provider.lower() == "ollama":
                    try:
                        self.fallback_client = OllamaClient(
                            model=self.fallback_model,
                            temperature=self.temperature,
                            max_tokens=self.max_tokens,
                            system_prompt=self.system_prompt
                        )
                        self.fallback_available = True
                        logger.info(f"Initialized Ollama fallback client with model: {self.fallback_model}")
                    except ConnectionError:
                        logger.error("Failed to connect to Ollama API for fallback")
                        self.fallback_available = False
                
                else:
                    logger.error(f"Unsupported fallback provider: {self.fallback_provider}")
                    self.fallback_available = False
                    
            except Exception as e:
                logger.error(f"Error initializing fallback client: {e}")
                self.fallback_available = False
    
    def _update_metrics(self, start_time: float, success: bool, used_fallback: bool):
        """Update performance metrics."""
        self.performance_metrics["requests"] += 1
        response_time = time.time() - start_time
        
        # Update average response time
        total_time = (self.performance_metrics["avg_response_time"] * 
                     (self.performance_metrics["requests"] - 1) + 
                     response_time)
        self.performance_metrics["avg_response_time"] = total_time / self.performance_metrics["requests"]
        
        if success:
            if used_fallback:
                self.performance_metrics["fallback_success"] += 1
            else:
                self.performance_metrics["primary_success"] += 1
        else:
            self.performance_metrics["failures"] += 1
    
    def _update_token_count(self, provider: str, model: str, prompt_tokens: int, completion_tokens: int):
        """Update token usage and cost estimates."""
        self.total_tokens["prompt"] += prompt_tokens
        self.total_tokens["completion"] += completion_tokens
    
    def generate(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        force_provider: Optional[str] = None,
        force_model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Generate text using the configured models with fallback support.
        
        Args:
            prompt: The prompt to send to the model
            system_prompt: Optional system prompt override
            temperature: Optional temperature override
            max_tokens: Optional max tokens override
            force_provider: Force a specific provider
            force_model: Force a specific model
            
        Returns:
            Dict containing the generation results and metadata
        """
        start_time = time.time()
        result = {
            "success": False,
            "text": "",
            "provider": None,
            "model": None,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "elapsed_time": 0,
        }
        
        # Override provider and model if specified
        if force_provider and force_model:
            if force_provider.lower() == "openai":
                client = LitellmModel(
                    model=force_model,
                    temperature=temperature or self.temperature,
                    max_tokens=max_tokens or self.max_tokens,
                )
            elif force_provider.lower() == "azure":
                client = LitellmModel(
                    model=f"azure/{force_model}",
                    temperature=temperature or self.temperature,
                    max_tokens=max_tokens or self.max_tokens,
                    model_type="chat"
                )
            elif force_provider.lower() == "ollama":
                client = OllamaClient(
                    model=force_model,
                    temperature=temperature or self.temperature,
                    max_tokens=max_tokens or self.max_tokens,
                    system_prompt=system_prompt or self.system_prompt
                )
            else:
                logger.error(f"Unsupported forced provider: {force_provider}")
                self._update_metrics(start_time, False, False)
                result["elapsed_time"] = time.time() - start_time
                return result
            
            try:
                if force_provider.lower() in ["openai", "azure"]:
                    messages = [{"role": "user", "content": prompt}]
                    if system_prompt or self.system_prompt:
                        messages.insert(0, {"role": "system", "content": system_prompt or self.system_prompt})
                    
                    response = client(messages=messages)
                    text = response[0]
                    
                    # Get token usage
                    if hasattr(client, "get_usage_and_reset"):
                        usage = client.get_usage_and_reset()
                        model_name = list(usage.keys())[0]
                        prompt_tokens = usage[model_name]["prompt_tokens"]
                        completion_tokens = usage[model_name]["completion_tokens"]
                        self._update_token_count(force_provider, force_model, prompt_tokens, completion_tokens)
                        
                        result["prompt_tokens"] = prompt_tokens
                        result["completion_tokens"] = completion_tokens
                    
                elif force_provider.lower() == "ollama":
                    text = client.generate(prompt, temperature, max_tokens, system_prompt)
                    
                    # Get token usage
                    usage = client.get_and_reset_usage()
                    prompt_tokens = usage["prompt_tokens"]
                    completion_tokens = usage["completion_tokens"]
                    self._update_token_count(force_provider, force_model, prompt_tokens, completion_tokens)
                    
                    result["prompt_tokens"] = prompt_tokens
                    result["completion_tokens"] = completion_tokens
                
                result["success"] = True
                result["text"] = text
                result["provider"] = force_provider
                result["model"] = force_model
                
                self._update_metrics(start_time, True, False)
                result["elapsed_time"] = time.time() - start_time
                return result
                
            except Exception as e:
                logger.error(f"Error with forced provider {force_provider}/{force_model}: {e}")
                self._update_metrics(start_time, False, False)
                result["elapsed_time"] = time.time() - start_time
                return result
        
        # Try primary provider
        used_fallback = False
        if self.primary_available:
            try:
                if self.primary_provider.lower() in ["openai", "azure"]:
                    messages = [{"role": "user", "content": prompt}]
                    if system_prompt or self.system_prompt:
                        messages.insert(0, {"role": "system", "content": system_prompt or self.system_prompt})
                    
                    response = self.primary_client(messages=messages)
                    text = response[0]
                    
                    # Get token usage
                    if hasattr(self.primary_client, "get_usage_and_reset"):
                        usage = self.primary_client.get_usage_and_reset()
                        model_name = list(usage.keys())[0]
                        prompt_tokens = usage[model_name]["prompt_tokens"]
                        completion_tokens = usage[model_name]["completion_tokens"]
                        self._update_token_count(self.primary_provider, self.primary_model, prompt_tokens, completion_tokens)
                        
                        result["prompt_tokens"] = prompt_tokens
                        result["completion_tokens"] = completion_tokens
                    
                elif self.primary_provider.lower() == "ollama":
                    text = self.primary_client.generate(prompt, temperature, max_tokens, system_prompt)
                    
                    # Get token usage
                    usage = self.primary_client.get_and_reset_usage()
                    prompt_tokens = usage["prompt_tokens"]
                    completion_tokens = usage["completion_tokens"]
                    self._update_token_count(self.primary_provider, self.primary_model, prompt_tokens, completion_tokens)
                    
                    result["prompt_tokens"] = prompt_tokens
                    result["completion_tokens"] = completion_tokens
                
                result["success"] = True
                result["text"] = text
                result["provider"] = self.primary_provider
                result["model"] = self.primary_model
                
                self._update_metrics(start_time, True, False)
                result["elapsed_time"] = time.time() - start_time
                return result
                
            except Exception as e:
                logger.error(f"Error with primary provider {self.primary_provider}/{self.primary_model}: {e}")
                # Fall through to fallback
        
        # Try fallback if available
        if self.fallback_available:
            used_fallback = True
            try:
                if self.fallback_provider.lower() in ["openai", "azure"]:
                    messages = [{"role": "user", "content": prompt}]
                    if system_prompt or self.system_prompt:
                        messages.insert(0, {"role": "system", "content": system_prompt or self.system_prompt})
                    
                    response = self.fallback_client(messages=messages)
                    text = response[0]
                    
                    # Get token usage
                    if hasattr(self.fallback_client, "get_usage_and_reset"):
                        usage = self.fallback_client.get_usage_and_reset()
                        model_name = list(usage.keys())[0]
                        prompt_tokens = usage[model_name]["prompt_tokens"]
                        completion_tokens = usage[model_name]["completion_tokens"]
                        self._update_token_count(self.fallback_provider, self.fallback_model, prompt_tokens, completion_tokens)
                        
                        result["prompt_tokens"] = prompt_tokens
                        result["completion_tokens"] = completion_tokens
                    
                elif self.fallback_provider.lower() == "ollama":
                    text = self.fallback_client.generate(prompt, temperature, max_tokens, system_prompt)
                    
                    # Get token usage
                    usage = self.fallback_client.get_and_reset_usage()
                    prompt_tokens = usage["prompt_tokens"]
                    completion_tokens = usage["completion_tokens"]
                    self._update_token_count(self.fallback_provider, self.fallback_model, prompt_tokens, completion_tokens)
                    
                    result["prompt_tokens"] = prompt_tokens
                    result["completion_tokens"] = completion_tokens
                
                result["success"] = True
                result["text"] = text
                result["provider"] = self.fallback_provider
                result["model"] = self.fallback_model
                
                self._update_metrics(start_time, True, True)
                result["elapsed_time"] = time.time() - start_time
                return result
                
            except Exception as e:
                logger.error(f"Error with fallback provider {self.fallback_provider}/{self.fallback_model}: {e}")
                # Both primary and fallback failed
        
        # All attempts failed
        self._update_metrics(start_time, False, used_fallback)
        result["elapsed_time"] = time.time() - start_time
        return result
    
    def get_performance_metrics(self):
        """Get performance metrics."""
        return self.performance_metrics
    
    def get_token_usage(self):
        """Get token usage statistics."""
        return self.total_tokens
    
    def reset_token_usage(self):
        """Reset token usage statistics."""
        self.total_tokens = {"prompt": 0, "completion": 0}
    
    def get_and_reset_token_usage(self):
        """Get token usage and reset counters."""
        usage = self.get_token_usage()
        self.reset_token_usage()
        return usage
    
    def list_available_models(self):
        """List all available models."""
        models = []
        
        if self.primary_available:
            models.append({
                "provider": self.primary_provider,
                "model": self.primary_model,
                "role": "primary"
            })
        
        if self.fallback_available:
            models.append({
                "provider": self.fallback_provider,
                "model": self.fallback_model,
                "role": "fallback"
            })
            
        return models

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # Create MCP Tool with OpenAI primary and Ollama fallback
    mcp = MCPTool(
        primary_provider="openai",
        primary_model="gpt-4o",
        fallback_provider="ollama",
        fallback_model="llama3",
        temperature=0.7,
        max_tokens=1000
    )
    
    # Generate text
    result = mcp.generate("Explain the concept of distributed consensus in 3 sentences.")
    
    print(f"Provider: {result['provider']}")
    print(f"Model: {result['model']}")
    print(f"Success: {result['success']}")
    print(f"Response: {result['text']}")
    print(f"Tokens: {result['prompt_tokens']} prompt, {result['completion_tokens']} completion")
    print(f"Time: {result['elapsed_time']:.2f} seconds")
    
    # Get metrics
    print(f"Performance: {mcp.get_performance_metrics()}")