# Project Breakdown: AI Codepilot

This document provides an extensive breakdown of the logic, design, and implementation details of the AI Codepilot project. The project is an AI-driven coding assistant that integrates multiple agents and a responsive Svelte frontend to analyze codebases, plan updates, merge changes, and provide real-time feedback.

---

## 1. Overview

**AI Codepilot** is designed to help developers interactively manage and update their codebases by leveraging several AI-powered agents. It performs tasks such as repository mapping, planning updates, generating and merging code changes, and conducting automated code reviews. The system combines a Python FastAPI backend with a Svelte-based frontend to offer a modern, interactive experience.

---

## 2. Project Structure

The project is organized into two main sections: **Backend** and **Frontend**.

### 2.1 Backend

- **Purpose:** Provides the core logic, AI agent orchestration, file operations, and real-time communication with the frontend.
- **Main Components:**
  - **FastAPI Server (`backend/server.py`):**
    - Sets up HTTP endpoints and WebSocket connections.
    - Serves the Svelte frontend as static files.
    - Handles incoming WebSocket connections and routes messages using the `WebSocketCommunicator`.

  - **Communication (`backend/communication.py`):**
    - Implements `WebSocketCommunicator` to manage asynchronous message routing.
    - Uses internal queues to manage different types of messages (logs, confirmations, questions, diffs, token usage, etc.).

  - **Repository Mapping (`backend/repo_map.py`):**
    - Recursively scans the project directory, respecting `.gitignore` patterns.
    - Parses various file types:
      - **Python Files:** Uses Python's `ast` module to extract function signatures and class definitions.
      - **HTML Files:** Uses BeautifulSoup to extract tag information.
      - **Svelte Files:** Analyzes component imports, `<script>` and `<style>` blocks, and exported props.
      - **Asset Files (JS/CSS):** Generates a stub containing a header comment and sample content.
    - Produces a “repository stub” that summarizes the project structure in a Python-like format.

  - **AI Agents (Located in `backend/agents/`):**
    - **OrchestratorAgent (`orchestrator_agent.py`):**
      - Coordinates the overall process to handle a user’s request.
      - Integrates various tools (planning, code updating, file reading, search) and registers them with its LLM agent.
    - **PlannerAgent (`planner_agent.py`):**
      - Generates a detailed plan (list of tasks) by analyzing the repository stub and the user request.
      - Uses an LLM (via the pydantic_ai library) to produce plain-text plans that are then parsed into structured tasks.
    - **CoderAgent (`coder_agent.py`):**
      - Generates code updates in response to a specified task.
      - Crafts detailed prompts using context (repository stub and user request), and processes responses from LLM models.
      - Groups code changes by filename and passes them to the MergeAgent.
    - **MergeAgent (`merge_agent.py`):**
      - Merges code updates (both replacements and insertions) into the existing file content.
      - Constructs a unified prompt describing the changes and relies on an LLM model to output the final updated code.
    - **ReviewAgent (`review_agent.py`):**
      - Reviews the proposed code changes.
      - Checks for correctness, best practices, potential bugs, and side effects.
      - Returns a review feedback model indicating whether the changes pass or need improvement.
    - **Data Models (`models.py`):**
      - Defines Pydantic models for structured code update information:
        - `CodeChunkUpdate` and `CodeChunkUpdates` for individual and grouped changes.
        - `FullCodeUpdate` and `FullCodeUpdates` for complete file modifications.
        - `ReviewFeedback` for summarizing the outcome of code reviews.
    - **Agent Utilities (`agents/utils.py`):**
      - Contains helper functions such as `send_usage` to relay token usage data from agents to the frontend.

  - **Utility Functions (`backend/utils.py`):**
    - Provides functions for:
      - **Search Indexing:** Utilizes ChromaDB to index code documents and perform search queries.
      - **Text Chunking:** Splits large texts into manageable chunks.
      - **File Content Retrieval:** Reads file contents while ensuring correct handling of relative and absolute paths.
      - **Context Building:** Aggregates repository stubs and file contents to create a comprehensive context for AI agents.

  - **Other Files:**
    - **`main.py`:** Entry point to run the FastAPI server using Uvicorn.
    - **`requirements.txt`:** Lists all Python dependencies required by the project.

---

### 2.2 Frontend

