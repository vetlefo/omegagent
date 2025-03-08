Agentic-Reasoning
├─ LICENSE
├─ PROJECT_BREAKDOWN.md
├─ README 2.md
├─ README.md
├─ Search Results.ini
├─ agentic_research
│  ├─ __init__.py
│  ├─ collaborative_storm
│  │  ├─ __init__.py
│  │  ├─ engine.py
│  │  └─ modules
│  │     ├─ __init__.py
│  │     ├─ article_generation.py
│  │     ├─ callback.py
│  │     ├─ co_storm_agents.py
│  │     ├─ collaborative_storm_utils.py
│  │     ├─ costorm_expert_utterance_generator.py
│  │     ├─ expert_generation.py
│  │     ├─ grounded_question_answering.py
│  │     ├─ grounded_question_generation.py
│  │     ├─ information_insertion_module.py
│  │     ├─ knowledge_base_summary.py
│  │     ├─ simulate_user.py
│  │     └─ warmstart_hierarchical_chat.py
│  ├─ dataclass.py
│  ├─ encoder.py
│  ├─ interface.py
│  ├─ lm.py
│  ├─ logging_wrapper.py
│  ├─ rm.py
│  ├─ storm_analysis
│  │  ├─ __init__.py
│  │  ├─ engine.py
│  │  └─ modules
│  │     ├─ __init__.py
│  │     ├─ article_generation.py
│  │     ├─ article_polish.py
│  │     ├─ callback.py
│  │     ├─ knowledge_curation.py
│  │     ├─ outline_generation.py
│  │     ├─ persona_generator.py
│  │     ├─ retriever.py
│  │     └─ storm_dataclass.py
│  └─ utils.py
├─ backend
│  ├─ __init__.py
│  ├─ agents
│  │  ├─ __init__.py
│  │  ├─ coder_agent.py
│  │  ├─ merge_agent.py
│  │  ├─ models.py
│  │  ├─ orchestrator_agent.py
│  │  ├─ planner_agent.py
│  │  ├─ review_agent.py
│  │  └─ utils.py
│  ├─ communication.py
│  ├─ main.py
│  ├─ models
│  │  └─ shared.py
│  ├─ repo_map.py
│  ├─ server.py
│  └─ utils.py
├─ deepresearch.md
├─ environment.yml
├─ frontend
│  ├─ README.md
│  ├─ index.html
│  ├─ jsconfig.json
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  └─ vite.svg
│  ├─ src
│  │  ├─ App.svelte
│  │  ├─ app.css
│  │  ├─ main.js
│  │  └─ vite-env.d.ts
│  ├─ svelte.config.js
│  └─ vite.config.js
├─ integration_guardrails.md
├─ lol
├─ requirements.txt
├─ scripts
│  ├─ __init__.py
│  ├─ agentic_ds.py
│  ├─ agentic_reason
│  │  ├─ __init__.py
│  │  ├─ cache.py
│  │  ├─ config.py
│  │  ├─ data_loader.py
│  │  ├─ generation.py
│  │  ├─ models.py
│  │  ├─ prompt_manager.py
│  │  ├─ search.py
│  │  └─ utils.py
│  ├─ evaluate.py
│  ├─ github_upload.py
│  ├─ lcb_runner
│  │  ├─ benchmarks
│  │  │  ├─ __init__.py
│  │  │  ├─ code_execution.py
│  │  │  └─ code_generation.py
│  │  ├─ evaluation
│  │  │  ├─ __init__.py
│  │  │  ├─ compute_code_execution_metrics.py
│  │  │  ├─ compute_code_generation_metrics.py
│  │  │  ├─ compute_scores.py
│  │  │  ├─ old_results_check.py
│  │  │  ├─ pass_k_utils.py
│  │  │  └─ utils_execute.py
│  │  ├─ lm_styles.py
│  │  ├─ prompts
│  │  │  ├─ __init__.py
│  │  │  ├─ code_execution.py
│  │  │  ├─ code_generation.py
│  │  │  ├─ few_shot_examples
│  │  │  │  └─ generation
│  │  │  │     ├─ func.json
│  │  │  │     └─ stdin.json
│  │  │  └─ self_repair.py
│  │  ├─ pyext
│  │  │  ├─ pyext-0.7
│  │  │  │  ├─ PKG-INFO
│  │  │  │  ├─ README.rst
│  │  │  │  ├─ pyext.py
│  │  │  │  ├─ setup.cfg
│  │  │  │  └─ setup.py
│  │  │  └─ pyext-0.7.tar.gz
│  │  ├─ runner
│  │  │  ├─ base_runner.py
│  │  │  ├─ claude3_runner.py
│  │  │  ├─ claude_runner.py
│  │  │  ├─ cohere_runner.py
│  │  │  ├─ custom_evaluator.py
│  │  │  ├─ deepseek_runner.py
│  │  │  ├─ gemini_runner.py
│  │  │  ├─ main.py
│  │  │  ├─ mistral_runner.py
│  │  │  ├─ oai_runner.py
│  │  │  ├─ parser.py
│  │  │  ├─ runner_utils.py
│  │  │  ├─ scenario_router.py
│  │  │  └─ vllm_runner.py
│  │  └─ utils
│  │     ├─ extraction_utils.py
│  │     ├─ multiprocess.py
│  │     ├─ path_utils.py
│  │     └─ scenarios.py
│  ├─ prompts.py
│  ├─ run_agentic_reason.py
│  ├─ tools
│  │  ├─ __init__.py
│  │  ├─ bing_search.py
│  │  ├─ creat_graph.py
│  │  ├─ duck_search.py
│  │  ├─ run_code.py
│  │  ├─ run_search.py
│  │  └─ temp.py
│  ├─ utils
│  │  ├─ math_equivalence.py
│  │  └─ remote_llm.py
│  └─ yolo.md
├─ setup.py
└─ temp.py

```