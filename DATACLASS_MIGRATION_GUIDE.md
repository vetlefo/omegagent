# Dataclass Migration Guide

## Overview

The `agentic_research/dataclass.py` file has been removed, and all its contents have been moved to `agentic_research/interface.py`. This document outlines the remaining files that need to be updated to fix import errors.

## Already Fixed Files

The following files have already been fixed by updating their imports:

- `agentic_research/collaborative_storm/modules/article_generation.py`
- `agentic_research/collaborative_storm/modules/information_insertion_module.py`
- `agentic_research/collaborative_storm/modules/knowledge_base_summary.py`
- `agentic_research/collaborative_storm/modules/warmstart_hierarchical_chat.py`
- `agentic_research/collaborative_storm/modules/costorm_expert_utterance_generator.py`
- `agentic_research/collaborative_storm/modules/grounded_question_generation.py`
- `agentic_research/collaborative_storm/modules/simulate_user.py`
- `agentic_research/collaborative_storm/engine.py`

## Remaining Files to Fix

The following files still need to be updated:

### Core Files
1. `agentic_research/collaborative_storm/runner.py`
   - Change `from ..dataclass import ConversationTurn, KnowledgeBase` to `from ..interface import ConversationTurn, KnowledgeBase`

2. `backend/agents/storm_orchestrator_agent.py`
   - Change `from agentic_research.dataclass import ConversationTurn` to `from agentic_research.interface import ConversationTurn`

### Test Files
3. `scripts/test_qdrant_store.py`
   - Change `from agentic_research.dataclass import ConversationTurn` to `from agentic_research.interface import ConversationTurn`

4. `scripts/test_minimal.py`
   - Change `from agentic_research.dataclass import ConversationTurn` to `from agentic_research.interface import ConversationTurn`

5. `scripts/test_agentic_reasoning.py`
   - Change `from agentic_research.dataclass import ConversationTurn` to `from agentic_research.interface import ConversationTurn`

### Other Potential Files
The following files may need to be checked, but they use a different import pattern:

- Various files in `agentic_research/storm_analysis/modules/` that import from `.storm_dataclass`
  - These are likely internal to the storm_analysis package and may not need updating if they don't also import from `agentic_research.dataclass`

## Testing

After updating the imports, test the application using:

```bash
python backend/main.py
```

Or:

```bash
uvicorn backend.server:app --reload
```

## Additional Notes

- When updating imports, make sure to use absolute imports from the `agentic_research` package (e.g., `from agentic_research.interface import ...`) instead of relative imports (e.g., `from ...dataclass import ...`).
- The `KnowledgeNode` class has been added to `interface.py`, ensuring that all files importing it will work correctly.
- If you encounter any more import errors, check the traceback to identify which file is still using the old import and update it accordingly.