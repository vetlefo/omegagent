from typing import List, Dict, Optional
import re
import logging

class KnowledgeSynthesizer:
    """Aggregates and synthesizes knowledge from multiple sources for coherent reasoning."""
    
    def __init__(self):
        """Initialize the KnowledgeSynthesizer with logging."""
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
    
    def clean_text(self, text: str) -> str:
        """Clean text by removing excessive whitespace and normalizing."""
        return re.sub(r'\s+', ' ', text.strip())
    
    def synthesize(
        self,
        sources: List[Dict[str, str]],
        query: str,
        max_length: int = 5000
    ) -> Dict[str, str]:
        """
        Synthesize knowledge from multiple sources into a coherent summary.
        
        Args:
            sources (List[Dict[str, str]]): List of source dicts with 'content' and 'origin' keys.
            query (str): The query guiding the synthesis.
            max_length (int): Maximum character length of the synthesized output.
        
        Returns:
            Dict[str, str]: Synthesized knowledge with 'content' and 'metadata'.
        """
        if not sources:
            return {"content": "No sources provided.", "metadata": ""}
        
        # Aggregate and clean content
        aggregated = []
        metadata_entries = []
        for source in sources:
            content = self.clean_text(source.get('content', ''))
            origin = source.get('origin', 'Unknown')
            aggregated.append(f"From {origin}: {content}")
            metadata_entries.append(f"Source: {origin}, Length: {len(content)} chars")
        
        # Initial synthesis
        synthesis = "\n\n".join(aggregated)
        if len(synthesis) <= max_length:
            return {
                "content": synthesis,
                "metadata": "; ".join(metadata_entries)
            }
        
        # Truncate and summarize
        truncated = synthesis[:max_length]
        last_period = truncated.rfind('.')
        if last_period > max_length // 2:
            truncated = truncated[:last_period + 1]
        
        summary_note = f"\n\n[Truncated: Original length {len(synthesis)} chars, reduced to {len(truncated)} chars.]"
        self.logger.info(f"Synthesized knowledge truncated from {len(synthesis)} to {len(truncated)} chars.")
        
        return {
            "content": truncated + summary_note,
            "metadata": "; ".join(metadata_entries) + f"; Truncated: Yes"
        }