# Agentic-Reasoning Testing Guide

This guide outlines the testing procedures for verifying the functionality of the Agentic-Reasoning integration with AI Codepilot. It provides step-by-step instructions for testing each component and ensuring that the integration is working correctly.

## Prerequisites

Before running the tests, ensure that you have:

1. Set up the development environment with all required dependencies
2. Configured the necessary environment variables in `.env`
3. Obtained API keys for OpenAI, Bing Search, and Jina AI (if using)
4. Installed Ollama locally (if testing local model support)

## 1. Testing the Backend Server

### 1.1 Basic Server Functionality

```bash
# Start the backend server
python backend/main.py
```

Verify that:
- The server starts without errors
- The server is accessible at http://localhost:8000
- The API documentation is available at http://localhost:8000/docs

### 1.2 WebSocket Communication

Use a WebSocket client (like Postman or a simple HTML page with WebSocket code) to connect to `ws://localhost:8000/ws` and send a test message:

```json
{
  "content": "List all Python files in the project",
  "config": {
    "review": true,
    "max_iterations": 1,
    "root_directory": ".",
    "use_storm": false
  }
}
```

Verify that:
- The WebSocket connection is established
- The server responds with appropriate messages
- The orchestration process completes successfully

## 2. Testing Agentic Reasoning CLI

### 2.1 Basic CLI Functionality

```bash
# Run with help flag to verify command-line options
python scripts/run_agentic_reason.py --help

# Run with a simple query
python scripts/run_agentic_reason.py --remote_model "gpt-4o"
```

When prompted, enter a simple query like "What is the capital of France?" and verify that:
- The CLI runs without errors
- The model generates a reasonable response
- The response is displayed correctly

### 2.2 Search Functionality

```bash
# Run with search capabilities
python scripts/run_agentic_reason.py \
  --remote_model "gpt-4o" \
  --bing_subscription_key "your-bing-key" \
  --use_jina True \
  --jina_api_key "your-jina-key"
```

When prompted, enter a query that requires search like "What are the latest developments in quantum computing?" and verify that:
- The search query is generated correctly
- The search results are retrieved and processed
- The final response incorporates information from the search results

### 2.3 Code Execution

```bash
# Run with code execution capabilities
python scripts/run_agentic_reason.py --remote_model "gpt-4o"
```

When prompted, enter a query that requires code execution like "Write a Python function to check if a number is prime and test it with 17 and 20" and verify that:
- The code query is generated correctly
- The code is executed successfully
- The execution results are incorporated into the response

### 2.4 Mind Map Functionality

```bash
# Run with mind map capabilities
python scripts/run_agentic_reason.py \
  --remote_model "gpt-4o" \
  --mind_map True \
  --mind_map_path "./mind_map"
```

When prompted, enter a series of related queries like:
1. "What is machine learning?"
2. "Explain neural networks"
3. "How does backpropagation work?"

Verify that:
- The mind map is created and updated correctly
- Subsequent queries benefit from the knowledge in the mind map
- The responses show continuity and context awareness

## 3. Testing Integration Components

### 3.1 Testing Encoder Integration

To test the Encoder integration, ensure that `USE_AGENTIC_ENCODER=true` is set in your `.env` file, then:

```bash
# Start the backend server
python backend/main.py
```

Connect to the WebSocket and send a message that requires semantic search:

```json
{
  "content": "Find all code related to token usage tracking",
  "config": {
    "review": true,
    "max_iterations": 1,
    "root_directory": ".",
    "use_storm": false
  }
}
```

Verify that:
- The logs show that the Agentic Encoder is being used
- The search results are more semantically relevant
- The response includes semantically related code snippets

### 3.2 Testing CollaborativeStorm Integration

To test the CollaborativeStorm integration, ensure that `USE_STORM=true` is set in your `.env` file, then:

```bash
# Start the backend server
python backend/main.py
```

Connect to the WebSocket and send a message with the `use_storm` flag enabled:

```json
{
  "content": "Refactor the code in scripts/tools/run_search.py to improve error handling",
  "config": {
    "review": true,
    "max_iterations": 1,
    "root_directory": ".",
    "use_storm": true
  }
}
```

Verify that:
- The logs show that the StormOrchestratorAgent is being used
- The response includes insights from multiple expert perspectives
- The code changes reflect a more comprehensive analysis

### 3.3 Testing Semantic Repository Mapping

To test the semantic repository mapping, ensure that `USE_SEMANTIC_ANALYSIS=true` is set in your `.env` file, then:

```bash
# Generate a repository map with semantic analysis
python -c "from backend.repo_map import RepoMap; rm = RepoMap('.', use_semantic_analysis=True); rm.build_map(); print(rm.to_python_stub(include_semantic_relationships=True))"
```

Verify that:
- The output includes a "Semantic Relationships" section
- The relationships identified are meaningful and relevant
- The similarity scores are reasonable

### 3.4 Testing Ollama Integration

To test the Ollama integration, ensure that Ollama is installed and running, and `USE_OLLAMA=true` is set in your `.env` file, then:

```bash
# Run with Ollama as the model provider
python scripts/run_agentic_reason.py --use_ollama True
```

When prompted, enter a simple query and verify that:
- The logs show that Ollama is being used
- The model generates a reasonable response
- The response is displayed correctly

