# Agentic-Reasoning Dev Guide

## Development Priorities
- IMPORTANT: Follow the structured roadmap in CODEBASE_IMPROVEMENT_ROADMAP.md
- Do not proceed to next phase until success criteria are met
- Focus on completing Phase 1 (Session Management & Configuration) first
- All changes must align with the roadmap's principles and guidelines

## Build/Test/Lint Commands
- Run all tests: `pytest -v agentic_research`
- Run single test: `pytest -v agentic_research/path/to/test.py::test_function_name`
- Install package: `pip install -e .`
- Start application: `python scripts/run_agentic_reason.py --bing_subscription_key <key> --remote_model gpt-4o`
- Start server: `python -m uvicorn backend.server:app --reload`

## Environment Setup
- Use conda: `conda env create -f environment.yml && conda activate agentic_reasoning`
- Required API keys: OPENAI_API_KEY, YDC_API_KEY, BING_API_KEY, JINA_API_KEY

## Integration Features
- Semantic search/analysis: `export USE_AGENTIC_ENCODER=true USE_SEMANTIC_ANALYSIS=true`
- StormOrchestrator: `export USE_STORM=true` (API: `{"config": {"use_storm": true}}`)
- Embedding models: `export ENCODER_API_TYPE=openai OPENAI_EMBEDDING_MODEL=text-embedding-3-small`
- Ollama integration: `export USE_OLLAMA=true OLLAMA_MODEL=llama3`
- MCP: `export USE_MCP=true MCP_PRIMARY_PROVIDER=openai MCP_PRIMARY_MODEL=gpt-4o`

## Code Style Guidelines
- PEP 8 conventions with 88 char line length
- Type hints required for all function parameters and return values
- Naming: PascalCase (classes), snake_case (functions/variables), UPPER_CASE (constants)
- Imports: Use relative imports within packages
- Error handling: Use try/except with specific exceptions (not bare except)
- Formatting: Use f-strings for string formatting
- Documentation: Docstrings for all public functions and classes

## Architecture Principles
- Single Responsibility: Each class/module should have one reason to change
- Dependency Injection: Pass dependencies to classes rather than creating internally
- Configuration Centralization: No direct environment variable access in business logic
- Error Recovery: Design for resilience with proper error handling
- State Management: Maintain consistent state across user sessions and reconnections
- Testing: Write tests before implementing new features or significant changes