- **Purpose:** Provides an interactive user interface for submitting requests, displaying diffs, logging real-time messages, and handling interactive confirmations.
- **Main Components:**
  - **Svelte Framework:**
    - Utilizes Svelte and Vite to create a reactive and performant web interface.
  - **Entry Points:**
    - **`index.html`:** The main HTML file that loads the Svelte application.
    - **`main.js`:** Bootstraps the Svelte App and mounts it onto the DOM.
  - **Core Svelte Components:**
    - **App.svelte:** Main component that structures the layout into two panels:
      - **Left Panel:** Contains components for user input, diffs (via `DiffViewer`), and token usage display.
      - **Right Panel:** Dedicated to displaying logs and system messages (via `LogViewer`).
    - **UserInput (`UserInput.svelte`):**
      - Provides a form for users to enter their coding requests.
      - Allows configuration options such as enabling code reviews, setting maximum iterations, and specifying the working directory.
    - **DiffViewer (`DiffViewer.svelte`):**
      - Displays unified diffs using the Monaco Editor.
      - Automatically updates when new diffs are received from the backend.
    - **LogViewer (`LogViewer.svelte`):**
      - Renders real-time logs and messages (e.g., status updates, errors).
      - Uses markdown parsing (via marked) to format messages.
    - **TokenUsage (`TokenUsage.svelte`):**
      - Displays real-time token usage statistics.
      - Calculates cost estimates based on token counts and model-specific pricing.
    - **Interactive Components:**
      - **ConfirmationDialog and QuestionPrompt:** Facilitate user interaction for confirming or providing feedback on proposed code updates.
  - **State Management:**
    - **Stores (`stores.js`):**
      - Implements Svelte stores to manage persistent state for form inputs and messages.
      - Persists state in `localStorage` to maintain consistency across sessions.
  - **Configuration Files:**
    - **`package.json`, `vite.config.js`, and `svelte.config.js`:** Define project settings, dependencies, and build configurations for the Svelte application.
    - **`jsconfig.json`:** Provides configuration for JavaScript development with Svelte and Vite.

  - **Additional Assets:**
    - **CSS Files (`app.css`):** Contains styles for both light and dark modes.
    - **Static Assets:** Such as `vite.svg` used in the project.

---

## 3. Interaction Flow

1. **User Request Submission:**
   - The user enters a coding request via the `UserInput` component.
   - Configuration options (e.g., enabling review, max iterations, working directory) are specified.

2. **Backend Orchestration:**
   - The frontend establishes a WebSocket connection to the FastAPI server.
   - The **OrchestratorAgent** receives the request and begins processing:
     - Generates a repository stub using **RepoMap**.
     - Uses **PlannerAgent** to create a task plan.
     - Calls **CoderAgent** to generate code updates.
     - Merges changes using **MergeAgent**.
     - Reviews updates via **ReviewAgent**.
   - Throughout this process, real-time logs, diffs, and token usage data are sent back to the frontend.

3. **User Interaction:**
   - The frontend displays diffs (via `DiffViewer`), logs (via `LogViewer`), and interactive prompts (confirmation or feedback via `ConfirmationDialog` and `QuestionPrompt`).
   - The user can accept, reject, or provide feedback on the proposed changes.
   - Final confirmation triggers file updates on the backend.

4. **Token Usage and Feedback:**
   - Token usage statistics are tracked and displayed in real time using the **TokenUsage** component.
   - This transparency allows users to monitor API consumption and associated costs.

---

## 4. Technologies and Libraries

- **Backend:**
  - **FastAPI & Uvicorn:** For building and running the asynchronous web server.
  - **Pydantic:** For data validation and model definitions.
  - **pydantic_ai:** For interfacing with LLM models.
  - **ChromaDB & tiktoken:** For search indexing and token counting.
  - **BeautifulSoup & ast:** For parsing HTML and Python files.
  - **asyncio:** For managing asynchronous tasks.
  - **backoff:** For retry logic in search indexing.
  
- **Frontend:**
  - **Svelte & Vite:** For building a reactive, high-performance web interface.
  - **Monaco Editor:** For displaying code diffs.
  - **Tailwind CSS:** For rapid UI styling.
  - **Marked:** For markdown parsing in logs and interactive prompts.

---

## 5. Summary of Implementation Strategies

- **Modular Multi-Agent Architecture:**  
  Each agent (planner, coder, merge, review) is designed as a separate module that focuses on a specific aspect of the code update process. The orchestrator coordinates their interactions, ensuring that each step is executed sequentially and that feedback loops (e.g., code reviews) are managed properly.

- **Asynchronous Communication:**  
  The backend leverages asyncio and WebSockets to provide real-time interaction with the frontend. This allows for dynamic updates (logs, diffs, confirmations) during long-running tasks.

- **Robust File Handling and Repository Mapping:**  
  The system recursively scans the project directory, respects `.gitignore` patterns, and parses multiple file types. This mapping facilitates context-aware updates and ensures that changes are applied only where necessary.

- **Interactive Frontend:**  
  The Svelte-based frontend provides an intuitive interface for users to submit requests and monitor progress. Real-time diffs, logs, and token usage insights enhance transparency and user control during code modifications.

---

## 6. Conclusion

The AI Codepilot project represents a sophisticated integration of AI-driven code analysis and update capabilities with an interactive frontend. By breaking down the project into clearly defined modules and leveraging modern asynchronous programming techniques, the system delivers a robust solution for managing and automating codebase updates.