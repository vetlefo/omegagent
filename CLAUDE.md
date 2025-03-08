# Agentic-Reasoning Master Guide

## Current Status
This codebase is a merged repository from three separate Agentic-Reasoning/Codepilot projects.
Currently addressing import and dependency issues before full functionality.

## Build/Test/Lint Commands
- Install package: `pip install -e .`
- Fix import issues: `export PYTHONPATH=$PYTHONPATH:$(pwd)`
- Run tests: `pytest -v agentic_research` or specific: `pytest -v scripts/test_agentic_reasoning.py`
- Start backend server: `python -m uvicorn backend.server:app --reload` (IMPORTANT: Use `python -m` prefix)
- Start CLI: `python scripts/run_agentic_reason.py --remote_model gpt-4o`
- Frontend dev: `cd frontend && npm run dev`
- Frontend build: `cd frontend && npm run build`
- Frontend deployment: After building, copy assets: `cp frontend/dist/assets/* frontend/assets/` and update HTML paths

## Environment Setup
- Python 3.11.10: `conda env create -f environment.yml && conda activate agentic_reasoning`
- Required API keys in .env: OPENAI_API_KEY, BING_API_KEY, GEMINI_API_KEY, JINA_API_KEY
- Feature flags: USE_STORM, USE_AGENTIC_ENCODER, USE_SEMANTIC_ANALYSIS, USE_MCP
- See INTEGRATION_GUIDE.md and DATACLASS_MIGRATION_GUIDE.md for dependency fixes

## Architecture Components
- Backend: FastAPI server with agent orchestration (coder, planner, orchestrator agents)
- Frontend: Svelte-based UI for interaction
- Core: agentic_research/ modules for reasoning and collaboration
- Search Agent: Web search with Bing API and content extraction
- Code Agent: Code generation and execution
- GraphRAG: Mind map for knowledge storage and retrieval
- STORM Orchestration: Multi-expert agent collaboration

## Integration Features
- Semantic search: `export USE_AGENTIC_ENCODER=true USE_SEMANTIC_ANALYSIS=true`
- Multi-expert agents: `export USE_STORM=true` (API: `{"config": {"use_storm": true}}`)
- Multi-provider LLM: `export USE_MCP=true MCP_PRIMARY_PROVIDER=openai MCP_PRIMARY_MODEL=gpt-4o`
- Local inference: `export USE_OLLAMA=true OLLAMA_MODEL=llama3`

## Code Style Guidelines
- PEP 8 conventions with 88 char line length
- Type hints for all function parameters and return values
- Naming: PascalCase (classes), snake_case (functions/variables), UPPER_CASE (constants)
- Imports: Use relative imports within packages, standard library first
- Error handling: Specific exceptions, never use bare except
- Documentation: Docstrings for all public functions and classes

## Implementation Priorities
1. Persistent session storage (SQLite/Redis/PostgreSQL)
2. Memory management for large structures
3. Centralized environment configuration
4. Error recovery and state persistence
5. WebSocket connection for continuous orchestration
6. See IMPLEMENTATION_PREREQUISITES.md for details