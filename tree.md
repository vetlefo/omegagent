.
├── AGENTIC_REASONING_INTEGRATION.md
├── CLAUDE.md
├── CODEBASE_IMPROVEMENT_ROADMAP.md
├── CODEBASE_IMPROVEMENT_SUMMARY.md
├── CONTINUOUS_ORCHESTRATION.md
├── DATACLASS_MIGRATION_GUIDE.md
├── GEMINI_FEEDBACK_ASSESSMENT.md
├── GEMINI_INTEGRATION.md
├── IMPLEMENTATION_PREREQUISITES.md
├── INTEGRATION_GUIDE.md
├── LICENSE
├── Miniconda3-latest-MacOSX-x86_64.sh
├── ORCHESTRATION_FIXES.md
├── PROJECT_BREAKDOWN.md
├── PROJECT_STATUS.md
├── PROMPT_LIBRARY_DESIGN.md
├── README 2.md
├── README.md
├── agentic_research
│   ├── __init__.py
│   ├── encoder.py
│   ├── interface.py
│   ├── lm.py
│   ├── logging_wrapper.py
│   ├── rm.py
│   └── utils.py
├── backend
│   ├── __init__.py
│   ├── agents
│   │   ├── __init__.py
│   │   ├── coder_agent.py
│   │   ├── merge_agent.py
│   │   ├── models.py
│   │   ├── orchestrator_agent.py
│   │   ├── planner_agent.py
│   │   ├── review_agent.py
│   │   └── utils.py
│   ├── communication.py
│   ├── main.py
│   ├── models
│   │   └── shared.py
│   ├── repo_map.py
│   ├── server.py
│   └── utils.py
├── docs
│   ├── 01_Project_Overview
│   │   └── file_tree_map.md
│   ├── 02_Phase1_Backend_Integration
│   │   └── setup_progress.md
│   ├── Integration-guide
│   │   └── summary.md
│   ├── coder_agent_integration.md
│   ├── graphrag_compatibility_solutions.md
│   ├── intelligentcontextretrieval.md
│   ├── master_merge_plan.md
│   └── websocket_visualization.md
├── environment.yml
├── frontend
│   ├── README.md
│   ├── assets
│   │   ├── index-BOKcLGz6.css
│   │   └── index-CL5YnCuQ.js
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   │   └── vite.svg
│   ├── src
│   │   ├── App.svelte
│   │   ├── app.css
│   │   ├── lib
│   │   │   ├── ConfirmationDialog.svelte
│   │   │   ├── DiffViewer.svelte
│   │   │   ├── Header.svelte
│   │   │   ├── LogViewer.svelte
│   │   │   ├── QuestionPrompt.svelte
│   │   │   ├── TokenUsage.svelte
│   │   │   ├── UserInput.svelte
│   │   │   └── stores.js
│   │   └── main.js
│   └── vite-env.d.ts
├── lol
├── requirements.txt
├── scripts
│   ├── __init__.py
│   ├── agentic_ds.py
│   ├── agentic_reason
│   │   ├── __init__.py
│   │   ├── cache.py
│   │   ├── config.py
│   │   ├── data_loader.py
│   │   ├── generation.py
│   │   ├── knowledge_synthesizer.py
│   │   ├── models.py
│   │   ├── prompt_manager.py
│   │   ├── reasoning_validator.py
│   │   ├── search.py
│   │   └── utils.py
│   ├── evaluate.py
│   ├── github_upload.py
│   ├── lcb_runner
│   │   ├── benchmarks
│   │   │   ├── __init__.py
│   │   │   ├── code_execution.py
│   │   │   └── code_generation.py
│   │   ├── evaluation
│   │   │   ├── __init__.py
│   │   │   ├── compute_code_execution_metrics.py
│   │   │   ├── compute_code_generation_metrics.py
│   │   │   ├── compute_scores.py
│   │   │   ├── compute_test_output_prediction_metrics.py
│   │   │   ├── old_results_check.py
│   │   │   ├── pass_k_utils.py
│   │   │   └── testing_util.py
│   │   ├── lm_styles.py
│   │   ├── prompts
│   │   │   ├── __init__.py
│   │   │   ├── code_execution.py
│   │   │   ├── code_generation.py
│   │   │   ├── few_shot_examples
│   │   │   │   └── generation
│   │   │   │       ├── func.json
│   │   │   │       └── stdin.json
│   │   │   ├── self_repair.py
│   │   │   └── test_output_prediction.py
│   │   ├── runner
│   │   │   ├── base_runner.py
│   │   │   ├── claude3_runner.py
│   │   │   ├── claude_runner.py
│   │   │   ├── cohere_runner.py
│   │   │   ├── custom_evaluator.py
│   │   │   ├── deepseek_runner.py
│   │   │   ├── gemini_runner.py
│   │   │   ├── main.py
│   │   │   ├── mistral_runner.py
│   │   │   ├── oai_runner.py
│   │   │   ├── parser.py
│   │   │   ├── scenario_router.py
│   │   │   └── vllm_runner.py
│   │   └── utils
│   │       ├── extraction_utils.py
│   │       ├── math_equivalence.py
│   │       ├── multiprocess.py
│   │       ├── path_utils.py
│   │       ├── scenarios.py
│   │       └── utils.py
│   ├── minimal_discourse_manager.py
│   ├── minimal_lm_configs.py
│   ├── prompts.py
│   ├── quicksum.py
│   ├── test_agentic_reasoning.py
│   ├── test_import.py
│   ├── test_imports_fixed.py
│   ├── test_minimal.py
│   ├── test_qdrant_store.py
│   ├── test_specific_imports.py
│   ├── test_with_