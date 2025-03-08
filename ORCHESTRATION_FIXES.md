# Agentic-Reasoning Orchestration Fixes

## Current Issues

After analyzing the WebSocket orchestration system, I've identified these key problems:

1. **State Management**: Each new WebSocket connection creates a new repository map and starts from scratch, losing previous context.

2. **Search Context**: The `search_tool` doesn't persist state between connections, causing file lookup failures when the user reconnects.

3. **User Experience**: Users lose their entire interaction context when a WebSocket connection is refreshed or reestablished.

4. **Resource Utilization**: Repeatedly rebuilding the repository map is expensive and unnecessary.

## Proposed Solutions

### 1. Session-Based State Management

Implement session management to preserve state between WebSocket connections:

```python
# Store active sessions
active_sessions = {}

# In websocket_endpoint():
session_id = config.get("session_id", None)
if not session_id:
    # Generate a new session ID
    import uuid
    session_id = str(uuid.uuid4())
else:
    logger.info(f"Using existing session ID: {session_id}")

# Reuse existing repo_map from a session
if session_id in active_sessions:
    session_data = active_sessions[session_id]
    repo_stub = session_data.get("repo_stub")
    search_context = session_data.get("search_context", {})
else:
    # Build new repo map and create session
    ...
    active_sessions[session_id] = {
        "repo_stub": repo_stub,
        "search_context": search_context,
        "last_active": asyncio.get_event_loop().time()
    }
```

### 2. Persistent Search Context

Modify the `search_tool` to store and reuse search context:

```python
async def search_tool(ctx: RunContext[str], search_terms: str) -> List[Dict[str, str]]:
    """Searches the codebase with persistent context"""
    # Check search context first
    for term, results in self.search_context.items():
        if search_terms.lower() in term.lower():
            await self.comm.send("log", f"[Tool Call: search] using cached results for: {search_terms}")
            return results
    
    # Perform the search if not in context
    try:
        snippets = await asyncio.to_thread(get_relevant_snippets, search_terms, self.root_directory)
        # Cache the results for future use
        self.search_context[search_terms] = snippets
        return snippets
    except Exception as e:
        await self.comm.send("error", f"Search tool failed: {str(e)}")
        return []
```

### 3. Session Cleanup

Implement automatic cleanup of inactive sessions:

```python
async def cleanup_inactive_sessions():
    """Periodically clean up inactive sessions."""
    while True:
        try:
            current_time = asyncio.get_event_loop().time()
            timeout = 3600  # 1 hour timeout
            
            # Find and remove inactive sessions
            expired_sessions = []
            for session_id, data in active_sessions.items():
                if current_time - data["last_active"] > timeout:
                    expired_sessions.append(session_id)
            
            for session_id in expired_sessions:
                logger.info(f"Removing inactive session {session_id}")
                del active_sessions[session_id]
                
        except Exception as e:
            logger.error(f"Error in session cleanup: {e}")
            
        # Check every 10 minutes
        await asyncio.sleep(600)

# Start session cleanup task
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(cleanup_inactive_sessions())
```

### 4. Client-Side Session Management

The frontend should:
1. Store the session ID in local storage
2. Send it with each new WebSocket connection
3. Handle reconnection logic to resume existing sessions

```javascript
// Example frontend code
let sessionId = localStorage.getItem('sessionId');

function connect() {
  const ws = new WebSocket('ws://localhost:8000/ws');
  
  ws.onopen = () => {
    // Send initial message with session ID if available
    ws.send(JSON.stringify({
      type: 'default',
      content: userPrompt,
      config: {
        session_id: sessionId,
        // other config...
      }
    }));
  };
  
  ws.onmessage = (event) => {
    const message = JSON.parse(event.data);
    if (message.type === 'session') {
      // Store new session ID if provided
      sessionId = message.content.session_id;
      localStorage.setItem('sessionId', sessionId);
    }
    // Handle other message types...
  };
}
```

## Implementation Strategy

1. Update `server.py` to implement session management
2. Modify `OrchestratorAgent` to initialize with and use search context
3. Add session management to the frontend code
4. Add cleanup mechanism to prevent memory leaks

These changes will create a more reliable and user-friendly orchestration system that maintains state between connections and provides a seamless experience even when connections are interrupted.