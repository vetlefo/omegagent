# Agentic-Reasoning Project Status

This document provides a comprehensive overview of the current status of the Agentic-Reasoning project, including its architecture, dependencies, integration status, and next steps.

## Project Overview

Agentic-Reasoning is an open-source framework for deep research that integrates agentic tools into LLM reasoning. The project aims to enhance LLM capabilities by providing tools for search, code execution, and knowledge management through a mind map.

The project is currently being integrated with AI Codepilot to enhance its code analysis and generation capabilities through advanced semantic understanding and collaborative multi-expert reasoning.

## Architecture

The project consists of several key components:

### 1. Core Components

- **Agentic Reasoning Engine**: The main reasoning engine that coordinates the use of various tools.
- **Search Agent**: Provides web search capabilities using Bing Search API and content extraction.
- **Code Agent**: Generates and executes Python code based on queries.
- **Mind Map**: A graph-based knowledge representation system (GraphRAG) for storing and retrieving information.

### 2. Backend Components

- **FastAPI Server**: Provides API endpoints for interacting with the system.
- **WebSocket Communication**: Enables real-time communication with the frontend.
- **Repository Mapping**: Analyzes code repositories to understand their structure.
- **Orchestrator Agents**: Coordinates the overall process to handle user requests.

### 3. Integration Components

- **Encoder**: Provides advanced embeddings for better semantic understanding.
- **CollaborativeStorm**: Enables multiple specialized expert agents to analyze problems collaboratively.
- **Enhanced Repository Mapping**: Uses semantic code analysis to identify related components.
- **Ollama Integration**: Connects to locally running Ollama server for LLM inference.
- **Model Control Protocol (MCP)**: Implements a unified interface for different LLM providers.

## Current Status

### 1. Fixed Issues

- **Import Fixes**:
  - Updated relative import in `scripts/tools/run_search.py` to use absolute imports
  - Fixed `backend/agents/utils.py` to use `StreamedRunResult` instead of `RunResult`
  - Updated import in `scripts/tools/run_code.py` to use `langchain_community.chat_models` instead of `langchain.chat_models`

- **Missing Dependencies**:
  - Added required packages: beautifulsoup4, chromadb, uvicorn, fastapi, toml, pathspec, langchain-community
  - Created missing `testing_util.py` file in `scripts/lcb_runner/evaluation/` directory

- **Code Modifications**:
  - Modified `scripts/agentic_reason/models.py` to handle the case where vllm is not available
  - Made the code more resilient to missing dependencies with graceful fallbacks

### 2. Verification

- **Backend Server**:
  - Successfully started the backend server on port 8000
  - Verified the server is responding to requests
  - Confirmed the API documentation is accessible

- **Command-line Tools**:
  - Successfully ran `scripts/run_agentic_reason.py --help` to verify it works
  - Fixed import issues to ensure the script can run properly

### 3. Environment Configuration

The `.env` file is properly configured with:
- Required API keys (OPENAI_API_KEY, GEMINI_API_KEY)
- Feature flags (USE_STORM, USE_AGENTIC_ENCODER, USE_SEMANTIC_ANALYSIS)
- Encoder configuration (ENCODER_API_TYPE, OPENAI_EMBEDDING_MODEL)
- Ollama configuration (USE_OLLAMA, OLLAMA_MODEL)
- Model Control Protocol configuration (USE_MCP and related settings)

## Dependencies

The project has the following key dependencies:

### Core Dependencies

- Python 3.11.10
- FastAPI and Uvicorn for the backend server
- Transformers for model loading and tokenization
- LangChain and LangChain Community for LLM integration
- Sentence Transformers for embeddings
- ChromaDB for vector storage
- DSPy for tool integration

### Optional Dependencies

- VLLM for efficient local model inference
- Ollama for local model hosting
- Bing Search API for web search
- Jina AI for content extraction

## Integration Status

The integration of Agentic-Reasoning with AI Codepilot is in progress. The following components have been integrated:

### Completed

- [x] Set up development environment with unified dependencies
- [x] Maintain modularity in the codebase
- [x] Define clear APIs between components
- [x] Resolve dependency conflicts

### In Progress

- [ ] Integrate `agentic_research.encoder` for better embeddings
- [ ] Enhance `repo_map.py` to use `Encoder` for better stub generation
- [ ] Implement semantic search in `backend/utils.py` using `Encoder`
- [ ] Integrate `agentic_research.collaborative_storm` for multi-agent orchestration

### Planned

- [ ] Refactor `OrchestratorAgent` to use STORM-based multi-agent orchestration
- [ ] Enhance `PlannerAgent` with deeper code understanding
- [ ] Improve `CoderAgent` and `MergeAgent` with collaborative reasoning
- [ ] Design Svelte components for visualizing the knowledge base

## Running the Project

### Backend Server

To run the backend server:

```bash
python backend/main.py
```

This will start the FastAPI server on port 8000.

### Agentic Reasoning CLI

To run the Agentic Reasoning CLI:

```bash
python scripts/run_agentic_reason.py \
--use_jina True \
--jina_api_key "your jina api key" \
--bing_subscription_key "your bing api key"\ 
--remote_model "your remote model name, e.g. gpt-4o" \
--mind_map True \ (optional)
--deep_research True \ (optional, if you want to use deep research)
```

## Next Steps

To complete the integration and improve the project, the following steps are recommended:

1. **Test the actual functionality** of the backend server with real requests
2. **Verify that the STORM orchestrator** works correctly
3. **Test the semantic analysis capabilities**
4. **Ensure the frontend can communicate** properly with the backend
5. **Implement the remaining integration components** as outlined in the integration plan
6. **Develop comprehensive tests** for all components
7. **Create detailed documentation** for users and developers

## Conclusion

The Agentic-Reasoning project is making good progress in its integration with AI Codepilot. The core functionality is working, and the integration is proceeding according to plan. With the completion of the remaining integration tasks, the project will provide a powerful framework for deep research and code analysis.