### 3.5 Testing Model Control Protocol (MCP)

To test the MCP integration, ensure that `USE_MCP=true` is set in your `.env` file along with the appropriate provider configurations, then:

```bash
# Create a test script to use the MCP tool
cat > test_mcp.py << 'EOF'
from scripts.tools.mcp_tool import MCPTool

# Initialize the MCP tool
mcp = MCPTool()

# Test generation
result = mcp.chat("What is the capital of France?")
print(f"Response: {result.content if hasattr(result, 'content') else result}")

# Test fallback by forcing an error in the primary provider
try:
    # This will cause an error in most providers
    result = mcp.chat("" * 10000)  # Empty string repeated many times
    print(f"Response: {result.content if hasattr(result, 'content') else result}")
except Exception as e:
    print(f"Expected error: {e}")
EOF

# Run the test script
python test_mcp.py
```

Verify that:
- The MCP tool initializes correctly
- The primary provider generates a response
- The fallback mechanism works when the primary provider fails

## 4. End-to-End Testing

### 4.1 Full Integration Test

This test verifies that all components work together correctly:

```bash
# Start the backend server
python backend/main.py
```

In another terminal, create a simple HTML file to test the WebSocket connection:

```bash
cat > test_websocket.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Test</title>
</head>
<body>
    <h1>WebSocket Test</h1>
    <div>
        <button id="connect">Connect</button>
        <button id="send">Send Request</button>
        <button id="disconnect">Disconnect</button>
    </div>
    <div>
        <h2>Messages:</h2>
        <pre id="messages" style="height: 400px; overflow-y: scroll; border: 1px solid #ccc; padding: 10px;"></pre>
    </div>

    <script>
        let socket;
        const messagesElement = document.getElementById('messages');
        
        function appendMessage(message) {
            messagesElement.textContent += message + '\n';
            messagesElement.scrollTop = messagesElement.scrollHeight;
        }
        
        document.getElementById('connect').addEventListener('click', () => {
            socket = new WebSocket('ws://localhost:8000/ws');
            
            socket.onopen = () => {
                appendMessage('Connected to WebSocket');
            };
            
            socket.onmessage = (event) => {
                const data = JSON.parse(event.data);
                appendMessage(`Received: ${JSON.stringify(data, null, 2)}`);
            };
            
            socket.onclose = () => {
                appendMessage('Disconnected from WebSocket');
            };
            
            socket.onerror = (error) => {
                appendMessage(`Error: ${error}`);
            };
        });
        
        document.getElementById('send').addEventListener('click', () => {
            if (socket && socket.readyState === WebSocket.OPEN) {
                const message = {
                    content: "Analyze the code in scripts/tools/run_search.py and suggest improvements",
                    config: {
                        review: true,
                        max_iterations: 1,
                        root_directory: ".",
                        use_storm: true,
                        include_semantic_relationships: true,
                        use_mcp: true,
                        use_ollama: false
                    }
                };
                
                socket.send(JSON.stringify(message));
                appendMessage(`Sent: ${JSON.stringify(message, null, 2)}`);
            } else {
                appendMessage('WebSocket is not connected');
            }
        });
        
        document.getElementById('disconnect').addEventListener('click', () => {
            if (socket) {
                socket.close();
                socket = null;
            }
        });
    </script>
</body>
</html>
EOF

# Open the HTML file in a browser
open test_websocket.html  # On macOS
# xdg-open test_websocket.html  # On Linux
# start test_websocket.html  # On Windows
```

Use the HTML interface to:
1. Connect to the WebSocket
2. Send the test request
3. Observe the messages received

Verify that:
- The connection is established successfully
- The request is processed correctly
- The response includes logs, token usage, and code updates
- The orchestration completes successfully

### 4.2 Deep Research Test

This test verifies the deep research capabilities:

```bash
# Run with deep research capabilities
python scripts/run_agentic_reason.py \
  --remote_model "gpt-4o" \
  --bing_subscription_key "your-bing-key" \
  --use_jina True \
  --jina_api_key "your-jina-key" \
  --deep_research True
```

When prompted, enter a complex research query like "Explain the current state of quantum computing and its potential applications" and verify that:
- The deep research process is initiated
- Multiple search queries are generated and executed
- The final response is comprehensive and well-structured

## 5. Troubleshooting

If you encounter issues during testing, try the following:

### 5.1 Environment Variables

Verify that all required environment variables are set correctly in `.env`:

```bash
cat .env
```

### 5.2 Dependencies

Verify that all required dependencies are installed:

```bash
pip list | grep -E 'fastapi|uvicorn|chromadb|langchain|sentence-transformers|beautifulsoup4|dspy'
```

### 5.3 API Keys

Verify that your API keys are valid by making a simple API call:

```bash
# Test OpenAI API key
curl -s -X POST https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 5
  }' | jq
```

### 5.4 Logs

Check the logs for error messages:

```bash
# Run with verbose logging
python scripts/run_agentic_reason.py --remote_model "gpt-4o" --verbose
```

### 5.5 Ollama

If using Ollama, verify that it's running and has the required models:

```bash
# Check Ollama status
curl -s http://localhost:11434/api/tags | jq
```

## Conclusion

