import dspy
from typing import Optional, List
from backend.utils import log_event
from scripts.lcb_runner.runner import BingSearchTool, KnowledgeBaseTool

class CoderAgent:
    """An agent responsible for generating code, enhanced with external tools for research and knowledge retrieval."""
    
    def __init__(self, lm: dspy.LM, logger):
        self.lm = lm
        self.logger = logger
        self.bing_search = BingSearchTool()
        self.knowledge_base = KnowledgeBaseTool()
        
    @log_event("CoderAgent: Generating code with external tools")
    def generate_code(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate code using LLM, augmented with BingSearch and KnowledgeBase tools."""
        # Step 1: Search for relevant documentation or examples
        search_results = self._search_relevant_info(prompt)
        
        # Step 2: Retrieve structured knowledge from KnowledgeBase
        kb_info = self._retrieve_knowledge(prompt)
        
        # Combine inputs for LLM
        enhanced_prompt = self._build_enhanced_prompt(prompt, context, search_results, kb_info)
        
        # Generate code with LLM
        with dspy.settings.context(lm=self.lm):
            response = dspy.Predict("prompt -> code")(prompt=enhanced_prompt).code
        return response
    
    def _search_relevant_info(self, query: str) -> List[str]:
        """Use BingSearch tool to fetch relevant information."""
        results = self.bing_search.search(query, top_k=3)
        return [result.snippet for result in results]
    
    def _retrieve_knowledge(self, query: str) -> str:
        """Retrieve information from KnowledgeBase."""
        return self.knowledge_base.query(query) or ""
    
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

# Type definitions for external use
CodeResponse = str