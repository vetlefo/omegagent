import dspy
import os
import json
import time
import sys
import re
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from backend.utils import ensure_imports

try:
    from scripts.tools.bing_search import bing_web_search, extract_relevant_info
except ImportError:
    # Mock these functions if they can't be imported
    def bing_web_search(*args, **kwargs):
        return {}
    
    def extract_relevant_info(*args, **kwargs):
        return []

# Type definitions needed by CoderAgent
@dataclass
class CodeUpdate:
    """A single code update, containing filename, original code, and updated code."""
    filename: str
    original_code: str = ""
    updated_code: str = ""
    explanation: str = ""

@dataclass
class FullCodeUpdates:
    """A collection of code updates for multiple files."""
    updates: List[CodeUpdate] = field(default_factory=list)

CodeResponse = str

class CoderAgent:
    """An agent responsible for generating code, enhanced with external tools for research and knowledge retrieval."""

    def __init__(self, lm=None, logger=None, review=True, max_iterations=1, comm=None, root_directory="."):
        self.lm = lm
        self.logger = logger
        self.review = review
        self.max_iterations = max_iterations
        self.comm = comm
        self.root_directory = root_directory

    async def update_code(self, task: str, context: str) -> FullCodeUpdates:
        """Update code based on the task description and context."""
        # This is a simplified implementation - in a real implementation, you would:
        # 1. Parse the task to understand what needs to be updated
        # 2. Extract relevant files from the context
        # 3. Generate updates based on the task requirements
        
        if self.logger:
            self.logger.info(f"Generating code updates for task: {task}")
            
        # For demo purposes, we'll just create a simple update
        updates = FullCodeUpdates(updates=[
            CodeUpdate(
                filename="example.py",
                original_code="# This is an example file\n\nprint('Hello, world!')",
                updated_code="# This is an example file - updated\n\nprint('Hello, world from CoderAgent!')",
                explanation="Updated the print statement to include the agent name."
            )
        ])
        
        return updates

    def generate_code(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate code using LLM, augmented with BingSearch and KnowledgeBase tools."""
        if not self.lm:
            return "# No language model available\n# This is placeholder code\n\ndef placeholder():\n    return 'Hello World'"
            
        # Step 1: Search for relevant documentation or examples
        search_results = self._search_relevant_info(prompt)

        # Step 2: Retrieve structured knowledge from KnowledgeBase (Still using your placeholder)
        kb_info = self._retrieve_knowledge(prompt)

        # Combine inputs for LLM
        enhanced_prompt = self._build_enhanced_prompt(prompt, context, search_results, kb_info)

        # Generate code with LLM
        try:
            # Check if self.lm is directly callable (our wrapper) or needs DSPy context
            if hasattr(self.lm, '__call__') and callable(getattr(self.lm, '__call__')):
                try:
                    # Try using the custom DSPyOpenAIWrapper
                    return self.lm(
                        f"Generate code for the following request. Respond with only the code, no explanation:\n\n{enhanced_prompt}"
                    )
                except Exception as direct_call_error:
                    if self.logger:
                        self.logger.error(f"Direct LM call failed: {direct_call_error}, falling back to DSPy")
                    
            # Try using DSPy's prediction framework
            try:
                with dspy.settings.context(lm=self.lm):
                    response = dspy.Predict("prompt -> code")(prompt=enhanced_prompt).code
                return response
            except Exception as dspy_error:
                if self.logger:
                    self.logger.error(f"DSPy prediction failed: {dspy_error}")
                
                # Last resort - simple direct call with error handling
                return self.lm(enhanced_prompt)
                
        except Exception as e:
            if self.logger:
                self.logger.error(f"All code generation methods failed: {e}")
            return f"# Error generating code: {e}\n\n# Placeholder implementation\ndef placeholder():\n    pass"

    @ensure_imports
    def _search_relevant_info(self, query: str) -> List[str]:
        """Use BingSearch tool to fetch relevant information."""
        try:
            # Directly call the bing_web_search function. Get API key from env.
            results = bing_web_search(query, os.getenv("BING_SEARCH_API_KEY"), "https://api.bing.microsoft.com/v7.0/search")
            if results and "webPages" in results and "value" in results["webPages"]:
                return [r['snippet'] for r in extract_relevant_info(results)]
        except Exception as e:
            if self.logger:
                self.logger.warning(f"Error searching information: {e}")
        return []
    
    def _retrieve_knowledge(self, query: str) -> str:
        """Retrieve information from KnowledgeBase."""
        # Placeholder - Replace with your actual knowledge base logic
        return ""  # Return an empty string

    def _build_enhanced_prompt(self, prompt: str, context: Optional[str], search: List[str], kb: str) -> str:
        """Construct an enhanced prompt with external tool outputs."""
        base = f"Generate code for: {prompt}"
        if context:
            base += f"\nContext: {context}"
        if search:
            search_items = "\n".join(f"- {s}" for s in search)
            base += "\nRelevant Info:\n" + search_items
        if kb:
            base += f"\nKnowledge Base: {kb}"
        return base

# These classes are now defined at the top of the file