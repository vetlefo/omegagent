# WebSocket Visualization Integration

## Overview
This document explains the updates to `server.py` and `DiffViewer.svelte` for streaming `DiscourseManager` actions in real-time via WebSocket.

## Transformations

### 1. WebSocket Endpoint in server.py
- **Change**: Added `/ws/discourse` WebSocket endpoint.
- **Why**: Enables real-time streaming of `DiscourseManager` actions to the frontend, enhancing transparency.
- **How**: Used FastAPI’s WebSocket support to poll and send actions every second.

### 2. Refactoring server.py
- **Change**: Separated WebSocket logic into a dedicated endpoint.
- **Why**: Keeps API endpoints modular and focused, improving maintainability.
- **How**: Moved streaming logic out of main routes, using asyncio for non-blocking updates.

### 3. DiffViewer.svelte Update
- **Change**: Added WebSocket subscription to display actions.
- **Why**: Provides a live view of agent actions, aiding debugging and user interaction.
- **How**: Used Svelte’s `onMount` to connect to the WebSocket and update a reactive `actions` array.

## Benefits
- **Real-Time Feedback**: Users see agent actions as they happen.
- **Modularity**: WebSocket logic is isolated, making it easy to extend or modify.
- **User Experience**: Clean, responsive UI with styled action list.

## Preserved Behavior
- Existing API endpoints (e.g., `/generate_code`) remain unchanged; only visualization is added.