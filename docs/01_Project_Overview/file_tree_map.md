# File Tree Map: Files Under Control (Agentic Reasoning Integration)

This tree map represents the files currently "under control" as part of the agentic reasoning integration plan into the Agentic-Reasoning project, as of February 19, 2025. It includes files I’ve modified, created, or directly referenced to establish a solid foundation.
Agentic-Reasoning
├─ docs
│  ├─ 01_Project_Overview
│  │  └─ file_tree_map.md                # [Created] This file, documenting the tree map of controlled files.
│  └─ 02_Phase1_Backend_Integration
│     └─ setup_guide_agentic_reasoning.md # [Created] Setup guide for agentic reasoning with DiscourseManager.
├─ integration_guardrails.md             # [Modified] Updated to focus on agentic reasoning and CollaborativeStorm.
├─ scripts
│  └─ test_agentic_reasoning.py          # [Proposed/Created] Test script referenced in setup guide for running DiscourseManager.
├─ tests
│  └─ test_discourse_manager.py          # [Created] Unit tests for DiscourseManager initialization and turn policy.
├─ agentic_research
│  └─ collaborative_storm
│     ├─ discourse_manager.py            # [Referenced] Core component for agentic reasoning integration.
│     ├─ lm_configs.py                   # [Referenced] Language model configurations used in setup.
│     ├─ runner_args.py                  # [Referenced] Arguments for configuring DiscourseManager.
│     └─ modules
│        └─ callback.py                  # [Referenced] Callback handler used in tests and setup.
├─ agentic_research
│  ├─ logging_wrapper.py                 # [Referenced] Logging utility for DiscourseManager.
│  ├─ rm.py                              # [Referenced] BingSearch module (mocked in tests/setup).
│  ├─ encoder.py                         # [Referenced] Encoder for semantic processing in DiscourseManager.
│  └─ dataclass.py                       # [Referenced] ConversationTurn data structure used in tests/setup.
└─ setup.py                              # [Referenced] Dependency management for the project.
## Legend
- **[Created]**: Newly created files as part of this integration effort.
- **[Modified]**: Existing files updated to reflect the current state.
- **[Proposed/Created]**: Suggested in documentation but not explicitly created in a prior <wonder> block; assumed under control.
- **[Referenced]**: Existing files critical to the setup/tests but not modified.

## Notes
- The tree focuses on files directly involved in the foundational agentic reasoning setup (Phase 1).
- Other project files (e.g., `backend/`, `frontend/`) exist but are not yet "under control" as they’re not modified or tested in this milestone.
- The `scripts/test_agentic_reasoning.py` is included as "proposed/created" since it was detailed in the setup guide; consider formalizing its creation in a future step.

This tree map provides a clear snapshot of the current controlled file set, ensuring traceability and alignment with the integration plan.