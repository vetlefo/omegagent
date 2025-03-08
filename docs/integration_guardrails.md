## Known Limitations

### Geographic Entity Parsing
The current entity extraction has basic location handling but may struggle with:
- Combined city/state names like "Bellevue, Washington"
- Country/region relationships
- Alternative location formats

We're working to improve geographic context understanding in future releases.
# Integration Guard Rails: Agentic Reasoning & AI Codepilot

This document outlines the integration path and guardrails for merging **Agentic Reasoning** (specifically its agentic reasoning capabilities via `CollaborativeStorm`) with **AI Codepilot**, enhancing the coding assistant with advanced reasoning. As of February 19, 2025, the focus is on establishing a solid foundation for agentic reasoning.

---

## Current Integration Focus

The current phase emphasizes **agentic reasoning**, leveraging the `CollaborativeStorm` module (located in `agentic_research/collaborative_storm/`) to enable multi-agent discourse and reasoning. We aim to integrate this into AI Codepilot’s backend and stop at a foundational milestone—ensuring basic functionality works before expanding further.

### Key Integration Areas

1. **Backend Integration**
   - Integrate `DiscourseManager` from `agentic_research/collaborative_storm/discourse_manager.py` into AI Codepilot’s `OrchestratorAgent`.
   - Use `CollaborativeStormLMConfigs` to configure language models for reasoning tasks.
   - Enhance repository mapping in `repo_map.py` with `Encoder` for context-aware reasoning.

2. **Foundational Milestone**
   - Set up a minimal agentic conversation loop using `DiscourseManager`.
   - Test with a simple scenario (e.g., simulated user asking a coding question).
   - Document setup and verify functionality with unit tests.

---

## Guard Railing Summary

### 1. Project Goals and Scope
- [x] **Define clear goals**: Enable agentic reasoning for code-related conversations.
- [x] **Determine scope**: Focus on `DiscourseManager` and basic agent interactions.
- [ ] **Establish success metrics**: Successful execution of a 3-turn conversation with correct agent responses.

### 2. Modular Design and Architecture
- [x] **Maintain modularity**: Keep `CollaborativeStorm` components independent.
- [x] **Define clear APIs**: Use existing interfaces in `interface.py` for agent interactions.
- [ ] **Backend architecture**: Plan integration into `server.py` and `orchestrator_agent.py`.

### 3. Step-by-Step Integration Plan

#### Phase 1: Backend Core Integration (Current Focus)
- [x] **Integrate `DiscourseManager`:**
  - [x] Import into `orchestrator_agent.py` (to be implemented).
  - [ ] Test initialization with mock LM configs.
- [ ] **Configure LMs:**
  - [ ] Use `CollaborativeStormLMConfigs` in `server.py` or a new config module.
- [ ] **Setup Guide & Tests:**
  - [ ] Create `setup_guide_agentic_reasoning.md` (see below).
  - [ ] Add unit tests in `tests/test_discourse_manager.py`.

#### Phase 2: Enhanced Reasoning (Future)
- Enhance `CoderAgent` with reasoning from `CoStormExpert`.
- Integrate `Encoder` for semantic context in `repo_map.py`.

### 4. Development and Testing
- [x] **Set up environment**: Unified in `setup.py`.
- [ ] **Unit tests**: Create tests for `DiscourseManager` initialization and turn policy.
- [ ] **Integration tests**: Verify agent orchestration.

### 5. Dependency Management
- [x] **Review dependencies**: `litellm`, `dspy`, `numpy` already in `setup.py`.
- [ ] **Add new dependencies**: If local RAG agents (e.g., `qwen2.5`) are used, update `setup.py`.

### 6. Stopping Point
- Stop after Phase 1: Verify a basic agentic conversation works with `DiscourseManager`.
- Ensure tests pass and document the setup.

---

## Conclusion

This updated guardrail focuses on integrating agentic reasoning via `CollaborativeStorm` into AI Codepilot, stopping at a foundational milestone to ensure stability. The next steps will expand reasoning capabilities once the base is solid.