# Agentic-Reasoning Integration with AI Codepilot

This document outlines the integration of the Agentic-Reasoning framework with the AI Codepilot system, enhancing its code analysis and generation capabilities through advanced semantic understanding and collaborative multi-expert reasoning.

## Overview

The integration adds three major capabilities to AI Codepilot:

1. **Advanced Semantic Code Understanding**
   - Uses the `Encoder` class from Agentic-Reasoning for better embeddings
   - Analyzes semantic relationships between code components
   - Enhances search and context building with deeper code understanding

2. **CollaborativeStorm Multi-Expert Reasoning**
   - Enables multiple specialized expert agents to analyze problems collaboratively
   - Leverages the STORM framework for synthesizing coherent analyses
   - Provides comprehensive insights by considering multiple perspectives

3. **Enhanced Repository Mapping**
   - Uses semantic code analysis to identify related components
   - Improves context-building with relationships data
   - Creates a more detailed understanding of codebase structure
   
4. **Local Model Support via Ollama**
   - Connects to locally running Ollama server for LLM inference
   - Reduces API costs by using local models
   - Provides offline capabilities for development

5. **Model Control Protocol (MCP)**
   - Implements unified interface for different LLM providers
   - Offers automatic fallback between models
   - Provides performance tracking and monitoring

## Key Components

### 1. Enhanced Search

- `AgenticEncoderFunction` class in `backend/utils.py` - Uses Agentic-Reasoning's Encoder for superior embeddings
- Enhanced `get_relevant_snippets` function - Provides better search results with semantic understanding
- Controlled via `USE_AGENTIC_ENCODER` environment variable

### 2. Semantic Repository Mapping

- Enhanced `RepoMap` class in `backend/repo_map.py` - Added semantic analysis capabilities 
- New `analyze_semantic_relationships` method - Identifies related code components
- Controlled via `USE_SEMANTIC_ANALYSIS` environment variable

### 3. StormOrchestratorAgent

- New `StormOrchestratorAgent` class in `backend/agents/storm_orchestrator_agent.py`
- Integrates with CollaborativeStorm's multi-expert architecture
- Provides enhanced reasoning through multiple specialist perspectives
- Controlled via `USE_STORM` environment variable

### 4. Server Integration

- Updated server in `backend/server.py` to support both orchestrator types
- Configuration parameters added to enable/disable STORM features
- Enriched context building with semantic relationship information

### 5. Ollama Integration

- `OllamaClient` class in `scripts/tools/ollama_client.py` - Provides access to local LLM models
- Connects to Ollama server for inference with locally installed models
- Tracks token usage and performance metrics
- Controlled via `USE_OLLAMA` environment variable

### 6. Model Control Protocol

- `MCPTool` class in `scripts/tools/mcp_tool.py` - Unified interface for different LLM backends
- Provides fallback capabilities between models (e.g., from OpenAI to Ollama)
- Includes performance tracking and monitoring
- Controlled via `USE_MCP` environment variable  

### 7. Frontend Example

- Example Svelte component in `frontend/src/lib/UserInputEnhanced.svelte.example`
- Shows how to add UI controls for all the new features
- Demonstrates passing configuration to the backend

## Usage

### Environment Variables

Set these environment variables to enable features:

```bash
# Enable advanced embeddings for search
export USE_AGENTIC_ENCODER=true

# Enable semantic code analysis
export USE_SEMANTIC_ANALYSIS=true

# Enable CollaborativeStorm reasoning
export USE_STORM=true

# Set encoder type (openai or azure)
export ENCODER_API_TYPE=openai

# Set specific embedding models (optional)
export OPENAI_EMBEDDING_MODEL=text-embedding-3-small
export AZURE_EMBEDDING_MODEL=text-embedding-3-small

# Enable local model support with Ollama
export USE_OLLAMA=true
export OLLAMA_MODEL=llama3

# Enable Model Control Protocol with fallback
export USE_MCP=true
export MCP_PRIMARY_PROVIDER=openai
export MCP_PRIMARY_MODEL=gpt-4o
export MCP_FALLBACK_PROVIDER=ollama
export MCP_FALLBACK_MODEL=llama3
```

### API Configuration

When making requests to the websocket endpoint, include these configuration options:

```javascript
// Example initial message to websocket
{
  "content": "User request here",
  "config": {
    "review": true,
    "max_iterations": 1,
    "root_directory": ".",
    "use_storm": true,
    "include_semantic_relationships": true,
    "use_mcp": true,
    "use_ollama": false
  }
}
```

### Repository Mapping

Generate a repository map with semantic analysis:

```bash
python backend/repo_map.py --root /path/to/repo --semantic --output repo_map.txt
```

## Architecture

The integration follows these design principles:

1. **Graceful Degradation** - If Agentic-Reasoning components are unavailable, the system falls back to standard behavior
2. **Feature Flagging** - All new capabilities can be enabled/disabled independently
3. **Minimal Core Changes** - We've extended functionality without modifying existing core logic
4. **Consistent APIs** - New functionality maintains compatibility with existing interfaces

## Future Enhancements

Potential next steps for further integration:

1. Enhanced frontend visualization of the knowledge base (mind map)
2. Integration of additional STORM modules (e.g., article generation)
3. Further improvements to the semantic analysis with fine-tuned embeddings
4. Support for additional LLM providers beyond OpenAI and Azure

## Notes for Maintainers

When updating this integration, consider these guidelines:

1. Always maintain backward compatibility with the standard orchestrator
2. Keep feature flags for all advanced features
3. Ensure proper error handling for graceful degradation
4. Update CLAUDE.md and this document with any API or usage changes
5. Run tests to ensure integration hasn't broken existing functionality