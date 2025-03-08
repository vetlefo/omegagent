# Quick Start Guide

This guide provides the fastest way to get the Agentic-Reasoning-Master project up and running.

## Prerequisites

- Python 3.11.10
- Conda (recommended)
- Node.js (for frontend)
- API keys for OpenAI, Bing, and others as needed

## Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Agentic-Reasoning-Master.git
   cd Agentic-Reasoning-Master
   ```

2. **Set up the environment**:
   ```bash
   conda env create -f environment.yml
   conda activate agentic_reasoning
   pip install -e .
   ```

3. **Configure API keys** - Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_openai_key
   BING_API_KEY=your_bing_key
   GEMINI_API_KEY=your_gemini_key 
   JINA_API_KEY=your_jina_key
   USE_AGENTIC_ENCODER=true
   USE_SEMANTIC_ANALYSIS=true
   ```

4. **Fix import issues** (temporary solution):
   ```bash
   export PYTHONPATH=$PYTHONPATH:$(pwd)
   ```

## Running the Backend

```bash
conda activate agentic_reasoning
python -m uvicorn backend.server:app --reload
```

If you encounter port conflicts:
```bash
python -m uvicorn backend.server:app --reload --port 8001
```

Access the API documentation at `http://localhost:8000/docs` (or the appropriate port)

## Running the CLI

```bash
python scripts/run_agentic_reason.py --remote_model gpt-4o
```

## Running the Frontend

```bash
cd frontend
npm install
npm run dev
```

Access the frontend at `http://localhost:5173`

## Common Issues

- **Import errors**: Use the PYTHONPATH fix or check DATACLASS_MIGRATION_GUIDE.md
- **Missing dependencies**: Install additional requirements with `pip install -r requirements.txt`
- **API key errors**: Check your .env file and ensure all required keys are set
- **Module errors**: Install missing packages like `pip install dspy dspy-ai pydantic-ai`
- **Import structure changes**: If encountering import errors related to `RunResult` or `RunContext`, see TROUBLESHOOTING.md

## Feature Flags

Enable advanced features through environment variables:

- Storm orchestration: `export USE_STORM=true`
- Semantic search: `export USE_AGENTIC_ENCODER=true USE_SEMANTIC_ANALYSIS=true`
- Ollama integration: `export USE_OLLAMA=true OLLAMA_MODEL=llama3`
- Multi-provider LLM: `export USE_MCP=true MCP_PRIMARY_PROVIDER=openai MCP_PRIMARY_MODEL=gpt-4o`

For more detailed information, see the README.md and CLAUDE.md files.