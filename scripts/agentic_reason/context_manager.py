from typing import List, Dict, Optional
import numpy as np
from sentence_transformers import SentenceTransformer
import logging

class ContextWindowManager:
    """Dynamically manages and optimizes context windows for reasoning tasks."""
    
    def __init__(self, max_tokens: int = 32768, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the ContextWindowManager with a token limit and embedding model.
        
        Args:
            max_tokens (int): Maximum tokens allowed in the context window.
            model_name (str): Name of the sentence transformer model for embeddings.
        """
        self.max_tokens = max_tokens
        self.model = SentenceTransformer(model_name)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
    
    def tokenize_estimate(self, text: str) -> int:
        """Estimate token count using a simple heuristic (words + 20% for punctuation)."""
        words = len(text.split())
        return int(words * 1.2)
    
    def compute_relevance(self, query: str, contexts: List[str]) -> List[float]:
        """Compute relevance scores for contexts relative to the query using embeddings."""
        query_embedding = self.model.encode([query])[0]
        context_embeddings = self.model.encode(contexts)
        similarities = [
            np.dot(query_embedding, ctx_emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(ctx_emb))
            for ctx_emb in context_embeddings
        ]
        return similarities
    
    def optimize_context(
        self, query: str, contexts: List[str], metadata: Optional[List[Dict]] = None
    ) -> Dict[str, str]:
        """
        Optimize context by selecting the most relevant pieces within token limits.
        
        Args:
            query (str): The query or task description.
            contexts (List[str]): List of potential context pieces (e.g., files, posts).
            metadata (Optional[List[Dict]]): Optional metadata for each context (e.g., source).
        
        Returns:
            Dict[str, str]: Optimized context with 'primary' and 'summary' sections.
        """
        if not contexts:
            return {"primary": "", "summary": "No context provided."}
        
        # Estimate token counts
        token_counts = [self.tokenize_estimate(ctx) for ctx in contexts]
        total_tokens = sum(token_counts)
        
        if total_tokens <= self.max_tokens:
            return {"primary": "\n".join(contexts), "summary": ""}
        
        # Compute relevance scores
        scores = self.compute_relevance(query, contexts)
        ranked_indices = np.argsort(scores)[::-1]  # Descending order
        
        # Select top contexts until token limit
        selected_contexts = []
        current_tokens = 0
        for idx in ranked_indices:
            if current_tokens + token_counts[idx] <= self.max_tokens:
                selected_contexts.append(contexts[idx])
                current_tokens += token_counts[idx]
        
        # Summarize remaining contexts if any
        remaining_contexts = [ctx for i, ctx in enumerate(contexts) if i not in ranked_indices[:len(selected_contexts)]]
        summary = (
            f"Summarized {len(remaining_contexts)} additional contexts (excluded due to token limit): "
            f"Total tokens exceeded by {total_tokens - self.max_tokens}."
        )
        
        self.logger.info(f"Optimized context: {len(selected_contexts)} pieces selected, {len(remaining_contexts)} summarized.")
        return {
            "primary": "\n".join(selected_contexts),
            "summary": summary if remaining_contexts else ""
        }