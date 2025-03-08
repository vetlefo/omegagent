# Component Overview

This document provides a high-level overview of the major components in the Agentic-Reasoning-Master project.

## Core Components

### 1. Agentic Research Library (`agentic_research/`)

The foundational library that provides reasoning capabilities:

- **Encoder** (`encoder.py`): Provides advanced text embeddings for semantic understanding
- **LM Interface** (`lm.py`): Abstracts language model interactions
- **Interface** (`interface.py`): Core data structures and interfaces (replacing `dataclass.py`)
- **RM** (`rm.py`): Reward modeling and evaluation components
- **Utils** (`utils.py`): Common utility functions

### 2. Backend Server (`backend/`)

FastAPI server for API access to reasoning capabilities:

- **Server** (`server.py`): Main FastAPI application with API endpoints
- **Communication** (`communication.py`): WebSocket connection management
- **Repo Map** (`repo_map.py`): Code repository analysis and structure extraction
- **Utils** (`utils.py`): Backend utility functions

### 3. Agents (`backend/agents/`)

The different specialized agents that perform tasks:

- **OrchestratorAgent** (`orchestrator_agent.py`): Coordinates the overall process
- **CoderAgent** (`coder_agent.py`): Generates and modifies code
- **PlannerAgent** (`planner_agent.py`): Creates execution plans
- **MergeAgent** (`merge_agent.py`): Handles code merging
- **ReviewAgent** (`review_agent.py`): Reviews code changes
- **StormOrchestratorAgent** (`storm_orchestrator_agent.py`): Multi-expert orchestration

### 4. Frontend (`frontend/`)

Svelte-based user interface:

- **App** (`src/App.svelte`): Main application component
- **DiffViewer** (`src/DiffViewer.svelte`): Code diff visualization
- **Main** (`src/main.js`): Application entry point

### 5. CLI Tools (`scripts/`)

Command-line utilities and runners:

- **run_agentic_reason.py**: Main CLI entry point
- **agentic_reason/**: Core reasoning modules
- **tools/**: External tool integrations (search, code execution)
- **test_*.py**: Test scripts for different components

## Feature Components

### 1. STORM Components (`agentic_research/collaborative_storm/` & `agentic_research/storm_analysis/`)

Multi-agent collaborative reasoning:

- **Engine** (`engine.py`): Core STORM execution engine
- **Discourse Manager** (`discourse_manager.py`): Manages multi-agent conversations
- **Expert Modules** (`modules/`): Specialized experts for different tasks
- **Turn Policy** (`turn_policy.py`): Controls agent turn-taking

### 2. GraphRAG / Mind Map (`nano-graphrag/`)

Graph-based knowledge storage and retrieval:

- **GraphRAG** (`graphrag.py`): Core graph-based RAG implementation
- **Vector Storage**: Storage backends for embeddings
- **Entity Relationships**: Knowledge graph structure

## Integration Components

### 1. Model Control Protocol (MCP)

Unified interface for different LLM providers:

- **MCP Tool** (`scripts/tools/mcp_tool.py`): Provider selection and API handling
- **Remote LLM** (`scripts/utils/remote_llm.py`): Remote model management

### 2. Ollama Integration

Local LLM inference:

- **Ollama Client** (`scripts/tools/ollama_client.py`): Interface to local Ollama server

### 3. Search Integration

Web search capabilities:

- **Bing Search** (`scripts/tools/bing_search.py`): Bing search API integration
- **Duck Search** (`scripts/tools/duck_search.py`): DuckDuckGo search integration

## Data Flow Overview

1. User provides a query via CLI or WebSocket
2. OrchestratorAgent processes the request
3. Search tools gather relevant information
4. PlannerAgent creates an execution plan
5. CoderAgent generates or modifies code
6. Results are returned to the user via CLI or WebSocket

## Extension Points

When adding new features, consider these extension points:

1. Add new expert agents in `agentic_research/collaborative_storm/modules/`
2. Add new tools in `scripts/tools/`
3. Extend the API in `backend/server.py`
4. Add new UI components in `frontend/src/`

## Dependency Structure

```
User Interface
   ↓
Backend Server
   ↓
Agent Orchestration
   ↓     ↙     ↘
  LLM   Search   Code
   ↓
Language Models (OpenAI/Gemini/Ollama)
```

For more detailed implementation information, see the PROJECT_STATUS.md and IMPLEMENTATION_PREREQUISITES.md documents.