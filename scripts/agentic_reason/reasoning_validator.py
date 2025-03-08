from typing import List, Dict, Optional
import logging

class ReasoningValidator:
    """Evaluates and validates reasoning chains for consistency and accuracy."""
    
    def __init__(self):
        """Initialize the ReasoningValidator with logging."""
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
    
    def validate_reasoning(
        self,
        reasoning_chain: List[str],
        query: str,
        evidence: Optional[List[str]] = None
    ) -> Dict[str, any]:
        """
        Validate a reasoning chain against a query and optional evidence.
        
        Args:
            reasoning_chain (List[str]): List of reasoning steps.
            query (str): The original query or task.
            evidence (Optional[List[str]]): Supporting evidence or context.
        
        Returns:
            Dict[str, any]: Validation result with score, issues, and confidence.
        """
        if not reasoning_chain:
            return {
                "is_valid": False,
                "score": 0.0,
                "issues": ["No reasoning chain provided."],
                "confidence": 0.0
            }
        
        # Basic checks
        issues = []
        score = 1.0
        
        # Check coherence (simple length and content check)
        if len(reasoning_chain) < 1:
            issues.append("Reasoning chain too short.")
            score -= 0.3
        for i, step in enumerate(reasoning_chain):
            if not step.strip():
                issues.append(f"Step {i + 1} is empty.")
                score -= 0.1
        
        # Check relevance to query (heuristic: keyword overlap)
        query_words = set(query.lower().split())
        chain_text = " ".join(reasoning_chain).lower()
        overlap = len(query_words.intersection(set(chain_text.split())))
        relevance = overlap / max(len(query_words), 1)
        if relevance < 0.5:
            issues.append("Low relevance to query.")
            score -= 0.2
        
        # Evidence consistency (if provided)
        if evidence:
            evidence_text = " ".join(evidence).lower()
            evidence_words = set(evidence_text.split())
            evidence_overlap = len(set(chain_text.split()).intersection(evidence_words))
            evidence_relevance = evidence_overlap / max(len(evidence_words), 1)
            if evidence_relevance < 0.3:
                issues.append("Inconsistent with provided evidence.")
                score -= 0.3
        
        score = max(0.0, min(1.0, score))
        confidence = score * 0.9 + 0.1 if score > 0.5 else score
        
        self.logger.info(f"Validated reasoning: Score={score}, Issues={len(issues)}")
        return {
            "is_valid": score >= 0.7,
            "score": score,
            "issues": issues,
            "confidence": confidence
        }