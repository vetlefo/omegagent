# Troubleshooting Guide

This guide covers common issues with the Agentic-Reasoning-Master project and their solutions.

## Import and Module Errors

### Missing Module Errors

Problem: `ModuleNotFoundError: No module named 'agentic_research.dataclass'`

Solutions:
1. The project is migrating from `dataclass.py` to `interface.py`. Check DATACLASS_MIGRATION_GUIDE.md
2. Set PYTHONPATH: `export PYTHONPATH=$PYTHONPATH:$(pwd)`
3. Check if you've installed the package: `pip install -e .`

Problem: `ModuleNotFoundError: No module named 'dspy'`

Solutions:
1. Install dspy: `conda activate agentic_reasoning && pip install dspy dspy-ai`
2. If still experiencing errors after installation, make sure you're running in the correct environment
3. Check if imports in code need to be updated from `dspy_ai` to `dspy`

Problem: `AttributeError: module 'dspy' has no attribute 'OpenAI'`

Solutions:
1. The codebase uses an older DSPy API which doesn't exist in newer versions
2. Server will automatically fall back to using pydantic_ai.models.openai.OpenAIModel
3. For a proper fix, update server.py to use the current DSPy API methods

### TODO: DSPy API Upgrade
- Investigate DSPy version compatibility issues (DSPy 2.6.10 doesn't provide expected backends)
- Update DSPy initialization in `backend/server.py` to use the latest DSPy API
- Consider removing dual DSPy/pydantic_ai approach for a more consistent implementation
- Fix CoderAgent to handle the selected LM interface consistently

Problem: Import errors with pydantic-ai components

Solutions:
1. For `ImportError: cannot import name 'RunResult'`, update to: `from pydantic_ai.result import FinalResult as RunResult`
2. For `ImportError: cannot import name 'RunContext'`, use: 
   ```python
   from pydantic_ai.models.openai import OpenAIModel
   from pydantic_ai.result import RunContext
   ```

### Import Issues in Scripts

Problem: Scripts can't find modules within the project

Solutions:
1. Use absolute imports in scripts: `from agentic_research.encoder import Encoder`
2. Use relative imports for modules within packages: `from ..utils import load_config`
3. For tests: `pytest -v path/to/test.py` (pytest adds the current directory to PYTHONPATH)

## Environment Setup Issues

### Conda Environment Creation Fails

Problem: `environment.yml` dependencies can't be resolved

Solutions:
1. Update conda: `conda update -n base -c defaults conda`
2. Try creating with only basic dependencies: `conda create -n agentic_reasoning python=3.11.10`
3. Then install packages manually: `pip install -r requirements.txt`

### API Key Configuration

Problem: "API key not found" or similar error messages

Solutions:
1. Create a `.env` file in the project root with all required keys:
   ```
   OPENAI_API_KEY=your_openai_key
   GEMINI_API_KEY=your_gemini_key
   BING_API_KEY=your_bing_key
   JINA_API_KEY=your_jina_key
   PYTHONPATH=./
   ```
2. Export keys in your shell: `export OPENAI_API_KEY=your_key_here`
3. Check for typos in variable names (e.g., `OPENAI_API_KEY` vs `OPENAI_KEY`)
4. If testing without all keys, you may need to modify server.py to make certain keys optional

## Running the Application

### Backend Server Issues

Problem: Server fails to start or crashes

Solutions:
1. Check logs for specific import or dependency errors
2. Verify all environment variables are correctly set
3. Try running with verbose output: `python -m uvicorn backend.server:app --reload --log-level debug`
4. Try explicitly using the Python interpreter from your conda environment: `conda activate agentic_reasoning && python -m uvicorn backend.server:app --reload`
5. If you get "Address already in use" errors, try a different port: `python -m uvicorn backend.server:app --reload --port 8001`

Problem: Frontend assets fail to load (404 errors for .js and .css files)

Solutions:
1. Ensure index.html references the correct paths for compiled assets:
   - Use `/static/assets/[filename].js` instead of `/src/main.js`
   - Check browser console for specific 404 errors
2. Verify that FastAPI is correctly mounting static files:
   - Make sure `app.mount("/static", StaticFiles(directory="frontend"), name="static")` is in server.py
3. If using a non-standard port, update WebSocket URLs in frontend code
4. After rebuilding frontend with `npm run build`, copy the new assets to the server-accessible location:
   ```bash
   # Copy new built assets to the frontend/assets directory (accessed via /static/assets/)
   cp frontend/dist/assets/* frontend/assets/
   
   # Update index.html to reference the new filenames (they contain hashes)
   cp frontend/dist/index.html frontend/index.html
   sed -i '' 's|"/assets/|"/static/assets/|g' frontend/index.html
   ```

### CLI Tool Issues

Problem: `scripts/run_agentic_reason.py` fails to run

Solutions:
1. Ensure required arguments are provided (e.g., `--remote_model gpt-4o`)
2. Check if API keys are properly configured
3. Try running with `--help` to see all required parameters

## Feature-Specific Issues

### STORM Orchestration Issues

Problem: Storm-based multi-agent isn't working

Solutions:
1. Verify `USE_STORM=true` is set in environment
2. Check if API context length is sufficient for your LLM
3. Review logs for specific error messages

### GraphRAG/Mind Map Issues

Problem: Graph-based knowledge retrieval not working

Solutions:
1. Ensure dependencies are installed: `pip install networkx pyvis`
2. Check cache directory permissions
3. Try clearing existing caches in nano_graphrag_cache_* directories

## Debugging Tips

1. Enable verbose logging: Add `--log-level debug` to commands
2. Check for conflicting dependencies: `pip check`
3. Isolate issues by running minimal examples from `scripts/test_minimal.py`
4. Use print statements or logging to track execution flow
5. Check Python version: The project requires Python 3.11.10

## Still Having Issues?

- Check if your issue is addressed in IMPLEMENTATION_PREREQUISITES.md
- Review the PROJECT_STATUS.md document for known limitations
- Search the issues in the repository for similar problems and solutions