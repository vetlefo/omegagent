
# Agentic Reasoning: Reasoning LLM with Agentic Tools
An open-source framework for deep research and beyond. The core idea is to integrate agentic tools into LLM reasoning.

Warning: Still in development. Theoretically runnable, but undergoing rapid updates.

## Install
install from environment.yml, e.g.
```
conda env create -f environment.yml
```

## Run
export your remote LLM API key in environment if you are using remote LLM, e.g.
```
export OPENAI_API_KEY="your openai api key"
```

export your you.com api key in environment if you are using deep research
```
export YDC_API_KEY="your you.com api key"
```

prepare JINA and BING API key if needed

run command:
```
python scripts/run_agentic_reason.py \
--use_jina True \
--jina_api_key "your jina api key" \
--bing_subscription_key "your bing api key"\ 
--remote_model "your remote model name, e.g. gpt-4o" \
--mind_map True \ (optional)
--deep_research True \ (optional, if you want to use deep research)
```

## TODO LIST
- [ ] auto research
- [ ] clean agentic reasoning


## Thanks
Code copied a lot from ...

## Ref
~~~
@misc{wu2025agenticreasoningreasoningllms,
      title={Agentic Reasoning: Reasoning LLMs with Tools for the Deep Research}, 
      author={Junde Wu and Jiayuan Zhu and Yuyuan Liu},
      year={2025},
      eprint={2502.04644},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2502.04644}, 
}
~~~

=======

```
Agentic-Reasoning
├─ .DS_Store
├─ LICENSE
├─ agentic_research
│  ├─ __init__.py
│  ├─ collaborative_storm
│  │  ├─ __init__.py
│  │  ├─ discourse_manager.py
│  │  ├─ lm_configs.py
│  │  ├─ modules
│  │  │  ├─ __init__.py
│  │  │  ├─ article_generation.py
│  │  │  ├─ callback.py
│  │  │  ├─ co_storm_agents.py
│  │  │  ├─ collaborative_storm_utils.py
│  │  │  ├─ costorm_expert_utterance_generator.py
│  │  │  ├─ expert_generation.py
│  │  │  ├─ grounded_question_answering.py
│  │  │  ├─ grounded_question_generation.py
│  │  │  ├─ information_insertion_module.py
│  │  │  ├─ knowledge_base_summary.py
│  │  │  ├─ simulate_user.py
│  │  │  └─ warmstart_hierarchical_chat.py
│  │  ├─ runner.py
│  │  ├─ runner_args.py
│  │  └─ turn_policy.py
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
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ repo_map.py
│  ├─ server.py
│  └─ utils.py
├─ docs
│  ├─ 00_Original_reference-docs
│  │  ├─ old-ar-README.md
│  │  ├─ old-cp-README.md
│  │  └─ old_cp_breakdown.md
│  ├─ 01_Project_Overview
│  │  └─ file_tree_map.md
│  ├─ 02_Phase1_Backend_Integration
│  │  ├─ setup_guide_agentic_reasoning.md
│  │  └─ setup_progress.md
│  ├─ Integration-guide
│  │  ├─ .editorconfig
│  │  ├─ Integration-study-Merging-AI-Codepilot,.md
│  │  ├─ README.md
│  │  ├─ cloud-deployment-strategy
│  │  │  └─ security-networking.md
│  │  ├─ deepresearch.md
│  │  ├─ index.md
│  │  └─ summary.md
│  ├─ coder_agent_integration.md
│  ├─ documentation-rules.md
│  ├─ graphrag_compatibility_solutions.md
│  ├─ integration-status.md
│  ├─ integration_guardrails.md
│  ├─ intelligentcontextretrieval.md
│  └─ websocket_visualization.md
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
│  │  ├─ DiffViewer.svelte
│  │  ├─ app.css
│  │  ├─ main.js
│  │  └─ vite-env.d.ts
│  ├─ svelte.config.js
│  └─ vite.config.js
├─ memgraph-platform
│  └─ docker-compose.yml
├─ nano-graphrag
│  ├─ .coveragerc
│  ├─ LICENSE
│  ├─ MANIFEST.in
│  ├─ docs
│  │  ├─ CONTRIBUTING.md
│  │  ├─ FAQ.md
│  │  ├─ ROADMAP.md
│  │  ├─ benchmark-dspy-entity-extraction.md
│  │  ├─ benchmark-en.md
│  │  ├─ benchmark-zh.md
│  │  └─ use_neo4j_for_graphrag.md
│  ├─ examples
│  │  ├─ benchmarks
│  │  │  ├─ dspy_entity.py
│  │  │  ├─ eval_naive_graphrag_on_multi_hop.ipynb
│  │  │  ├─ hnsw_vs_nano_vector_storage.py
│  │  │  └─ md5_vs_xxhash.py
│  │  ├─ finetune_entity_relationship_dspy.ipynb
│  │  ├─ generate_entity_relationship_dspy.ipynb
│  │  ├─ graphml_visualize.py
│  │  ├─ no_openai_key_at_all.py
│  │  ├─ using_amazon_bedrock.py
│  │  ├─ using_custom_chunking_method.py
│  │  ├─ using_deepseek_api_as_llm+glm_api_as_embedding.py
│  │  ├─ using_deepseek_as_llm.py
│  │  ├─ using_dspy_entity_extraction.py
│  │  ├─ using_faiss_as_vextorDB.py
│  │  ├─ using_hnsw_as_vectorDB.py
│  │  ├─ using_llm_api_as_llm+ollama_embedding.py
│  │  ├─ using_local_embedding_model.py
│  │  ├─ using_milvus_as_vectorDB.py
│  │  ├─ using_ollama_as_llm.py
│  │  └─ using_ollama_as_llm_and_embedding.py
│  ├─ nano_graphrag
│  │  ├─ __init__.py
│  │  ├─ _llm.py
│  │  ├─ _op.py
│  │  ├─ _splitter.py
│  │  ├─ _storage
│  │  │  ├─ __init__.py
│  │  │  ├─ gdb_neo4j.py
│  │  │  ├─ gdb_networkx.py
│  │  │  ├─ kv_json.py
│  │  │  ├─ vdb_hnswlib.py
│  │  │  └─ vdb_nanovectordb.py
│  │  ├─ _utils.py
│  │  ├─ base.py
│  │  ├─ entity_extraction
│  │  │  ├─ __init__.py
│  │  │  ├─ extract.py
│  │  │  ├─ metric.py
│  │  │  └─ module.py
│  │  ├─ graphrag.py
│  │  └─ prompt.py
│  ├─ nano_graphrag_cache_2025-02-19-23:51:49
│  ├─ nano_graphrag_cache_2025-02-20-00:02:28
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:03:47
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:03:54
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:05:36
│  ├─ nano_graphrag_cache_2025-02-20-00:06:14
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:06:43
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:06:47
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:09:02
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:09:30
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:09:44
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:11:06
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:11:33
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:11:36
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:14:52
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:15:30
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:15:34
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:19:29
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:19:51
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:20:20
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:21:45
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:22:30
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:22:42
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ readme.md
│  ├─ requirements-dev.txt
│  ├─ requirements.txt
│  └─ setup.py
├─ requirements.txt
├─ scripts
│  ├─ __init__.py
│  ├─ agentic_ds.py
│  ├─ agentic_reason
│  │  ├─ __init__.py
│  │  ├─ cache.py
│  │  ├─ config.py
│  │  ├─ context_manager.py
│  │  ├─ data_loader.py
│  │  ├─ generation.py
│  │  ├─ knowledge_synthesizer.py
│  │  ├─ models.py
│  │  ├─ prompt_manager.py
│  │  ├─ reasoning_validator.py
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
│  ├─ minimal_discourse_manager.py
│  ├─ minimal_lm_configs.py
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
│  └─ utils
│     ├─ math_equivalence.py
│     └─ remote_llm.py
├─ setup.py
├─ temp.py
├─ tokenizers-main
│  ├─ .DS_Store
│  ├─ CITATION.cff
│  ├─ LICENSE
│  ├─ README.md
│  ├─ RELEASE.md
│  ├─ bindings
│  │  ├─ node
│  │  │  ├─ .cargo
│  │  │  │  └─ config.toml
│  │  │  ├─ .editorconfig
│  │  │  ├─ .eslintrc.yml
│  │  │  ├─ .prettierignore
│  │  │  ├─ .taplo.toml
│  │  │  ├─ .yarn
│  │  │  │  └─ releases
│  │  │  │     └─ yarn-3.5.1.cjs
│  │  │  ├─ .yarnrc.yml
│  │  │  ├─ Cargo.toml
│  │  │  ├─ LICENSE
│  │  │  ├─ Makefile
│  │  │  ├─ README.md
│  │  │  ├─ build.rs
│  │  │  ├─ examples
│  │  │  │  └─ documentation
│  │  │  ├─ index.d.ts
│  │  │  ├─ index.js
│  │  │  ├─ jest.config.js
│  │  │  ├─ npm
│  │  │  │  ├─ android-arm-eabi
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ android-arm64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ darwin-arm64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ darwin-x64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ freebsd-x64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-arm-gnueabihf
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-arm64-gnu
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-arm64-musl
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-x64-gnu
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-x64-musl
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ win32-arm64-msvc
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ win32-ia32-msvc
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  └─ win32-x64-msvc
│  │  │  │     ├─ README.md
│  │  │  │     └─ package.json
│  │  │  ├─ package.json
│  │  │  ├─ rustfmt.toml
│  │  │  ├─ src
│  │  │  │  ├─ arc_rwlock_serde.rs
│  │  │  │  ├─ decoders.rs
│  │  │  │  ├─ encoding.rs
│  │  │  │  ├─ lib.rs
│  │  │  │  ├─ models.rs
│  │  │  │  ├─ normalizers.rs
│  │  │  │  ├─ pre_tokenizers.rs
│  │  │  │  ├─ processors.rs
│  │  │  │  ├─ tasks
│  │  │  │  │  ├─ mod.rs
│  │  │  │  │  ├─ models.rs
│  │  │  │  │  └─ tokenizer.rs
│  │  │  │  ├─ tokenizer.rs
│  │  │  │  ├─ trainers.rs
│  │  │  │  └─ utils.rs
│  │  │  ├─ tsconfig.json
│  │  │  ├─ types.ts
│  │  │  └─ yarn.lock
│  │  └─ python
│  │     ├─ .cargo
│  │     │  └─ config.toml
│  │     ├─ CHANGELOG.md
│  │     ├─ Cargo.toml
│  │     ├─ MANIFEST.in
│  │     ├─ Makefile
│  │     ├─ README.md
│  │     ├─ benches
│  │     ├─ examples
│  │     │  ├─ custom_components.py
│  │     │  ├─ example.py
│  │     │  ├─ train_bert_wordpiece.py
│  │     │  ├─ train_bytelevel_bpe.py
│  │     │  ├─ train_with_datasets.py
│  │     │  └─ using_the_visualizer.ipynb
│  │     ├─ py_src
│  │     │  └─ tokenizers
│  │     │     ├─ __init__.py
│  │     │     ├─ __init__.pyi
│  │     │     ├─ decoders
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ implementations
│  │     │     │  ├─ __init__.py
│  │     │     │  ├─ base_tokenizer.py
│  │     │     │  ├─ bert_wordpiece.py
│  │     │     │  ├─ byte_level_bpe.py
│  │     │     │  ├─ char_level_bpe.py
│  │     │     │  ├─ sentencepiece_bpe.py
│  │     │     │  └─ sentencepiece_unigram.py
│  │     │     ├─ models
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ normalizers
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ pre_tokenizers
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ processors
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ tools
│  │     │     │  ├─ __init__.py
│  │     │     │  ├─ visualizer-styles.css
│  │     │     │  └─ visualizer.py
│  │     │     └─ trainers
│  │     │        ├─ __init__.py
│  │     │        └─ __init__.pyi
│  │     ├─ pyproject.toml
│  │     ├─ rust-toolchain
│  │     ├─ scripts
│  │     │  ├─ convert.py
│  │     │  ├─ sentencepiece_extractor.py
│  │     │  └─ spm_parity_check.py
│  │     ├─ setup.cfg
│  │     ├─ src
│  │     │  ├─ decoders.rs
│  │     │  ├─ encoding.rs
│  │     │  ├─ error.rs
│  │     │  ├─ lib.rs
│  │     │  ├─ models.rs
│  │     │  ├─ normalizers.rs
│  │     │  ├─ pre_tokenizers.rs
│  │     │  ├─ processors.rs
│  │     │  ├─ token.rs
│  │     │  ├─ tokenizer.rs
│  │     │  ├─ trainers.rs
│  │     │  └─ utils
│  │     │     ├─ iterators.rs
│  │     │     ├─ mod.rs
│  │     │     ├─ normalization.rs
│  │     │     ├─ pretokenization.rs
│  │     │     ├─ regex.rs
│  │     │     └─ serde_pyo3.rs
│  │     └─ stub.py
│  ├─ docs
│  │  ├─ Makefile
│  │  ├─ README.md
│  │  ├─ source
│  │  │  ├─ _ext
│  │  │  │  ├─ entities.py
│  │  │  │  ├─ rust_doc.py
│  │  │  │  └─ toctree_tags.py
│  │  │  ├─ _static
│  │  │  │  ├─ css
│  │  │  │  │  ├─ Calibre-Light.ttf
│  │  │  │  │  ├─ Calibre-Medium.otf
│  │  │  │  │  ├─ Calibre-Regular.otf
│  │  │  │  │  ├─ Calibre-Thin.otf
│  │  │  │  │  ├─ code-snippets.css
│  │  │  │  │  └─ huggingface.css
│  │  │  │  └─ js
│  │  │  │     └─ custom.js
│  │  │  ├─ api
│  │  │  │  ├─ node.inc
│  │  │  │  ├─ python.inc
│  │  │  │  ├─ reference.rst
│  │  │  │  └─ rust.inc
│  │  │  ├─ components.rst
│  │  │  ├─ conf.py
│  │  │  ├─ entities.inc
│  │  │  ├─ index.rst
│  │  │  ├─ installation
│  │  │  │  ├─ main.rst
│  │  │  │  ├─ node.inc
│  │  │  │  ├─ python.inc
│  │  │  │  └─ rust.inc
│  │  │  ├─ pipeline.rst
│  │  │  ├─ quicktour.rst
│  │  │  └─ tutorials
│  │  │     └─ python
│  │  │        └─ training_from_memory.rst
│  │  └─ source-doc-builder
│  │     ├─ _toctree.yml
│  │     ├─ api
│  │     │  ├─ added-tokens.mdx
│  │     │  ├─ decoders.mdx
│  │     │  ├─ encode-inputs.mdx
│  │     │  ├─ encoding.mdx
│  │     │  ├─ input-sequences.mdx
│  │     │  ├─ models.mdx
│  │     │  ├─ normalizers.mdx
│  │     │  ├─ post-processors.mdx
│  │     │  ├─ pre-tokenizers.mdx
│  │     │  ├─ tokenizer.mdx
│  │     │  ├─ trainers.mdx
│  │     │  └─ visualizer.mdx
│  │     ├─ components.mdx
│  │     ├─ index.mdx
│  │     ├─ installation.mdx
│  │     ├─ pipeline.mdx
│  │     ├─ quicktour.mdx
│  │     └─ training_from_memory.mdx
│  └─ tokenizers
│     ├─ CHANGELOG.md
│     ├─ Cargo.toml
│     ├─ LICENSE
│     ├─ Makefile
│     ├─ README.md
│     ├─ README.tpl
│     ├─ benches
│     │  ├─ bert_benchmark.rs
│     │  ├─ bpe_benchmark.rs
│     │  ├─ common
│     │  │  └─ mod.rs
│     │  ├─ layout_benchmark.rs
│     │  ├─ llama3.rs
│     │  └─ unigram_benchmark.rs
│     ├─ examples
│     │  ├─ encode_batch.rs
│     │  ├─ serialization.rs
│     │  └─ unstable_wasm
│     │     ├─ Cargo.toml
│     │     ├─ README.md
│     │     ├─ src
│     │     │  ├─ lib.rs
│     │     │  └─ utils.rs
│     │     └─ www
│     │        ├─ .bin
│     │        │  └─ create-wasm-app.js
│     │        ├─ .travis.yml
│     │        ├─ LICENSE-APACHE
│     │        ├─ LICENSE-MIT
│     │        ├─ README.md
│     │        ├─ bootstrap.js
│     │        ├─ index.html
│     │        ├─ index.js
│     │        ├─ package-lock.json
│     │        ├─ package.json
│     │        └─ webpack.config.js
│     ├─ rust-toolchain
│     └─ src
│        ├─ decoders
│        │  ├─ bpe.rs
│        │  ├─ byte_fallback.rs
│        │  ├─ ctc.rs
│        │  ├─ fuse.rs
│        │  ├─ mod.rs
│        │  ├─ sequence.rs
│        │  ├─ strip.rs
│        │  └─ wordpiece.rs
│        ├─ lib.rs
│        ├─ models
│        │  ├─ bpe
│        │  │  ├─ mod.rs
│        │  │  ├─ model.rs
│        │  │  ├─ serialization.rs
│        │  │  ├─ trainer.rs
│        │  │  └─ word.rs
│        │  ├─ mod.rs
│        │  ├─ unigram
│        │  │  ├─ lattice.rs
│        │  │  ├─ mod.rs
│        │  │  ├─ model.rs
│        │  │  ├─ serialization.rs
│        │  │  ├─ trainer.rs
│        │  │  └─ trie.rs
│        │  ├─ wordlevel
│        │  │  ├─ mod.rs
│        │  │  ├─ serialization.rs
│        │  │  └─ trainer.rs
│        │  └─ wordpiece
│        │     ├─ mod.rs
│        │     ├─ serialization.rs
│        │     └─ trainer.rs
│        ├─ normalizers
│        │  ├─ bert.rs
│        │  ├─ byte_level.rs
│        │  ├─ mod.rs
│        │  ├─ precompiled.rs
│        │  ├─ prepend.rs
│        │  ├─ replace.rs
│        │  ├─ strip.rs
│        │  ├─ unicode.rs
│        │  └─ utils.rs
│        ├─ pre_tokenizers
│        │  ├─ bert.rs
│        │  ├─ byte_level.rs
│        │  ├─ delimiter.rs
│        │  ├─ digits.rs
│        │  ├─ metaspace.rs
│        │  ├─ mod.rs
│        │  ├─ punctuation.rs
│        │  ├─ sequence.rs
│        │  ├─ split.rs
│        │  ├─ unicode_scripts
│        │  │  ├─ mod.rs
│        │  │  ├─ pre_tokenizer.rs
│        │  │  └─ scripts.rs
│        │  └─ whitespace.rs
│        ├─ processors
│        │  ├─ bert.rs
│        │  ├─ mod.rs
│        │  ├─ roberta.rs
│        │  ├─ sequence.rs
│        │  └─ template.rs
│        ├─ tokenizer
│        │  ├─ added_vocabulary.rs
│        │  ├─ encoding.rs
│        │  ├─ mod.rs
│        │  ├─ normalizer.rs
│        │  ├─ pattern.rs
│        │  ├─ pre_tokenizer.rs
│        │  └─ serialization.rs
│        └─ utils
│           ├─ cache.rs
│           ├─ fancy.rs
│           ├─ from_pretrained.rs
│           ├─ iter.rs
│           ├─ mod.rs
│           ├─ onig.rs
│           ├─ padding.rs
│           ├─ parallelism.rs
│           ├─ progress.rs
│           └─ truncation.rs
├─ tree.md
└─ venv311
   ├─ bin
   │  ├─ Activate.ps1
   │  ├─ activate
   │  ├─ activate.csh
   │  ├─ activate.fish
   │  ├─ alembic
   │  ├─ chroma
   │  ├─ coloredlogs
   │  ├─ datasets-cli
   │  ├─ distro
   │  ├─ dotenv
   │  ├─ email_validator
   │  ├─ esprima
   │  ├─ f2py
   │  ├─ fastapi
   │  ├─ fastavro
   │  ├─ fonttools
   │  ├─ futurize
   │  ├─ get_gprof
   │  ├─ get_objgraph
   │  ├─ griffe
   │  ├─ gunicorn
   │  ├─ httpx
   │  ├─ huggingface-cli
   │  ├─ humanfriendly
   │  ├─ isympy
   │  ├─ jp.py
   │  ├─ json_repair
   │  ├─ jsonschema
   │  ├─ litellm
   │  ├─ mako-render
   │  ├─ markdown-it
   │  ├─ normalizer
   │  ├─ numba
   │  ├─ openai
   │  ├─ opentelemetry-bootstrap
   │  ├─ opentelemetry-instrument
   │  ├─ optuna
   │  ├─ pasteurize
   │  ├─ pip
   │  ├─ pip3
   │  ├─ pip3.11
   │  ├─ pyftmerge
   │  ├─ pyftsubset
   │  ├─ pygmentize
   │  ├─ pyproject-build
   │  ├─ pyrsa-decrypt
   │  ├─ pyrsa-encrypt
   │  ├─ pyrsa-keygen
   │  ├─ pyrsa-priv2pub
   │  ├─ pyrsa-sign
   │  ├─ pyrsa-verify
   │  ├─ python
   │  ├─ python3
   │  ├─ python3.11
   │  ├─ rq
   │  ├─ rqinfo
   │  ├─ rqworker
   │  ├─ tqdm
   │  ├─ ttx
   │  ├─ typer
   │  ├─ undill
   │  ├─ uvicorn
   │  ├─ watchfiles
   │  ├─ wheel
   │  └─ wsdump
   ├─ include
   │  └─ python3.11
   ├─ pyvenv.cfg
   └─ share
      └─ man
         └─ man1
            ├─ isympy.1
            └─ ttx.1

```
```
Agentic-Reasoning
├─ .DS_Store
├─ .trunk
│  ├─ actions
│  │  ├─ trunk-cache-prune
│  │  │  ├─ 2025-03-04-18-40-31.503.yaml
│  │  │  ├─ 2025-03-04-19-40-31.843.yaml
│  │  │  ├─ 2025-03-05-19-07-40.522.yaml
│  │  │  ├─ 2025-03-06-19-02-26.794.yaml
│  │  │  └─ 2025-03-07-19-09-00.866.yaml
│  │  ├─ trunk-share-with-everyone
│  │  │  ├─ 2025-03-04-18-40-31.509.yaml
│  │  │  ├─ 2025-03-04-19-40-31.340.yaml
│  │  │  ├─ 2025-03-05-19-07-40.470.yaml
│  │  │  ├─ 2025-03-06-19-02-27.202.yaml
│  │  │  └─ 2025-03-07-19-09-00.900.yaml
│  │  ├─ trunk-single-player-auto-on-upgrade
│  │  │  ├─ 2025-03-04-18-46-09.495.yaml
│  │  │  ├─ 2025-03-04-19-41-10.57.yaml
│  │  │  ├─ 2025-03-05-19-08-21.0.yaml
│  │  │  ├─ 2025-03-06-19-03-38.785.yaml
│  │  │  └─ 2025-03-07-19-09-41.262.yaml
│  │  ├─ trunk-single-player-auto-upgrade
│  │  │  ├─ 2025-03-04-19-46-15.87.yaml
│  │  │  ├─ 2025-03-05-19-46-14.515.yaml
│  │  │  ├─ 2025-03-06-20-20-29.525.yaml
│  │  │  └─ 2025-03-07-19-46-14.497.yaml
│  │  ├─ trunk-upgrade-available
│  │  │  ├─ 2025-03-04-18-46-23.263.yaml
│  │  │  ├─ 2025-03-04-19-40-46.247.yaml
│  │  │  ├─ 2025-03-04-19-40-58.515.yaml
│  │  │  ├─ 2025-03-04-19-41-09.760.yaml
│  │  │  ├─ 2025-03-04-19-41-21.265.yaml
│  │  │  ├─ 2025-03-04-19-41-26.256.yaml
│  │  │  ├─ 2025-03-04-19-46-22.599.yaml
│  │  │  ├─ 2025-03-04-19-46-28.847.yaml
│  │  │  ├─ 2025-03-05-01-08-14.501.yaml
│  │  │  ├─ 2025-03-05-01-08-14.553.yaml
│  │  │  ├─ 2025-03-05-06-46-58.260.yaml
│  │  │  ├─ 2025-03-05-06-46-58.261.yaml
│  │  │  ├─ 2025-03-05-08-02-02.804.yaml
│  │  │  ├─ 2025-03-05-08-46-58.763.yaml
│  │  │  ├─ 2025-03-05-11-04-36.607.yaml
│  │  │  ├─ 2025-03-05-11-04-38.780.yaml
│  │  │  ├─ 2025-03-05-12-22-00.661.yaml
│  │  │  ├─ 2025-03-05-13-04-38.236.yaml
│  │  │  ├─ 2025-03-05-14-29-48.199.yaml
│  │  │  ├─ 2025-03-05-15-19-14.192.yaml
│  │  │  ├─ 2025-03-05-19-07-54.730.yaml
│  │  │  ├─ 2025-03-05-19-07-55.264.yaml
│  │  │  ├─ 2025-03-05-19-08-06.175.yaml
│  │  │  ├─ 2025-03-05-19-08-20.529.yaml
│  │  │  ├─ 2025-03-05-19-08-29.522.yaml
│  │  │  ├─ 2025-03-05-19-08-34.266.yaml
│  │  │  ├─ 2025-03-05-19-46-28.511.yaml
│  │  │  ├─ 2025-03-05-20-22-36.795.yaml
│  │  │  ├─ 2025-03-05-21-07-54.442.yaml
│  │  │  ├─ 2025-03-05-22-24-11.766.yaml
│  │  │  ├─ 2025-03-05-23-07-52.142.yaml
│  │  │  ├─ 2025-03-06-01-56-14.913.yaml
│  │  │  ├─ 2025-03-06-01-56-14.970.yaml
│  │  │  ├─ 2025-03-06-02-56-12.58.yaml
│  │  │  ├─ 2025-03-06-07-56-48.258.yaml
│  │  │  ├─ 2025-03-06-07-56-48.260.yaml
│  │  │  ├─ 2025-03-06-10-28-38.200.yaml
│  │  │  ├─ 2025-03-06-10-28-39.511.yaml
│  │  │  ├─ 2025-03-06-11-42-40.709.yaml
│  │  │  ├─ 2025-03-06-12-28-37.509.yaml
│  │  │  ├─ 2025-03-06-13-28-34.213.yaml
│  │  │  ├─ 2025-03-06-14-28-35.194.yaml
│  │  │  ├─ 2025-03-06-15-29-46.776.yaml
│  │  │  ├─ 2025-03-06-16-51-52.58.yaml
│  │  │  ├─ 2025-03-06-17-28-35.255.yaml
│  │  │  ├─ 2025-03-06-18-28-33.95.yaml
│  │  │  ├─ 2025-03-06-19-02-51.237.yaml
│  │  │  ├─ 2025-03-06-19-03-33.781.yaml
│  │  │  ├─ 2025-03-06-19-03-47.516.yaml
│  │  │  ├─ 2025-03-06-19-04-06.143.yaml
│  │  │  ├─ 2025-03-06-20-20-36.517.yaml
│  │  │  ├─ 2025-03-06-20-20-41.457.yaml
│  │  │  ├─ 2025-03-06-20-30-16.69.yaml
│  │  │  ├─ 2025-03-06-21-28-35.768.yaml
│  │  │  ├─ 2025-03-06-22-46-19.57.yaml
│  │  │  ├─ 2025-03-06-23-28-35.445.yaml
│  │  │  ├─ 2025-03-07-02-56-03.236.yaml
│  │  │  ├─ 2025-03-07-02-56-03.261.yaml
│  │  │  ├─ 2025-03-07-04-52-27.216.yaml
│  │  │  ├─ 2025-03-07-04-56-02.770.yaml
│  │  │  ├─ 2025-03-07-08-14-56.732.yaml
│  │  │  ├─ 2025-03-07-08-14-58.773.yaml
│  │  │  ├─ 2025-03-07-09-35-30.701.yaml
│  │  │  ├─ 2025-03-07-10-17-34.510.yaml
│  │  │  ├─ 2025-03-07-11-33-23.284.yaml
│  │  │  ├─ 2025-03-07-12-53-31.767.yaml
│  │  │  ├─ 2025-03-07-13-14-56.514.yaml
│  │  │  ├─ 2025-03-07-14-14-59.259.yaml
│  │  │  ├─ 2025-03-07-15-14-56.270.yaml
│  │  │  ├─ 2025-03-07-19-09-15.253.yaml
│  │  │  ├─ 2025-03-07-19-09-15.258.yaml
│  │  │  ├─ 2025-03-07-19-09-24.715.yaml
│  │  │  ├─ 2025-03-07-19-09-36.58.yaml
│  │  │  ├─ 2025-03-07-19-09-49.849.yaml
│  │  │  ├─ 2025-03-07-19-09-54.514.yaml
│  │  │  ├─ 2025-03-07-19-46-28.805.yaml
│  │  │  ├─ 2025-03-07-20-18-06.65.yaml
│  │  │  ├─ 2025-03-07-21-17-07.254.yaml
│  │  │  └─ 2025-03-07-22-09-13.58.yaml
│  │  └─ trunk-whoami
│  │     ├─ 2025-03-04-19-46-22.870.yaml
│  │     ├─ 2025-03-05-19-46-20.499.yaml
│  │     ├─ 2025-03-06-20-20-35.468.yaml
│  │     └─ 2025-03-07-19-46-20.593.yaml
│  ├─ configs
│  │  ├─ .isort.cfg
│  │  ├─ .markdownlint.yaml
│  │  ├─ .yamllint.yaml
│  │  └─ ruff.toml
│  ├─ notifications
│  │  ├─ trunk-share-with-everyone.yaml
│  │  ├─ trunk-share-with-everyone.yaml.lock
│  │  └─ trunk-upgrade.yaml.lock
│  ├─ out
│  │  ├─ 01SD0.yaml
│  │  ├─ 0K2VL.yaml
│  │  ├─ 14S7M.yaml
│  │  ├─ 15MS6.yaml
│  │  ├─ 15Q62.yaml
│  │  ├─ 15QY7.yaml
│  │  ├─ 1AB2Z.yaml
│  │  ├─ 1B8WY.yaml
│  │  ├─ 1BP34.yaml
│  │  ├─ 1FDLN.yaml
│  │  ├─ 1H7PR.yaml
│  │  ├─ 1KQ4R.yaml
│  │  ├─ 2AUBW.yaml
│  │  ├─ 2PEQN.yaml
│  │  ├─ 3EL8B.yaml
│  │  ├─ 3LYG3.yaml
│  │  ├─ 3NGWZ.yaml
│  │  ├─ 3TRAX.yaml
│  │  ├─ 3WSQ6.yaml
│  │  ├─ 3ZUS7.yaml
│  │  ├─ 4UB2T.yaml
│  │  ├─ 50HFL.yaml
│  │  ├─ 6656M.yaml
│  │  ├─ 673F3.yaml
│  │  ├─ 67SMA.yaml
│  │  ├─ 6CV8W.yaml
│  │  ├─ 6LGQE.yaml
│  │  ├─ 71JU9.yaml
│  │  ├─ 720YS.yaml
│  │  ├─ 8534G.yaml
│  │  ├─ 85LNt.yaml
│  │  ├─ 8AJ74.yaml
│  │  ├─ 8NGB8.yaml
│  │  ├─ 8phPF.yaml
│  │  ├─ 99N96.yaml
│  │  ├─ 9B2Y7.yaml
│  │  ├─ 9NGGP.yaml
│  │  ├─ B3XFL.yaml
│  │  ├─ B8Z6K.yaml
│  │  ├─ BaMey.yaml
│  │  ├─ C75UT.yaml
│  │  ├─ CGL0E.yaml
│  │  ├─ CJW9S.yaml
│  │  ├─ CLCG4.yaml
│  │  ├─ D7XUT.yaml
│  │  ├─ DKLRV.yaml
│  │  ├─ EGCL5.yaml
│  │  ├─ EOcg1.yaml
│  │  ├─ F3D7W.yaml
│  │  ├─ F43J8.yaml
│  │  ├─ G0MCM.yaml
│  │  ├─ G61PD.yaml
│  │  ├─ GAKL1.yaml
│  │  ├─ GR3PG.yaml
│  │  ├─ GUAFJ.yaml
│  │  ├─ GXGR2.yaml
│  │  ├─ HA6S9.yaml
│  │  ├─ HC96S.yaml
│  │  ├─ HGMMR.yaml
│  │  ├─ HP72V.yaml
│  │  ├─ HP9YC.yaml
│  │  ├─ J2195.yaml
│  │  ├─ JLHUX.yaml
│  │  ├─ JTVK7.yaml
│  │  ├─ JZA6Y.yaml
│  │  ├─ KFX8P.yaml
│  │  ├─ KXGWK.yaml
│  │  ├─ L56Q4.yaml
│  │  ├─ M058Y.yaml
│  │  ├─ ND13J.yaml
│  │  ├─ NLMEU.yaml
│  │  ├─ NuGSi.yaml
│  │  ├─ P0K11.yaml
│  │  ├─ PX510.yaml
│  │  ├─ Q4JK6.yaml
│  │  ├─ Q6CMS.yaml
│  │  ├─ S3B1T.yaml
│  │  ├─ S6VLJ.yaml
│  │  ├─ SPYCM.yaml
│  │  ├─ SXWQV.yaml
│  │  ├─ T0WWD.yaml
│  │  ├─ U1R3H.yaml
│  │  ├─ U698L.yaml
│  │  ├─ U8PU6.yaml
│  │  ├─ V3X73.yaml
│  │  ├─ V9SAU.yaml
│  │  ├─ VFUVN.yaml
│  │  ├─ W9bB8.yaml
│  │  ├─ WKDXX.yaml
│  │  ├─ WP6HQ.yaml
│  │  ├─ X5Y3D.yaml
│  │  ├─ XHMT7.yaml
│  │  ├─ XKBKU.yaml
│  │  ├─ YBD19.yaml
│  │  ├─ Z0A55.yaml
│  │  ├─ Z3C7Y.yaml
│  │  ├─ ZNEH7.yaml
│  │  ├─ fR6ow.yaml
│  │  ├─ kD3vB.yaml
│  │  ├─ rV6Wv.yaml
│  │  └─ wTXCk.yaml
│  ├─ plugins
│  │  └─ trunk
│  │     ├─ .devcontainer.json
│  │     ├─ .editorconfig
│  │     ├─ .trunk
│  │     │  ├─ setup-ci
│  │     │  │  └─ action.yaml
│  │     │  └─ trunk.yaml
│  │     ├─ CONTRIBUTING.md
│  │     ├─ LICENSE
│  │     ├─ README.md
│  │     ├─ actions
│  │     │  ├─ buf
│  │     │  │  ├─ README.md
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ commitizen
│  │     │  │  ├─ README.md
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ commitlint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ commitlint.test.ts
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ git
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ git-blame-ignore-revs
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ update_config.sh
│  │     │  ├─ go-mod-tidy
│  │     │  │  ├─ README.md
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ go-mod-tidy-vendor
│  │     │  │  ├─ README.md
│  │     │  │  ├─ go-mod-tidy-vendor.sh
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ hello-world
│  │     │  │  └─ python
│  │     │  │     ├─ README.md
│  │     │  │     ├─ hello
│  │     │  │     ├─ hello_world.test.ts
│  │     │  │     ├─ plugin.yaml
│  │     │  │     └─ requirements.txt
│  │     │  ├─ npm-check
│  │     │  │  ├─ README.md
│  │     │  │  ├─ npm.png
│  │     │  │  ├─ npm_check.js
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ npm-check-pre-push
│  │     │  │  ├─ npm_check.js
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ poetry
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ poetry.test.ts
│  │     │  │  └─ requirements.txt
│  │     │  ├─ submodules
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ terraform-docs
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform-docs.py
│  │     │  ├─ trunk
│  │     │  │  └─ plugin.yaml
│  │     │  └─ yarn-check
│  │     │     ├─ README.md
│  │     │     ├─ package.json
│  │     │     ├─ plugin.yaml
│  │     │     ├─ yarn.png
│  │     │     └─ yarn_check.js
│  │     ├─ eslint.config.cjs
│  │     ├─ jest.config.json
│  │     ├─ linters
│  │     │  ├─ actionlint
│  │     │  │  ├─ actionlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ansible-lint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ ansible_lint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ autopep8
│  │     │  │  ├─ autopep8.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ bandit
│  │     │  │  ├─ bandit.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ biome
│  │     │  │  ├─ biome.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ black
│  │     │  │  ├─ black.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ brakeman
│  │     │  │  ├─ brakeman.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ buf
│  │     │  │  ├─ buf.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ buildifier
│  │     │  │  ├─ buildifier.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cfnlint
│  │     │  │  ├─ cfnlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ checkov
│  │     │  │  ├─ checkov.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ circleci
│  │     │  │  ├─ circleci.test.ts
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ run.sh
│  │     │  ├─ clang-format
│  │     │  │  ├─ clang_format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clang-tidy
│  │     │  │  ├─ .clang-tidy
│  │     │  │  ├─ clang_tidy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clippy
│  │     │  │  ├─ clippy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cmake-format
│  │     │  │  ├─ cmake-format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ codespell
│  │     │  │  ├─ codespell.test.ts
│  │     │  │  ├─ codespell_to_sarif.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cspell
│  │     │  │  ├─ cspell.test.ts
│  │     │  │  ├─ cspell.yaml
│  │     │  │  ├─ expected_basic_issues.json
│  │     │  │  ├─ expected_dictionary_issues.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cue-fmt
│  │     │  │  ├─ cue_fmt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dart
│  │     │  │  ├─ dart.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ deno
│  │     │  │  ├─ deno.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ detekt
│  │     │  │  ├─ detekt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ djlint
│  │     │  │  ├─ .djlintrc
│  │     │  │  ├─ README.md
│  │     │  │  ├─ djlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dotenv-linter
│  │     │  │  ├─ dotenv_linter.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dotnet-format
│  │     │  │  ├─ dotnet_format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dustilock
│  │     │  │  ├─ dustilock.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ eslint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ eslint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ flake8
│  │     │  │  ├─ .flake8
│  │     │  │  ├─ flake8.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ git-diff-check
│  │     │  │  ├─ git_diff_check.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gitleaks
│  │     │  │  ├─ gitleaks.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gofmt
│  │     │  │  ├─ gofmt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gofumpt
│  │     │  │  ├─ gofumpt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ goimports
│  │     │  │  ├─ goimports.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gokart
│  │     │  │  ├─ analyzers.yml
│  │     │  │  ├─ gokart.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ golangci-lint
│  │     │  │  ├─ golangci_lint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ golines
│  │     │  │  ├─ golines.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ google-java-format
│  │     │  │  ├─ google-java-format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ graphql-schema-linter
│  │     │  │  ├─ graphql_schema_linter.test.ts
│  │     │  │  ├─ parse.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ hadolint
│  │     │  │  ├─ .hadolint.yaml
│  │     │  │  ├─ hadolint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ haml-lint
│  │     │  │  ├─ haml_lint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ isort
│  │     │  │  ├─ .isort.cfg
│  │     │  │  ├─ isort.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ iwyu
│  │     │  │  ├─ iwyu.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ktlint
│  │     │  │  ├─ ktlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ kube-linter
│  │     │  │  ├─ kube_linter.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdown-link-check
│  │     │  │  ├─ markdown-link-check.test.ts
│  │     │  │  ├─ parse.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdown-table-prettify
│  │     │  │  ├─ markdown_table_prettify.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdownlint
│  │     │  │  ├─ .markdownlint.yaml
│  │     │  │  ├─ markdownlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdownlint-cli2
│  │     │  │  ├─ markdownlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ mypy
│  │     │  │  ├─ mypy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ nancy
│  │     │  │  ├─ expected_issues.json
│  │     │  │  ├─ nancy.test.ts
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ run.sh
│  │     │  ├─ nixpkgs-fmt
│  │     │  │  ├─ nixpkgs_fmt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ opa
│  │     │  │  ├─ opa.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ osv-scanner
│  │     │  │  ├─ expected_issues.json
│  │     │  │  ├─ osv_scanner.test.ts
│  │     │  │  ├─ osv_to_sarif.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ oxipng
│  │     │  │  ├─ oxipng.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ perlcritic
│  │     │  │  ├─ .perlcriticrc
│  │     │  │  ├─ perlcritic.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ perltidy
│  │     │  │  ├─ .perltidyrc
│  │     │  │  ├─ perltidy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ php-cs-fixer
│  │     │  │  ├─ php-cs-fixer.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ phpstan
│  │     │  │  ├─ phpstan.test.ts
│  │     │  │  ├─ phpstan_parser.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ plugin.yaml
│  │     │  ├─ pmd
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pmd.test.ts
│  │     │  ├─ pragma-once
│  │     │  │  ├─ README.md
│  │     │  │  ├─ fix.sh
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pragma_once.test.ts
│  │     │  ├─ pre-commit-hooks
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pre_commit_hooks.test.ts
│  │     │  ├─ prettier
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ prettier.test.ts
│  │     │  │  └─ prettier_to_sarif.py
│  │     │  ├─ prisma
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ prisma.test.ts
│  │     │  ├─ psscriptanalyzer
│  │     │  │  ├─ README.md
│  │     │  │  ├─ format.ps1
│  │     │  │  ├─ lint.ps1
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ psscriptanalyzer.test.ts
│  │     │  ├─ pylint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pylint.test.ts
│  │     │  ├─ pyright
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ pyright.test.ts
│  │     │  │  └─ pyright_to_sarif.py
│  │     │  ├─ regal
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ regal.test.ts
│  │     │  ├─ remark-lint
│  │     │  │  ├─ .remarkrc.yaml
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ remark_lint.test.ts
│  │     │  ├─ renovate
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ renovate.test.ts
│  │     │  ├─ rome
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ rome.test.ts
│  │     │  ├─ rubocop
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ rubocop.test.ts
│  │     │  │  └─ rubocop_to_sarif.py
│  │     │  ├─ ruff
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ ruff.test.ts
│  │     │  │  ├─ ruff.toml
│  │     │  │  └─ ruff_to_sarif.py
│  │     │  ├─ rufo
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ rufo.test.ts
│  │     │  ├─ rustfmt
│  │     │  │  ├─ .rustfmt.toml
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ rustfmt.test.ts
│  │     │  ├─ scalafmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ scalafmt.test.ts
│  │     │  ├─ semgrep
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ semgrep.test.ts
│  │     │  ├─ shellcheck
│  │     │  │  ├─ .shellcheckrc
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ shellcheck.test.ts
│  │     │  ├─ shfmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ shfmt.test.ts
│  │     │  ├─ snyk
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ snyk.test.ts
│  │     │  ├─ sort-package-json
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sort_package_json.test.ts
│  │     │  ├─ sourcery
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sourcery.test.ts
│  │     │  ├─ sql-formatter
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sql_formatter.test.ts
│  │     │  ├─ sqlfluff
│  │     │  │  ├─ .sqlfluff
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ sqlfluff.test.ts
│  │     │  │  └─ sqlfluff_to_sarif.py
│  │     │  ├─ sqlfmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sqlfmt.test.ts
│  │     │  ├─ squawk
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ squawk.test.ts
│  │     │  ├─ standardrb
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ standardrb.test.ts
│  │     │  ├─ stringslint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ stringslint.test.ts
│  │     │  ├─ stylelint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ stylelint.test.ts
│  │     │  ├─ stylua
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ stylua.test.ts
│  │     │  │  └─ stylua.toml
│  │     │  ├─ svgo
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ svgo.config.mjs
│  │     │  │  └─ svgo.test.ts
│  │     │  ├─ swiftformat
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ swiftformat.test.ts
│  │     │  ├─ swiftlint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ swiftlint.test.ts
│  │     │  ├─ taplo
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ taplo.test.ts
│  │     │  ├─ terraform
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform.test.ts
│  │     │  ├─ terragrunt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terragrunt.test.ts
│  │     │  ├─ terrascan
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ sarif_to_sarif.py
│  │     │  │  └─ terrascan.test.ts
│  │     │  ├─ tflint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tflint.test.ts
│  │     │  ├─ tfsec
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfsec.test.ts
│  │     │  ├─ tofu
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tofu.test.ts
│  │     │  ├─ trivy
│  │     │  │  ├─ README.md
│  │     │  │  ├─ config_expected_issues.json
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ trivy.test.ts
│  │     │  │  ├─ trivy_config_to_sarif.py
│  │     │  │  ├─ trivy_fs_secret_to_sarif.py
│  │     │  │  ├─ trivy_fs_vuln_to_sarif.py
│  │     │  │  └─ vuln_expected_issues.json
│  │     │  ├─ trufflehog
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ trufflehog.test.ts
│  │     │  │  └─ trufflehog_to_sarif.py
│  │     │  ├─ trunk-toolbox
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ trunk_toolbox.test.ts
│  │     │  ├─ txtpbfmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ txtpbfmt.test.ts
│  │     │  ├─ vale
│  │     │  │  ├─ .vale.ini
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ vale.test.ts
│  │     │  ├─ yamllint
│  │     │  │  ├─ .yamllint.yaml
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ yamllint.test.ts
│  │     │  └─ yapf
│  │     │     ├─ plugin.yaml
│  │     │     └─ yapf.test.ts
│  │     ├─ package-lock.json
│  │     ├─ package.json
│  │     ├─ plugin.yaml
│  │     ├─ repo-tools
│  │     │  ├─ definition-checker
│  │     │  │  └─ check.ts
│  │     │  ├─ linter-test-helper
│  │     │  │  ├─ generate
│  │     │  │  ├─ linter_sample.test.ts
│  │     │  │  ├─ linter_sample_plugin.yaml
│  │     │  │  └─ requirements.txt
│  │     │  └─ tool-test-helper
│  │     │     ├─ generate
│  │     │     ├─ requirements.txt
│  │     │     ├─ tool_sample.test.ts
│  │     │     └─ tool_sample_plugin.yaml
│  │     ├─ runtimes
│  │     │  ├─ README.md
│  │     │  ├─ go
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ java
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ node
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ php
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ python
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ruby
│  │     │  │  └─ plugin.yaml
│  │     │  └─ rust
│  │     │     └─ plugin.yaml
│  │     ├─ security.md
│  │     ├─ tests
│  │     │  ├─ README.md
│  │     │  ├─ driver
│  │     │  │  ├─ action_driver.ts
│  │     │  │  ├─ driver.ts
│  │     │  │  ├─ index.ts
│  │     │  │  ├─ lint_driver.ts
│  │     │  │  └─ tool_driver.ts
│  │     │  ├─ index.ts
│  │     │  ├─ jest_setup.ts
│  │     │  ├─ parse
│  │     │  │  └─ index.ts
│  │     │  ├─ repo_tests
│  │     │  │  ├─ config_check.test.ts
│  │     │  │  ├─ readme_inclusion.test.ts
│  │     │  │  └─ valid_package_download.test.ts
│  │     │  ├─ reporter
│  │     │  │  ├─ index.js
│  │     │  │  └─ reporter.ts
│  │     │  ├─ types
│  │     │  │  └─ index.ts
│  │     │  └─ utils
│  │     │     ├─ index.ts
│  │     │     ├─ landing_state.ts
│  │     │     └─ trunk_config.ts
│  │     ├─ tools
│  │     │  ├─ 1password-cli
│  │     │  │  ├─ 1password_cli.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ act
│  │     │  │  ├─ act.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ action-validator
│  │     │  │  ├─ action_validator.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ adr
│  │     │  │  ├─ adr.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ age
│  │     │  │  ├─ age.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ agebox
│  │     │  │  ├─ agebox.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ air
│  │     │  │  ├─ air.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ alp
│  │     │  │  ├─ alp.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ amazon-ecr-credential-helper
│  │     │  │  ├─ amazon_ecr_credential_helper.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ asciinema
│  │     │  │  ├─ asciinema.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ assh
│  │     │  │  ├─ assh.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ aws-amplify
│  │     │  │  ├─ aws_amplify.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ awscli
│  │     │  │  ├─ awscli.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ bazel
│  │     │  │  ├─ bazel.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ bazel-differ
│  │     │  │  ├─ bazel.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ circleci
│  │     │  │  ├─ circleci.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clangd
│  │     │  │  ├─ clangd.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clangd-indexing-tools
│  │     │  │  ├─ clangd_indexing_tools.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dbt-cli
│  │     │  │  ├─ dbt_cli.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ deno
│  │     │  │  ├─ deno.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ diff-so-fancy
│  │     │  │  ├─ diff_so_fancy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ difft
│  │     │  │  ├─ difft.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ docker-credential-ecr-login
│  │     │  │  ├─ docker-credential-ecr-login.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dotnet
│  │     │  │  ├─ dotnet.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ eksctl
│  │     │  │  ├─ eksctl.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gh
│  │     │  │  ├─ gh.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gk
│  │     │  │  ├─ gk.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ goreleaser
│  │     │  │  ├─ goreleaser.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ grpcui
│  │     │  │  ├─ grpcui.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gt
│  │     │  │  ├─ gt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gulp
│  │     │  │  ├─ gulp.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ helm
│  │     │  │  ├─ helm.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ibazel
│  │     │  │  ├─ ibazel.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ istioctl
│  │     │  │  ├─ istioctl.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ jq
│  │     │  │  ├─ jq.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ kubectl
│  │     │  │  ├─ kubectl.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ minikube
│  │     │  │  ├─ minikube.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ paratest
│  │     │  │  ├─ paratest.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ phpunit
│  │     │  │  ├─ phpunit.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ platformio
│  │     │  │  ├─ platformio.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ pnpm
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pnpm.test.ts
│  │     │  ├─ prisma
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ prisma.test.ts
│  │     │  ├─ pwsh
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pwsh.test.ts
│  │     │  ├─ renovate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ renovate.test.ts
│  │     │  ├─ ripgrep
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ ripgrep.test.ts
│  │     │  ├─ sentry-cli
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sentry_cli.test.ts
│  │     │  ├─ sfdx
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sfdx.test.ts
│  │     │  ├─ sourcery
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sourcery.test.ts
│  │     │  ├─ tailwindcss
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tailwindcss.test.ts
│  │     │  ├─ target-determinator
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ target_determinator.test.ts
│  │     │  ├─ terraform
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform.test.ts
│  │     │  ├─ terraform-docs
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform_docs.test.ts
│  │     │  ├─ terraform-switcher
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform_switcher.test.ts
│  │     │  ├─ terraformer
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraformer.test.ts
│  │     │  ├─ terramate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terramate.test.ts
│  │     │  ├─ tfmigrate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfmigrate.test.ts
│  │     │  ├─ tfnotify
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfnotify.test.ts
│  │     │  ├─ tfupdate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfupdate.test.ts
│  │     │  ├─ tofu
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tofu.test.ts
│  │     │  ├─ tree-sitter
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tree_sitter.test.ts
│  │     │  ├─ ts-node
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ ts_node.test.ts
│  │     │  ├─ tsc
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tsc.test.ts
│  │     │  ├─ webpack
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ webpack.test.ts
│  │     │  ├─ yarn
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ yarn.test.ts
│  │     │  └─ yq
│  │     │     ├─ plugin.yaml
│  │     │     └─ yq.test.ts
│  │     ├─ trunk.ps1
│  │     └─ tsconfig.json
│  ├─ tools
│  │  ├─ bandit
│  │  ├─ black
│  │  ├─ checkov
│  │  ├─ isort
│  │  ├─ markdownlint
│  │  ├─ osv-scanner
│  │  ├─ prettier
│  │  ├─ ruff
│  │  ├─ trufflehog
│  │  ├─ trunk
│  │  └─ yamllint
│  └─ trunk.yaml
├─ LICENSE
├─ README.md
├─ agentic_research
│  ├─ .DS_Store
│  ├─ __init__.py
│  ├─ collaborative_storm
│  │  ├─ .DS_Store
│  │  ├─ __init__.py
│  │  ├─ discourse_manager.py
│  │  ├─ lm_configs.py
│  │  ├─ modules
│  │  │  ├─ __init__.py
│  │  │  ├─ article_generation.py
│  │  │  ├─ callback.py
│  │  │  ├─ co_storm_agents.py
│  │  │  ├─ collaborative_storm_utils.py
│  │  │  ├─ costorm_expert_utterance_generator.py
│  │  │  ├─ expert_generation.py
│  │  │  ├─ grounded_question_answering.py
│  │  │  ├─ grounded_question_generation.py
│  │  │  ├─ information_insertion_module.py
│  │  │  ├─ knowledge_base_summary.py
│  │  │  ├─ simulate_user.py
│  │  │  └─ warmstart_hierarchical_chat.py
│  │  ├─ runner.py
│  │  ├─ runner_args.py
│  │  └─ turn_policy.py
│  ├─ dataclass.py
│  ├─ encoder.py
│  ├─ interface.py
│  ├─ lm.py
│  ├─ logging_wrapper.py
│  ├─ rm.py
│  ├─ storm_analysis
│  │  ├─ .DS_Store
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
│  ├─ test_engine.py
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
│  │  ├─ test_coder_agent.py
│  │  └─ utils.py
│  ├─ communication.py
│  ├─ main.py
│  ├─ models
│  │  └─ shared.py
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ repo_map.py
│  ├─ server.py
│  └─ utils.py
├─ docs
│  ├─ 00_Original_reference-docs
│  │  ├─ old-ar-README.md
│  │  ├─ old-cp-README.md
│  │  └─ old_cp_breakdown.md
│  ├─ 01_Project_Overview
│  │  └─ file_tree_map.md
│  ├─ 02_Phase1_Backend_Integration
│  │  ├─ setup_guide_agentic_reasoning.md
│  │  └─ setup_progress.md
│  ├─ Integration-guide
│  │  ├─ .editorconfig
│  │  ├─ Integration-study-Merging-AI-Codepilot,.md
│  │  ├─ README.md
│  │  ├─ cloud-deployment-strategy
│  │  │  └─ security-networking.md
│  │  ├─ deepresearch.md
│  │  ├─ git-and-doc-strategy.md
│  │  ├─ index.md
│  │  └─ summary.md
│  ├─ coder_agent_integration.md
│  ├─ documentation-rules.md
│  ├─ graphrag_compatibility_solutions.md
│  ├─ integration-status.md
│  ├─ integration_guardrails.md
│  ├─ intelligentcontextretrieval.md
│  └─ websocket_visualization.md
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
│  │  ├─ DiffViewer.svelte
│  │  ├─ app.css
│  │  ├─ main.js
│  │  └─ vite-env.d.ts
│  ├─ svelte.config.js
│  └─ vite.config.js
├─ memgraph-platform
│  └─ docker-compose.yml
├─ nano-graphrag
│  ├─ .coveragerc
│  ├─ LICENSE
│  ├─ MANIFEST.in
│  ├─ docs
│  │  ├─ CONTRIBUTING.md
│  │  ├─ FAQ.md
│  │  ├─ ROADMAP.md
│  │  ├─ benchmark-dspy-entity-extraction.md
│  │  ├─ benchmark-en.md
│  │  ├─ benchmark-zh.md
│  │  └─ use_neo4j_for_graphrag.md
│  ├─ examples
│  │  ├─ benchmarks
│  │  │  ├─ dspy_entity.py
│  │  │  ├─ eval_naive_graphrag_on_multi_hop.ipynb
│  │  │  ├─ hnsw_vs_nano_vector_storage.py
│  │  │  └─ md5_vs_xxhash.py
│  │  ├─ finetune_entity_relationship_dspy.ipynb
│  │  ├─ generate_entity_relationship_dspy.ipynb
│  │  ├─ graphml_visualize.py
│  │  ├─ no_openai_key_at_all.py
│  │  ├─ using_amazon_bedrock.py
│  │  ├─ using_custom_chunking_method.py
│  │  ├─ using_deepseek_api_as_llm+glm_api_as_embedding.py
│  │  ├─ using_deepseek_as_llm.py
│  │  ├─ using_dspy_entity_extraction.py
│  │  ├─ using_faiss_as_vextorDB.py
│  │  ├─ using_hnsw_as_vectorDB.py
│  │  ├─ using_llm_api_as_llm+ollama_embedding.py
│  │  ├─ using_local_embedding_model.py
│  │  ├─ using_milvus_as_vectorDB.py
│  │  ├─ using_ollama_as_llm.py
│  │  └─ using_ollama_as_llm_and_embedding.py
│  ├─ nano_graphrag
│  │  ├─ __init__.py
│  │  ├─ _llm.py
│  │  ├─ _op.py
│  │  ├─ _splitter.py
│  │  ├─ _storage
│  │  │  ├─ __init__.py
│  │  │  ├─ gdb_neo4j.py
│  │  │  ├─ gdb_networkx.py
│  │  │  ├─ kv_json.py
│  │  │  ├─ vdb_hnswlib.py
│  │  │  └─ vdb_nanovectordb.py
│  │  ├─ _utils.py
│  │  ├─ base.py
│  │  ├─ entity_extraction
│  │  │  ├─ __init__.py
│  │  │  ├─ extract.py
│  │  │  ├─ metric.py
│  │  │  └─ module.py
│  │  ├─ graphrag.py
│  │  └─ prompt.py
│  ├─ nano_graphrag_cache_2025-02-19-23:51:49
│  ├─ nano_graphrag_cache_2025-02-20-00:02:28
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:03:47
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:03:54
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:05:36
│  ├─ nano_graphrag_cache_2025-02-20-00:06:14
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:06:43
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:06:47
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:09:02
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:09:30
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:09:44
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:11:06
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:11:33
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:11:36
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:14:52
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:15:30
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:15:34
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:19:29
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:19:51
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:20:20
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:21:45
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:22:30
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:22:42
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-03:18:45
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-03:19:07
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-03:19:10
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-04:06:36
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-04:06:54
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-04:06:59
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ readme.md
│  ├─ requirements-dev.txt
│  ├─ requirements.txt
│  ├─ setup.py
│  └─ tests
│     ├─ __init__.py
│     ├─ entity_extraction
│     │  ├─ __init__.py
│     │  ├─ test_extract.py
│     │  ├─ test_metric.py
│     │  └─ test_module.py
│     ├─ fixtures
│     │  └─ mock_cache.json
│     ├─ mock_data.txt
│     ├─ test_graphrag.py
│     ├─ test_hnsw_vector_storage.py
│     ├─ test_json_parsing.py
│     ├─ test_neo4j_storage.py
│     ├─ test_networkx_storage.py
│     ├─ test_o.py
│     ├─ test_openai.py
│     ├─ test_rag.py
│     ├─ test_splitter.py
│     └─ zhuyuanzhang.txt
├─ nano_graphrag_cache_2025-02-21-04:20:58
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-04:21:16
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-04:21:19
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:07:45
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:08:08
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:08:21
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:25:06
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:25:29
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:25:32
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ package-lock.json
├─ pytest.ini
├─ requirements.txt
├─ scripts
│  ├─ __init__.py
│  ├─ agentic_ds.py
│  ├─ agentic_reason
│  │  ├─ __init__.py
│  │  ├─ cache.py
│  │  ├─ config.py
│  │  ├─ context_manager.py
│  │  ├─ data_loader.py
│  │  ├─ generation.py
│  │  ├─ knowledge_synthesizer.py
│  │  ├─ models.py
│  │  ├─ prompt_manager.py
│  │  ├─ reasoning_validator.py
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
│  │  │  ├─ compute_test_output_prediction_metrics.py
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
│  ├─ minimal_discourse_manager.py
│  ├─ minimal_lm_configs.py
│  ├─ project_context.txt
│  ├─ prompts.py
│  ├─ quicksum.py
│  ├─ run_agentic_reason.py
│  ├─ test_agentic_reasoning.py
│  ├─ test_minimal.py
│  ├─ test_qdrant_store.py
│  ├─ test_utils.py
│  ├─ tools
│  │  ├─ __init__.py
│  │  ├─ bing_search.py
│  │  ├─ creat_graph.py
│  │  ├─ duck_search.py
│  │  ├─ run_code.py
│  │  ├─ run_search.py
│  │  └─ temp.py
│  └─ utils
│     ├─ math_equivalence.py
│     └─ remote_llm.py
├─ setup.py
├─ temp.py
├─ tests
│  ├─ kv_store_llm_response_cache.json
│  ├─ nano_graphrag_cache_TEST
│  └─ test_discourse_manager.py
├─ tokenizers-main
│  ├─ .DS_Store
│  ├─ CITATION.cff
│  ├─ LICENSE
│  ├─ README.md
│  ├─ RELEASE.md
│  ├─ bindings
│  │  ├─ node
│  │  │  ├─ .cargo
│  │  │  │  └─ config.toml
│  │  │  ├─ .editorconfig
│  │  │  ├─ .eslintrc.yml
│  │  │  ├─ .prettierignore
│  │  │  ├─ .taplo.toml
│  │  │  ├─ .yarn
│  │  │  │  └─ releases
│  │  │  │     └─ yarn-3.5.1.cjs
│  │  │  ├─ .yarnrc.yml
│  │  │  ├─ Cargo.toml
│  │  │  ├─ LICENSE
│  │  │  ├─ Makefile
│  │  │  ├─ README.md
│  │  │  ├─ build.rs
│  │  │  ├─ examples
│  │  │  │  └─ documentation
│  │  │  │     ├─ pipeline.test.ts
│  │  │  │     └─ quicktour.test.ts
│  │  │  ├─ index.d.ts
│  │  │  ├─ index.js
│  │  │  ├─ jest.config.js
│  │  │  ├─ npm
│  │  │  │  ├─ android-arm-eabi
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ android-arm64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ darwin-arm64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ darwin-x64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ freebsd-x64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-arm-gnueabihf
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-arm64-gnu
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-arm64-musl
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-x64-gnu
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-x64-musl
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ win32-arm64-msvc
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ win32-ia32-msvc
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  └─ win32-x64-msvc
│  │  │  │     ├─ README.md
│  │  │  │     └─ package.json
│  │  │  ├─ package.json
│  │  │  ├─ rustfmt.toml
│  │  │  ├─ src
│  │  │  │  ├─ arc_rwlock_serde.rs
│  │  │  │  ├─ decoders.rs
│  │  │  │  ├─ encoding.rs
│  │  │  │  ├─ lib.rs
│  │  │  │  ├─ models.rs
│  │  │  │  ├─ normalizers.rs
│  │  │  │  ├─ pre_tokenizers.rs
│  │  │  │  ├─ processors.rs
│  │  │  │  ├─ tasks
│  │  │  │  │  ├─ mod.rs
│  │  │  │  │  ├─ models.rs
│  │  │  │  │  └─ tokenizer.rs
│  │  │  │  ├─ tokenizer.rs
│  │  │  │  ├─ trainers.rs
│  │  │  │  └─ utils.rs
│  │  │  ├─ tsconfig.json
│  │  │  ├─ types.ts
│  │  │  └─ yarn.lock
│  │  └─ python
│  │     ├─ .cargo
│  │     │  └─ config.toml
│  │     ├─ CHANGELOG.md
│  │     ├─ Cargo.toml
│  │     ├─ MANIFEST.in
│  │     ├─ Makefile
│  │     ├─ README.md
│  │     ├─ benches
│  │     │  └─ test_tiktoken.py
│  │     ├─ conftest.py
│  │     ├─ examples
│  │     │  ├─ custom_components.py
│  │     │  ├─ example.py
│  │     │  ├─ train_bert_wordpiece.py
│  │     │  ├─ train_bytelevel_bpe.py
│  │     │  ├─ train_with_datasets.py
│  │     │  └─ using_the_visualizer.ipynb
│  │     ├─ py_src
│  │     │  └─ tokenizers
│  │     │     ├─ __init__.py
│  │     │     ├─ __init__.pyi
│  │     │     ├─ decoders
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ implementations
│  │     │     │  ├─ __init__.py
│  │     │     │  ├─ base_tokenizer.py
│  │     │     │  ├─ bert_wordpiece.py
│  │     │     │  ├─ byte_level_bpe.py
│  │     │     │  ├─ char_level_bpe.py
│  │     │     │  ├─ sentencepiece_bpe.py
│  │     │     │  └─ sentencepiece_unigram.py
│  │     │     ├─ models
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ normalizers
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ pre_tokenizers
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ processors
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ tools
│  │     │     │  ├─ __init__.py
│  │     │     │  ├─ visualizer-styles.css
│  │     │     │  └─ visualizer.py
│  │     │     └─ trainers
│  │     │        ├─ __init__.py
│  │     │        └─ __init__.pyi
│  │     ├─ pyproject.toml
│  │     ├─ rust-toolchain
│  │     ├─ scripts
│  │     │  ├─ convert.py
│  │     │  ├─ sentencepiece_extractor.py
│  │     │  └─ spm_parity_check.py
│  │     ├─ setup.cfg
│  │     ├─ src
│  │     │  ├─ decoders.rs
│  │     │  ├─ encoding.rs
│  │     │  ├─ error.rs
│  │     │  ├─ lib.rs
│  │     │  ├─ models.rs
│  │     │  ├─ normalizers.rs
│  │     │  ├─ pre_tokenizers.rs
│  │     │  ├─ processors.rs
│  │     │  ├─ token.rs
│  │     │  ├─ tokenizer.rs
│  │     │  ├─ trainers.rs
│  │     │  └─ utils
│  │     │     ├─ iterators.rs
│  │     │     ├─ mod.rs
│  │     │     ├─ normalization.rs
│  │     │     ├─ pretokenization.rs
│  │     │     ├─ regex.rs
│  │     │     └─ serde_pyo3.rs
│  │     ├─ stub.py
│  │     ├─ test.txt
│  │     └─ tests
│  │        ├─ __init__.py
│  │        ├─ bindings
│  │        │  ├─ __init__.py
│  │        │  ├─ test_decoders.py
│  │        │  ├─ test_encoding.py
│  │        │  ├─ test_models.py
│  │        │  ├─ test_normalizers.py
│  │        │  ├─ test_pre_tokenizers.py
│  │        │  ├─ test_processors.py
│  │        │  ├─ test_tokenizer.py
│  │        │  └─ test_trainers.py
│  │        ├─ documentation
│  │        │  ├─ __init__.py
│  │        │  ├─ test_pipeline.py
│  │        │  ├─ test_quicktour.py
│  │        │  └─ test_tutorial_train_from_iterators.py
│  │        ├─ implementations
│  │        │  ├─ __init__.py
│  │        │  ├─ test_base_tokenizer.py
│  │        │  ├─ test_bert_wordpiece.py
│  │        │  ├─ test_byte_level_bpe.py
│  │        │  ├─ test_char_bpe.py
│  │        │  └─ test_sentencepiece.py
│  │        ├─ test_serialization.py
│  │        └─ utils.py
│  ├─ docs
│  │  ├─ Makefile
│  │  ├─ README.md
│  │  ├─ source
│  │  │  ├─ _ext
│  │  │  │  ├─ entities.py
│  │  │  │  ├─ rust_doc.py
│  │  │  │  └─ toctree_tags.py
│  │  │  ├─ _static
│  │  │  │  ├─ css
│  │  │  │  │  ├─ Calibre-Light.ttf
│  │  │  │  │  ├─ Calibre-Medium.otf
│  │  │  │  │  ├─ Calibre-Regular.otf
│  │  │  │  │  ├─ Calibre-Thin.otf
│  │  │  │  │  ├─ code-snippets.css
│  │  │  │  │  └─ huggingface.css
│  │  │  │  └─ js
│  │  │  │     └─ custom.js
│  │  │  ├─ api
│  │  │  │  ├─ node.inc
│  │  │  │  ├─ python.inc
│  │  │  │  ├─ reference.rst
│  │  │  │  └─ rust.inc
│  │  │  ├─ components.rst
│  │  │  ├─ conf.py
│  │  │  ├─ entities.inc
│  │  │  ├─ index.rst
│  │  │  ├─ installation
│  │  │  │  ├─ main.rst
│  │  │  │  ├─ node.inc
│  │  │  │  ├─ python.inc
│  │  │  │  └─ rust.inc
│  │  │  ├─ pipeline.rst
│  │  │  ├─ quicktour.rst
│  │  │  └─ tutorials
│  │  │     └─ python
│  │  │        └─ training_from_memory.rst
│  │  └─ source-doc-builder
│  │     ├─ _toctree.yml
│  │     ├─ api
│  │     │  ├─ added-tokens.mdx
│  │     │  ├─ decoders.mdx
│  │     │  ├─ encode-inputs.mdx
│  │     │  ├─ encoding.mdx
│  │     │  ├─ input-sequences.mdx
│  │     │  ├─ models.mdx
│  │     │  ├─ normalizers.mdx
│  │     │  ├─ post-processors.mdx
│  │     │  ├─ pre-tokenizers.mdx
│  │     │  ├─ tokenizer.mdx
│  │     │  ├─ trainers.mdx
│  │     │  └─ visualizer.mdx
│  │     ├─ components.mdx
│  │     ├─ index.mdx
│  │     ├─ installation.mdx
│  │     ├─ pipeline.mdx
│  │     ├─ quicktour.mdx
│  │     └─ training_from_memory.mdx
│  └─ tokenizers
│     ├─ CHANGELOG.md
│     ├─ Cargo.toml
│     ├─ LICENSE
│     ├─ Makefile
│     ├─ README.md
│     ├─ README.tpl
│     ├─ benches
│     │  ├─ bert_benchmark.rs
│     │  ├─ bpe_benchmark.rs
│     │  ├─ common
│     │  │  └─ mod.rs
│     │  ├─ layout_benchmark.rs
│     │  ├─ llama3.rs
│     │  └─ unigram_benchmark.rs
│     ├─ examples
│     │  ├─ encode_batch.rs
│     │  ├─ serialization.rs
│     │  └─ unstable_wasm
│     │     ├─ Cargo.toml
│     │     ├─ README.md
│     │     ├─ src
│     │     │  ├─ lib.rs
│     │     │  └─ utils.rs
│     │     ├─ tests
│     │     │  └─ web.rs
│     │     └─ www
│     │        ├─ .bin
│     │        │  └─ create-wasm-app.js
│     │        ├─ .travis.yml
│     │        ├─ LICENSE-APACHE
│     │        ├─ LICENSE-MIT
│     │        ├─ README.md
│     │        ├─ bootstrap.js
│     │        ├─ index.html
│     │        ├─ index.js
│     │        ├─ package-lock.json
│     │        ├─ package.json
│     │        └─ webpack.config.js
│     ├─ rust-toolchain
│     ├─ src
│     │  ├─ decoders
│     │  │  ├─ bpe.rs
│     │  │  ├─ byte_fallback.rs
│     │  │  ├─ ctc.rs
│     │  │  ├─ fuse.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ sequence.rs
│     │  │  ├─ strip.rs
│     │  │  └─ wordpiece.rs
│     │  ├─ lib.rs
│     │  ├─ models
│     │  │  ├─ bpe
│     │  │  │  ├─ mod.rs
│     │  │  │  ├─ model.rs
│     │  │  │  ├─ serialization.rs
│     │  │  │  ├─ trainer.rs
│     │  │  │  └─ word.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ unigram
│     │  │  │  ├─ lattice.rs
│     │  │  │  ├─ mod.rs
│     │  │  │  ├─ model.rs
│     │  │  │  ├─ serialization.rs
│     │  │  │  ├─ trainer.rs
│     │  │  │  └─ trie.rs
│     │  │  ├─ wordlevel
│     │  │  │  ├─ mod.rs
│     │  │  │  ├─ serialization.rs
│     │  │  │  └─ trainer.rs
│     │  │  └─ wordpiece
│     │  │     ├─ mod.rs
│     │  │     ├─ serialization.rs
│     │  │     └─ trainer.rs
│     │  ├─ normalizers
│     │  │  ├─ bert.rs
│     │  │  ├─ byte_level.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ precompiled.rs
│     │  │  ├─ prepend.rs
│     │  │  ├─ replace.rs
│     │  │  ├─ strip.rs
│     │  │  ├─ unicode.rs
│     │  │  └─ utils.rs
│     │  ├─ pre_tokenizers
│     │  │  ├─ bert.rs
│     │  │  ├─ byte_level.rs
│     │  │  ├─ delimiter.rs
│     │  │  ├─ digits.rs
│     │  │  ├─ metaspace.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ punctuation.rs
│     │  │  ├─ sequence.rs
│     │  │  ├─ split.rs
│     │  │  ├─ unicode_scripts
│     │  │  │  ├─ mod.rs
│     │  │  │  ├─ pre_tokenizer.rs
│     │  │  │  └─ scripts.rs
│     │  │  └─ whitespace.rs
│     │  ├─ processors
│     │  │  ├─ bert.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ roberta.rs
│     │  │  ├─ sequence.rs
│     │  │  └─ template.rs
│     │  ├─ tokenizer
│     │  │  ├─ added_vocabulary.rs
│     │  │  ├─ encoding.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ normalizer.rs
│     │  │  ├─ pattern.rs
│     │  │  ├─ pre_tokenizer.rs
│     │  │  └─ serialization.rs
│     │  └─ utils
│     │     ├─ cache.rs
│     │     ├─ fancy.rs
│     │     ├─ from_pretrained.rs
│     │     ├─ iter.rs
│     │     ├─ mod.rs
│     │     ├─ onig.rs
│     │     ├─ padding.rs
│     │     ├─ parallelism.rs
│     │     ├─ progress.rs
│     │     └─ truncation.rs
│     └─ tests
│        ├─ added_tokens.rs
│        ├─ common
│        │  └─ mod.rs
│        ├─ documentation.rs
│        ├─ from_pretrained.rs
│        ├─ offsets.rs
│        ├─ serialization.rs
│        ├─ stream.rs
│        ├─ training.rs
│        └─ unigram.rs
├─ tree.md
└─ venv311
   ├─ bin
   │  ├─ Activate.ps1
   │  ├─ activate
   │  ├─ activate.csh
   │  ├─ activate.fish
   │  ├─ alembic
   │  ├─ chroma
   │  ├─ coloredlogs
   │  ├─ datasets-cli
   │  ├─ distro
   │  ├─ dotenv
   │  ├─ email_validator
   │  ├─ esprima
   │  ├─ f2py
   │  ├─ fastapi
   │  ├─ fastavro
   │  ├─ fonttools
   │  ├─ futurize
   │  ├─ get_gprof
   │  ├─ get_objgraph
   │  ├─ griffe
   │  ├─ gunicorn
   │  ├─ httpx
   │  ├─ huggingface-cli
   │  ├─ humanfriendly
   │  ├─ isympy
   │  ├─ jp.py
   │  ├─ json_repair
   │  ├─ jsonschema
   │  ├─ litellm
   │  ├─ mako-render
   │  ├─ markdown-it
   │  ├─ normalizer
   │  ├─ numba
   │  ├─ onnxruntime_test
   │  ├─ openai
   │  ├─ opentelemetry-bootstrap
   │  ├─ opentelemetry-instrument
   │  ├─ optuna
   │  ├─ pasteurize
   │  ├─ pip
   │  ├─ pip3
   │  ├─ pip3.11
   │  ├─ py.test
   │  ├─ pyftmerge
   │  ├─ pyftsubset
   │  ├─ pygmentize
   │  ├─ pyproject-build
   │  ├─ pyrsa-decrypt
   │  ├─ pyrsa-encrypt
   │  ├─ pyrsa-keygen
   │  ├─ pyrsa-priv2pub
   │  ├─ pyrsa-sign
   │  ├─ pyrsa-verify
   │  ├─ pytest
   │  ├─ python
   │  ├─ python3
   │  ├─ python3.11
   │  ├─ rq
   │  ├─ rqinfo
   │  ├─ rqworker
   │  ├─ tqdm
   │  ├─ ttx
   │  ├─ typer
   │  ├─ undill
   │  ├─ uvicorn
   │  ├─ watchfiles
   │  ├─ wheel
   │  └─ wsdump
   ├─ include
   │  └─ python3.11
   ├─ pyvenv.cfg
   └─ share
      └─ man
         └─ man1
            ├─ isympy.1
            └─ ttx.1

```
```
Agentic-Reasoning
├─ .DS_Store
├─ .trunk
│  ├─ actions
│  │  ├─ trunk-cache-prune
│  │  │  ├─ 2025-03-04-18-40-31.503.yaml
│  │  │  ├─ 2025-03-04-19-40-31.843.yaml
│  │  │  ├─ 2025-03-05-19-07-40.522.yaml
│  │  │  ├─ 2025-03-06-19-02-26.794.yaml
│  │  │  └─ 2025-03-07-19-09-00.866.yaml
│  │  ├─ trunk-share-with-everyone
│  │  │  ├─ 2025-03-04-18-40-31.509.yaml
│  │  │  ├─ 2025-03-04-19-40-31.340.yaml
│  │  │  ├─ 2025-03-05-19-07-40.470.yaml
│  │  │  ├─ 2025-03-06-19-02-27.202.yaml
│  │  │  └─ 2025-03-07-19-09-00.900.yaml
│  │  ├─ trunk-single-player-auto-on-upgrade
│  │  │  ├─ 2025-03-04-18-46-09.495.yaml
│  │  │  ├─ 2025-03-04-19-41-10.57.yaml
│  │  │  ├─ 2025-03-05-19-08-21.0.yaml
│  │  │  ├─ 2025-03-06-19-03-38.785.yaml
│  │  │  └─ 2025-03-07-19-09-41.262.yaml
│  │  ├─ trunk-single-player-auto-upgrade
│  │  │  ├─ 2025-03-04-19-46-15.87.yaml
│  │  │  ├─ 2025-03-05-19-46-14.515.yaml
│  │  │  ├─ 2025-03-06-20-20-29.525.yaml
│  │  │  └─ 2025-03-07-19-46-14.497.yaml
│  │  ├─ trunk-upgrade-available
│  │  │  ├─ 2025-03-04-18-46-23.263.yaml
│  │  │  ├─ 2025-03-04-19-40-46.247.yaml
│  │  │  ├─ 2025-03-04-19-40-58.515.yaml
│  │  │  ├─ 2025-03-04-19-41-09.760.yaml
│  │  │  ├─ 2025-03-04-19-41-21.265.yaml
│  │  │  ├─ 2025-03-04-19-41-26.256.yaml
│  │  │  ├─ 2025-03-04-19-46-22.599.yaml
│  │  │  ├─ 2025-03-04-19-46-28.847.yaml
│  │  │  ├─ 2025-03-05-01-08-14.501.yaml
│  │  │  ├─ 2025-03-05-01-08-14.553.yaml
│  │  │  ├─ 2025-03-05-06-46-58.260.yaml
│  │  │  ├─ 2025-03-05-06-46-58.261.yaml
│  │  │  ├─ 2025-03-05-08-02-02.804.yaml
│  │  │  ├─ 2025-03-05-08-46-58.763.yaml
│  │  │  ├─ 2025-03-05-11-04-36.607.yaml
│  │  │  ├─ 2025-03-05-11-04-38.780.yaml
│  │  │  ├─ 2025-03-05-12-22-00.661.yaml
│  │  │  ├─ 2025-03-05-13-04-38.236.yaml
│  │  │  ├─ 2025-03-05-14-29-48.199.yaml
│  │  │  ├─ 2025-03-05-15-19-14.192.yaml
│  │  │  ├─ 2025-03-05-19-07-54.730.yaml
│  │  │  ├─ 2025-03-05-19-07-55.264.yaml
│  │  │  ├─ 2025-03-05-19-08-06.175.yaml
│  │  │  ├─ 2025-03-05-19-08-20.529.yaml
│  │  │  ├─ 2025-03-05-19-08-29.522.yaml
│  │  │  ├─ 2025-03-05-19-08-34.266.yaml
│  │  │  ├─ 2025-03-05-19-46-28.511.yaml
│  │  │  ├─ 2025-03-05-20-22-36.795.yaml
│  │  │  ├─ 2025-03-05-21-07-54.442.yaml
│  │  │  ├─ 2025-03-05-22-24-11.766.yaml
│  │  │  ├─ 2025-03-05-23-07-52.142.yaml
│  │  │  ├─ 2025-03-06-01-56-14.913.yaml
│  │  │  ├─ 2025-03-06-01-56-14.970.yaml
│  │  │  ├─ 2025-03-06-02-56-12.58.yaml
│  │  │  ├─ 2025-03-06-07-56-48.258.yaml
│  │  │  ├─ 2025-03-06-07-56-48.260.yaml
│  │  │  ├─ 2025-03-06-10-28-38.200.yaml
│  │  │  ├─ 2025-03-06-10-28-39.511.yaml
│  │  │  ├─ 2025-03-06-11-42-40.709.yaml
│  │  │  ├─ 2025-03-06-12-28-37.509.yaml
│  │  │  ├─ 2025-03-06-13-28-34.213.yaml
│  │  │  ├─ 2025-03-06-14-28-35.194.yaml
│  │  │  ├─ 2025-03-06-15-29-46.776.yaml
│  │  │  ├─ 2025-03-06-16-51-52.58.yaml
│  │  │  ├─ 2025-03-06-17-28-35.255.yaml
│  │  │  ├─ 2025-03-06-18-28-33.95.yaml
│  │  │  ├─ 2025-03-06-19-02-51.237.yaml
│  │  │  ├─ 2025-03-06-19-03-33.781.yaml
│  │  │  ├─ 2025-03-06-19-03-47.516.yaml
│  │  │  ├─ 2025-03-06-19-04-06.143.yaml
│  │  │  ├─ 2025-03-06-20-20-36.517.yaml
│  │  │  ├─ 2025-03-06-20-20-41.457.yaml
│  │  │  ├─ 2025-03-06-20-30-16.69.yaml
│  │  │  ├─ 2025-03-06-21-28-35.768.yaml
│  │  │  ├─ 2025-03-06-22-46-19.57.yaml
│  │  │  ├─ 2025-03-06-23-28-35.445.yaml
│  │  │  ├─ 2025-03-07-02-56-03.236.yaml
│  │  │  ├─ 2025-03-07-02-56-03.261.yaml
│  │  │  ├─ 2025-03-07-04-52-27.216.yaml
│  │  │  ├─ 2025-03-07-04-56-02.770.yaml
│  │  │  ├─ 2025-03-07-08-14-56.732.yaml
│  │  │  ├─ 2025-03-07-08-14-58.773.yaml
│  │  │  ├─ 2025-03-07-09-35-30.701.yaml
│  │  │  ├─ 2025-03-07-10-17-34.510.yaml
│  │  │  ├─ 2025-03-07-11-33-23.284.yaml
│  │  │  ├─ 2025-03-07-12-53-31.767.yaml
│  │  │  ├─ 2025-03-07-13-14-56.514.yaml
│  │  │  ├─ 2025-03-07-14-14-59.259.yaml
│  │  │  ├─ 2025-03-07-15-14-56.270.yaml
│  │  │  ├─ 2025-03-07-19-09-15.253.yaml
│  │  │  ├─ 2025-03-07-19-09-15.258.yaml
│  │  │  ├─ 2025-03-07-19-09-24.715.yaml
│  │  │  ├─ 2025-03-07-19-09-36.58.yaml
│  │  │  ├─ 2025-03-07-19-09-49.849.yaml
│  │  │  ├─ 2025-03-07-19-09-54.514.yaml
│  │  │  ├─ 2025-03-07-19-46-28.805.yaml
│  │  │  ├─ 2025-03-07-20-18-06.65.yaml
│  │  │  ├─ 2025-03-07-21-17-07.254.yaml
│  │  │  └─ 2025-03-07-22-09-13.58.yaml
│  │  └─ trunk-whoami
│  │     ├─ 2025-03-04-19-46-22.870.yaml
│  │     ├─ 2025-03-05-19-46-20.499.yaml
│  │     ├─ 2025-03-06-20-20-35.468.yaml
│  │     └─ 2025-03-07-19-46-20.593.yaml
│  ├─ configs
│  │  ├─ .isort.cfg
│  │  ├─ .markdownlint.yaml
│  │  ├─ .yamllint.yaml
│  │  └─ ruff.toml
│  ├─ notifications
│  │  ├─ trunk-share-with-everyone.yaml
│  │  ├─ trunk-share-with-everyone.yaml.lock
│  │  └─ trunk-upgrade.yaml.lock
│  ├─ out
│  │  ├─ 01SD0.yaml
│  │  ├─ 0K2VL.yaml
│  │  ├─ 14S7M.yaml
│  │  ├─ 15MS6.yaml
│  │  ├─ 15Q62.yaml
│  │  ├─ 15QY7.yaml
│  │  ├─ 1AB2Z.yaml
│  │  ├─ 1B8WY.yaml
│  │  ├─ 1BP34.yaml
│  │  ├─ 1FDLN.yaml
│  │  ├─ 1H7PR.yaml
│  │  ├─ 1KQ4R.yaml
│  │  ├─ 2AUBW.yaml
│  │  ├─ 2PEQN.yaml
│  │  ├─ 3EL8B.yaml
│  │  ├─ 3LYG3.yaml
│  │  ├─ 3NGWZ.yaml
│  │  ├─ 3TRAX.yaml
│  │  ├─ 3WSQ6.yaml
│  │  ├─ 3ZUS7.yaml
│  │  ├─ 4UB2T.yaml
│  │  ├─ 50HFL.yaml
│  │  ├─ 6656M.yaml
│  │  ├─ 673F3.yaml
│  │  ├─ 67SMA.yaml
│  │  ├─ 6CV8W.yaml
│  │  ├─ 6LGQE.yaml
│  │  ├─ 71JU9.yaml
│  │  ├─ 720YS.yaml
│  │  ├─ 8534G.yaml
│  │  ├─ 85LNt.yaml
│  │  ├─ 8AJ74.yaml
│  │  ├─ 8NGB8.yaml
│  │  ├─ 8phPF.yaml
│  │  ├─ 99N96.yaml
│  │  ├─ 9B2Y7.yaml
│  │  ├─ 9NGGP.yaml
│  │  ├─ B3XFL.yaml
│  │  ├─ B8Z6K.yaml
│  │  ├─ BaMey.yaml
│  │  ├─ C75UT.yaml
│  │  ├─ CGL0E.yaml
│  │  ├─ CJW9S.yaml
│  │  ├─ CLCG4.yaml
│  │  ├─ D7XUT.yaml
│  │  ├─ DKLRV.yaml
│  │  ├─ EGCL5.yaml
│  │  ├─ EOcg1.yaml
│  │  ├─ F3D7W.yaml
│  │  ├─ F43J8.yaml
│  │  ├─ G0MCM.yaml
│  │  ├─ G61PD.yaml
│  │  ├─ GAKL1.yaml
│  │  ├─ GR3PG.yaml
│  │  ├─ GUAFJ.yaml
│  │  ├─ GXGR2.yaml
│  │  ├─ HA6S9.yaml
│  │  ├─ HC96S.yaml
│  │  ├─ HGMMR.yaml
│  │  ├─ HP72V.yaml
│  │  ├─ HP9YC.yaml
│  │  ├─ J2195.yaml
│  │  ├─ JLHUX.yaml
│  │  ├─ JTVK7.yaml
│  │  ├─ JZA6Y.yaml
│  │  ├─ KFX8P.yaml
│  │  ├─ KXGWK.yaml
│  │  ├─ L56Q4.yaml
│  │  ├─ M058Y.yaml
│  │  ├─ ND13J.yaml
│  │  ├─ NLMEU.yaml
│  │  ├─ NuGSi.yaml
│  │  ├─ P0K11.yaml
│  │  ├─ PX510.yaml
│  │  ├─ Q4JK6.yaml
│  │  ├─ Q6CMS.yaml
│  │  ├─ S3B1T.yaml
│  │  ├─ S6VLJ.yaml
│  │  ├─ SPYCM.yaml
│  │  ├─ SXWQV.yaml
│  │  ├─ T0WWD.yaml
│  │  ├─ U1R3H.yaml
│  │  ├─ U698L.yaml
│  │  ├─ U8PU6.yaml
│  │  ├─ V3X73.yaml
│  │  ├─ V9SAU.yaml
│  │  ├─ VFUVN.yaml
│  │  ├─ W9bB8.yaml
│  │  ├─ WKDXX.yaml
│  │  ├─ WP6HQ.yaml
│  │  ├─ X5Y3D.yaml
│  │  ├─ XHMT7.yaml
│  │  ├─ XKBKU.yaml
│  │  ├─ YBD19.yaml
│  │  ├─ Z0A55.yaml
│  │  ├─ Z3C7Y.yaml
│  │  ├─ ZNEH7.yaml
│  │  ├─ fR6ow.yaml
│  │  ├─ kD3vB.yaml
│  │  ├─ rV6Wv.yaml
│  │  └─ wTXCk.yaml
│  ├─ plugins
│  │  └─ trunk
│  │     ├─ .devcontainer.json
│  │     ├─ .editorconfig
│  │     ├─ .trunk
│  │     │  ├─ setup-ci
│  │     │  │  └─ action.yaml
│  │     │  └─ trunk.yaml
│  │     ├─ CONTRIBUTING.md
│  │     ├─ LICENSE
│  │     ├─ README.md
│  │     ├─ actions
│  │     │  ├─ buf
│  │     │  │  ├─ README.md
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ commitizen
│  │     │  │  ├─ README.md
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ commitlint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ commitlint.test.ts
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ git
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ git-blame-ignore-revs
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ update_config.sh
│  │     │  ├─ go-mod-tidy
│  │     │  │  ├─ README.md
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ go-mod-tidy-vendor
│  │     │  │  ├─ README.md
│  │     │  │  ├─ go-mod-tidy-vendor.sh
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ hello-world
│  │     │  │  └─ python
│  │     │  │     ├─ README.md
│  │     │  │     ├─ hello
│  │     │  │     ├─ hello_world.test.ts
│  │     │  │     ├─ plugin.yaml
│  │     │  │     └─ requirements.txt
│  │     │  ├─ npm-check
│  │     │  │  ├─ README.md
│  │     │  │  ├─ npm.png
│  │     │  │  ├─ npm_check.js
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ npm-check-pre-push
│  │     │  │  ├─ npm_check.js
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ poetry
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ poetry.test.ts
│  │     │  │  └─ requirements.txt
│  │     │  ├─ submodules
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ terraform-docs
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform-docs.py
│  │     │  ├─ trunk
│  │     │  │  └─ plugin.yaml
│  │     │  └─ yarn-check
│  │     │     ├─ README.md
│  │     │     ├─ package.json
│  │     │     ├─ plugin.yaml
│  │     │     ├─ yarn.png
│  │     │     └─ yarn_check.js
│  │     ├─ eslint.config.cjs
│  │     ├─ jest.config.json
│  │     ├─ linters
│  │     │  ├─ actionlint
│  │     │  │  ├─ actionlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ansible-lint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ ansible_lint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ autopep8
│  │     │  │  ├─ autopep8.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ bandit
│  │     │  │  ├─ bandit.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ biome
│  │     │  │  ├─ biome.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ black
│  │     │  │  ├─ black.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ brakeman
│  │     │  │  ├─ brakeman.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ buf
│  │     │  │  ├─ buf.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ buildifier
│  │     │  │  ├─ buildifier.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cfnlint
│  │     │  │  ├─ cfnlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ checkov
│  │     │  │  ├─ checkov.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ circleci
│  │     │  │  ├─ circleci.test.ts
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ run.sh
│  │     │  ├─ clang-format
│  │     │  │  ├─ clang_format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clang-tidy
│  │     │  │  ├─ .clang-tidy
│  │     │  │  ├─ clang_tidy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clippy
│  │     │  │  ├─ clippy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cmake-format
│  │     │  │  ├─ cmake-format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ codespell
│  │     │  │  ├─ codespell.test.ts
│  │     │  │  ├─ codespell_to_sarif.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cspell
│  │     │  │  ├─ cspell.test.ts
│  │     │  │  ├─ cspell.yaml
│  │     │  │  ├─ expected_basic_issues.json
│  │     │  │  ├─ expected_dictionary_issues.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cue-fmt
│  │     │  │  ├─ cue_fmt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dart
│  │     │  │  ├─ dart.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ deno
│  │     │  │  ├─ deno.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ detekt
│  │     │  │  ├─ detekt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ djlint
│  │     │  │  ├─ .djlintrc
│  │     │  │  ├─ README.md
│  │     │  │  ├─ djlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dotenv-linter
│  │     │  │  ├─ dotenv_linter.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dotnet-format
│  │     │  │  ├─ dotnet_format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dustilock
│  │     │  │  ├─ dustilock.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ eslint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ eslint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ flake8
│  │     │  │  ├─ .flake8
│  │     │  │  ├─ flake8.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ git-diff-check
│  │     │  │  ├─ git_diff_check.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gitleaks
│  │     │  │  ├─ gitleaks.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gofmt
│  │     │  │  ├─ gofmt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gofumpt
│  │     │  │  ├─ gofumpt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ goimports
│  │     │  │  ├─ goimports.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gokart
│  │     │  │  ├─ analyzers.yml
│  │     │  │  ├─ gokart.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ golangci-lint
│  │     │  │  ├─ golangci_lint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ golines
│  │     │  │  ├─ golines.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ google-java-format
│  │     │  │  ├─ google-java-format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ graphql-schema-linter
│  │     │  │  ├─ graphql_schema_linter.test.ts
│  │     │  │  ├─ parse.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ hadolint
│  │     │  │  ├─ .hadolint.yaml
│  │     │  │  ├─ hadolint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ haml-lint
│  │     │  │  ├─ haml_lint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ isort
│  │     │  │  ├─ .isort.cfg
│  │     │  │  ├─ isort.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ iwyu
│  │     │  │  ├─ iwyu.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ktlint
│  │     │  │  ├─ ktlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ kube-linter
│  │     │  │  ├─ kube_linter.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdown-link-check
│  │     │  │  ├─ markdown-link-check.test.ts
│  │     │  │  ├─ parse.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdown-table-prettify
│  │     │  │  ├─ markdown_table_prettify.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdownlint
│  │     │  │  ├─ .markdownlint.yaml
│  │     │  │  ├─ markdownlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdownlint-cli2
│  │     │  │  ├─ markdownlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ mypy
│  │     │  │  ├─ mypy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ nancy
│  │     │  │  ├─ expected_issues.json
│  │     │  │  ├─ nancy.test.ts
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ run.sh
│  │     │  ├─ nixpkgs-fmt
│  │     │  │  ├─ nixpkgs_fmt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ opa
│  │     │  │  ├─ opa.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ osv-scanner
│  │     │  │  ├─ expected_issues.json
│  │     │  │  ├─ osv_scanner.test.ts
│  │     │  │  ├─ osv_to_sarif.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ oxipng
│  │     │  │  ├─ oxipng.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ perlcritic
│  │     │  │  ├─ .perlcriticrc
│  │     │  │  ├─ perlcritic.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ perltidy
│  │     │  │  ├─ .perltidyrc
│  │     │  │  ├─ perltidy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ php-cs-fixer
│  │     │  │  ├─ php-cs-fixer.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ phpstan
│  │     │  │  ├─ phpstan.test.ts
│  │     │  │  ├─ phpstan_parser.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ plugin.yaml
│  │     │  ├─ pmd
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pmd.test.ts
│  │     │  ├─ pragma-once
│  │     │  │  ├─ README.md
│  │     │  │  ├─ fix.sh
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pragma_once.test.ts
│  │     │  ├─ pre-commit-hooks
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pre_commit_hooks.test.ts
│  │     │  ├─ prettier
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ prettier.test.ts
│  │     │  │  └─ prettier_to_sarif.py
│  │     │  ├─ prisma
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ prisma.test.ts
│  │     │  ├─ psscriptanalyzer
│  │     │  │  ├─ README.md
│  │     │  │  ├─ format.ps1
│  │     │  │  ├─ lint.ps1
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ psscriptanalyzer.test.ts
│  │     │  ├─ pylint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pylint.test.ts
│  │     │  ├─ pyright
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ pyright.test.ts
│  │     │  │  └─ pyright_to_sarif.py
│  │     │  ├─ regal
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ regal.test.ts
│  │     │  ├─ remark-lint
│  │     │  │  ├─ .remarkrc.yaml
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ remark_lint.test.ts
│  │     │  ├─ renovate
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ renovate.test.ts
│  │     │  ├─ rome
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ rome.test.ts
│  │     │  ├─ rubocop
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ rubocop.test.ts
│  │     │  │  └─ rubocop_to_sarif.py
│  │     │  ├─ ruff
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ ruff.test.ts
│  │     │  │  ├─ ruff.toml
│  │     │  │  └─ ruff_to_sarif.py
│  │     │  ├─ rufo
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ rufo.test.ts
│  │     │  ├─ rustfmt
│  │     │  │  ├─ .rustfmt.toml
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ rustfmt.test.ts
│  │     │  ├─ scalafmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ scalafmt.test.ts
│  │     │  ├─ semgrep
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ semgrep.test.ts
│  │     │  ├─ shellcheck
│  │     │  │  ├─ .shellcheckrc
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ shellcheck.test.ts
│  │     │  ├─ shfmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ shfmt.test.ts
│  │     │  ├─ snyk
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ snyk.test.ts
│  │     │  ├─ sort-package-json
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sort_package_json.test.ts
│  │     │  ├─ sourcery
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sourcery.test.ts
│  │     │  ├─ sql-formatter
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sql_formatter.test.ts
│  │     │  ├─ sqlfluff
│  │     │  │  ├─ .sqlfluff
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ sqlfluff.test.ts
│  │     │  │  └─ sqlfluff_to_sarif.py
│  │     │  ├─ sqlfmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sqlfmt.test.ts
│  │     │  ├─ squawk
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ squawk.test.ts
│  │     │  ├─ standardrb
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ standardrb.test.ts
│  │     │  ├─ stringslint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ stringslint.test.ts
│  │     │  ├─ stylelint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ stylelint.test.ts
│  │     │  ├─ stylua
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ stylua.test.ts
│  │     │  │  └─ stylua.toml
│  │     │  ├─ svgo
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ svgo.config.mjs
│  │     │  │  └─ svgo.test.ts
│  │     │  ├─ swiftformat
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ swiftformat.test.ts
│  │     │  ├─ swiftlint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ swiftlint.test.ts
│  │     │  ├─ taplo
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ taplo.test.ts
│  │     │  ├─ terraform
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform.test.ts
│  │     │  ├─ terragrunt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terragrunt.test.ts
│  │     │  ├─ terrascan
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ sarif_to_sarif.py
│  │     │  │  └─ terrascan.test.ts
│  │     │  ├─ tflint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tflint.test.ts
│  │     │  ├─ tfsec
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfsec.test.ts
│  │     │  ├─ tofu
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tofu.test.ts
│  │     │  ├─ trivy
│  │     │  │  ├─ README.md
│  │     │  │  ├─ config_expected_issues.json
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ trivy.test.ts
│  │     │  │  ├─ trivy_config_to_sarif.py
│  │     │  │  ├─ trivy_fs_secret_to_sarif.py
│  │     │  │  ├─ trivy_fs_vuln_to_sarif.py
│  │     │  │  └─ vuln_expected_issues.json
│  │     │  ├─ trufflehog
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ trufflehog.test.ts
│  │     │  │  └─ trufflehog_to_sarif.py
│  │     │  ├─ trunk-toolbox
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ trunk_toolbox.test.ts
│  │     │  ├─ txtpbfmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ txtpbfmt.test.ts
│  │     │  ├─ vale
│  │     │  │  ├─ .vale.ini
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ vale.test.ts
│  │     │  ├─ yamllint
│  │     │  │  ├─ .yamllint.yaml
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ yamllint.test.ts
│  │     │  └─ yapf
│  │     │     ├─ plugin.yaml
│  │     │     └─ yapf.test.ts
│  │     ├─ package-lock.json
│  │     ├─ package.json
│  │     ├─ plugin.yaml
│  │     ├─ repo-tools
│  │     │  ├─ definition-checker
│  │     │  │  └─ check.ts
│  │     │  ├─ linter-test-helper
│  │     │  │  ├─ generate
│  │     │  │  ├─ linter_sample.test.ts
│  │     │  │  ├─ linter_sample_plugin.yaml
│  │     │  │  └─ requirements.txt
│  │     │  └─ tool-test-helper
│  │     │     ├─ generate
│  │     │     ├─ requirements.txt
│  │     │     ├─ tool_sample.test.ts
│  │     │     └─ tool_sample_plugin.yaml
│  │     ├─ runtimes
│  │     │  ├─ README.md
│  │     │  ├─ go
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ java
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ node
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ php
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ python
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ruby
│  │     │  │  └─ plugin.yaml
│  │     │  └─ rust
│  │     │     └─ plugin.yaml
│  │     ├─ security.md
│  │     ├─ tests
│  │     │  ├─ README.md
│  │     │  ├─ driver
│  │     │  │  ├─ action_driver.ts
│  │     │  │  ├─ driver.ts
│  │     │  │  ├─ index.ts
│  │     │  │  ├─ lint_driver.ts
│  │     │  │  └─ tool_driver.ts
│  │     │  ├─ index.ts
│  │     │  ├─ jest_setup.ts
│  │     │  ├─ parse
│  │     │  │  └─ index.ts
│  │     │  ├─ repo_tests
│  │     │  │  ├─ config_check.test.ts
│  │     │  │  ├─ readme_inclusion.test.ts
│  │     │  │  └─ valid_package_download.test.ts
│  │     │  ├─ reporter
│  │     │  │  ├─ index.js
│  │     │  │  └─ reporter.ts
│  │     │  ├─ types
│  │     │  │  └─ index.ts
│  │     │  └─ utils
│  │     │     ├─ index.ts
│  │     │     ├─ landing_state.ts
│  │     │     └─ trunk_config.ts
│  │     ├─ tools
│  │     │  ├─ 1password-cli
│  │     │  │  ├─ 1password_cli.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ act
│  │     │  │  ├─ act.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ action-validator
│  │     │  │  ├─ action_validator.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ adr
│  │     │  │  ├─ adr.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ age
│  │     │  │  ├─ age.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ agebox
│  │     │  │  ├─ agebox.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ air
│  │     │  │  ├─ air.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ alp
│  │     │  │  ├─ alp.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ amazon-ecr-credential-helper
│  │     │  │  ├─ amazon_ecr_credential_helper.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ asciinema
│  │     │  │  ├─ asciinema.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ assh
│  │     │  │  ├─ assh.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ aws-amplify
│  │     │  │  ├─ aws_amplify.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ awscli
│  │     │  │  ├─ awscli.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ bazel
│  │     │  │  ├─ bazel.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ bazel-differ
│  │     │  │  ├─ bazel.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ circleci
│  │     │  │  ├─ circleci.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clangd
│  │     │  │  ├─ clangd.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clangd-indexing-tools
│  │     │  │  ├─ clangd_indexing_tools.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dbt-cli
│  │     │  │  ├─ dbt_cli.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ deno
│  │     │  │  ├─ deno.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ diff-so-fancy
│  │     │  │  ├─ diff_so_fancy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ difft
│  │     │  │  ├─ difft.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ docker-credential-ecr-login
│  │     │  │  ├─ docker-credential-ecr-login.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dotnet
│  │     │  │  ├─ dotnet.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ eksctl
│  │     │  │  ├─ eksctl.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gh
│  │     │  │  ├─ gh.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gk
│  │     │  │  ├─ gk.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ goreleaser
│  │     │  │  ├─ goreleaser.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ grpcui
│  │     │  │  ├─ grpcui.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gt
│  │     │  │  ├─ gt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gulp
│  │     │  │  ├─ gulp.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ helm
│  │     │  │  ├─ helm.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ibazel
│  │     │  │  ├─ ibazel.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ istioctl
│  │     │  │  ├─ istioctl.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ jq
│  │     │  │  ├─ jq.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ kubectl
│  │     │  │  ├─ kubectl.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ minikube
│  │     │  │  ├─ minikube.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ paratest
│  │     │  │  ├─ paratest.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ phpunit
│  │     │  │  ├─ phpunit.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ platformio
│  │     │  │  ├─ platformio.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ pnpm
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pnpm.test.ts
│  │     │  ├─ prisma
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ prisma.test.ts
│  │     │  ├─ pwsh
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pwsh.test.ts
│  │     │  ├─ renovate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ renovate.test.ts
│  │     │  ├─ ripgrep
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ ripgrep.test.ts
│  │     │  ├─ sentry-cli
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sentry_cli.test.ts
│  │     │  ├─ sfdx
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sfdx.test.ts
│  │     │  ├─ sourcery
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sourcery.test.ts
│  │     │  ├─ tailwindcss
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tailwindcss.test.ts
│  │     │  ├─ target-determinator
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ target_determinator.test.ts
│  │     │  ├─ terraform
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform.test.ts
│  │     │  ├─ terraform-docs
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform_docs.test.ts
│  │     │  ├─ terraform-switcher
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform_switcher.test.ts
│  │     │  ├─ terraformer
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraformer.test.ts
│  │     │  ├─ terramate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terramate.test.ts
│  │     │  ├─ tfmigrate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfmigrate.test.ts
│  │     │  ├─ tfnotify
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfnotify.test.ts
│  │     │  ├─ tfupdate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfupdate.test.ts
│  │     │  ├─ tofu
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tofu.test.ts
│  │     │  ├─ tree-sitter
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tree_sitter.test.ts
│  │     │  ├─ ts-node
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ ts_node.test.ts
│  │     │  ├─ tsc
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tsc.test.ts
│  │     │  ├─ webpack
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ webpack.test.ts
│  │     │  ├─ yarn
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ yarn.test.ts
│  │     │  └─ yq
│  │     │     ├─ plugin.yaml
│  │     │     └─ yq.test.ts
│  │     ├─ trunk.ps1
│  │     └─ tsconfig.json
│  ├─ tools
│  │  ├─ bandit
│  │  ├─ black
│  │  ├─ checkov
│  │  ├─ isort
│  │  ├─ markdownlint
│  │  ├─ osv-scanner
│  │  ├─ prettier
│  │  ├─ ruff
│  │  ├─ trufflehog
│  │  ├─ trunk
│  │  └─ yamllint
│  └─ trunk.yaml
├─ LICENSE
├─ README.md
├─ agentic_research
│  ├─ .DS_Store
│  ├─ __init__.py
│  ├─ collaborative_storm
│  │  ├─ .DS_Store
│  │  ├─ __init__.py
│  │  ├─ discourse_manager.py
│  │  ├─ lm_configs.py
│  │  ├─ modules
│  │  │  ├─ __init__.py
│  │  │  ├─ article_generation.py
│  │  │  ├─ callback.py
│  │  │  ├─ co_storm_agents.py
│  │  │  ├─ collaborative_storm_utils.py
│  │  │  ├─ costorm_expert_utterance_generator.py
│  │  │  ├─ expert_generation.py
│  │  │  ├─ grounded_question_answering.py
│  │  │  ├─ grounded_question_generation.py
│  │  │  ├─ information_insertion_module.py
│  │  │  ├─ knowledge_base_summary.py
│  │  │  ├─ simulate_user.py
│  │  │  └─ warmstart_hierarchical_chat.py
│  │  ├─ runner.py
│  │  ├─ runner_args.py
│  │  └─ turn_policy.py
│  ├─ dataclass.py
│  ├─ encoder.py
│  ├─ interface.py
│  ├─ lm.py
│  ├─ logging_wrapper.py
│  ├─ rm.py
│  ├─ storm_analysis
│  │  ├─ .DS_Store
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
│  ├─ test_engine.py
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
│  │  ├─ test_coder_agent.py
│  │  └─ utils.py
│  ├─ communication.py
│  ├─ main.py
│  ├─ models
│  │  └─ shared.py
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ repo_map.py
│  ├─ server.py
│  └─ utils.py
├─ docs
│  ├─ 00_Original_reference-docs
│  │  ├─ old-ar-README.md
│  │  ├─ old-cp-README.md
│  │  └─ old_cp_breakdown.md
│  ├─ 01_Project_Overview
│  │  └─ file_tree_map.md
│  ├─ 02_Phase1_Backend_Integration
│  │  ├─ setup_guide_agentic_reasoning.md
│  │  └─ setup_progress.md
│  ├─ Integration-guide
│  │  ├─ .editorconfig
│  │  ├─ Integration-study-Merging-AI-Codepilot,.md
│  │  ├─ README.md
│  │  ├─ cloud-deployment-strategy
│  │  │  └─ security-networking.md
│  │  ├─ deepresearch.md
│  │  ├─ git-and-doc-strategy.md
│  │  ├─ index.md
│  │  └─ summary.md
│  ├─ coder_agent_integration.md
│  ├─ documentation-rules.md
│  ├─ graphrag_compatibility_solutions.md
│  ├─ integration-status.md
│  ├─ integration_guardrails.md
│  ├─ intelligentcontextretrieval.md
│  └─ websocket_visualization.md
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
│  │  ├─ DiffViewer.svelte
│  │  ├─ app.css
│  │  ├─ main.js
│  │  └─ vite-env.d.ts
│  ├─ svelte.config.js
│  └─ vite.config.js
├─ memgraph-platform
│  └─ docker-compose.yml
├─ nano-graphrag
│  ├─ .coveragerc
│  ├─ LICENSE
│  ├─ MANIFEST.in
│  ├─ docs
│  │  ├─ CONTRIBUTING.md
│  │  ├─ FAQ.md
│  │  ├─ ROADMAP.md
│  │  ├─ benchmark-dspy-entity-extraction.md
│  │  ├─ benchmark-en.md
│  │  ├─ benchmark-zh.md
│  │  └─ use_neo4j_for_graphrag.md
│  ├─ examples
│  │  ├─ benchmarks
│  │  │  ├─ dspy_entity.py
│  │  │  ├─ eval_naive_graphrag_on_multi_hop.ipynb
│  │  │  ├─ hnsw_vs_nano_vector_storage.py
│  │  │  └─ md5_vs_xxhash.py
│  │  ├─ finetune_entity_relationship_dspy.ipynb
│  │  ├─ generate_entity_relationship_dspy.ipynb
│  │  ├─ graphml_visualize.py
│  │  ├─ no_openai_key_at_all.py
│  │  ├─ using_amazon_bedrock.py
│  │  ├─ using_custom_chunking_method.py
│  │  ├─ using_deepseek_api_as_llm+glm_api_as_embedding.py
│  │  ├─ using_deepseek_as_llm.py
│  │  ├─ using_dspy_entity_extraction.py
│  │  ├─ using_faiss_as_vextorDB.py
│  │  ├─ using_hnsw_as_vectorDB.py
│  │  ├─ using_llm_api_as_llm+ollama_embedding.py
│  │  ├─ using_local_embedding_model.py
│  │  ├─ using_milvus_as_vectorDB.py
│  │  ├─ using_ollama_as_llm.py
│  │  └─ using_ollama_as_llm_and_embedding.py
│  ├─ nano_graphrag
│  │  ├─ __init__.py
│  │  ├─ _llm.py
│  │  ├─ _op.py
│  │  ├─ _splitter.py
│  │  ├─ _storage
│  │  │  ├─ __init__.py
│  │  │  ├─ gdb_neo4j.py
│  │  │  ├─ gdb_networkx.py
│  │  │  ├─ kv_json.py
│  │  │  ├─ vdb_hnswlib.py
│  │  │  └─ vdb_nanovectordb.py
│  │  ├─ _utils.py
│  │  ├─ base.py
│  │  ├─ entity_extraction
│  │  │  ├─ __init__.py
│  │  │  ├─ extract.py
│  │  │  ├─ metric.py
│  │  │  └─ module.py
│  │  ├─ graphrag.py
│  │  └─ prompt.py
│  ├─ nano_graphrag_cache_2025-02-19-23:51:49
│  ├─ nano_graphrag_cache_2025-02-20-00:02:28
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:03:47
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:03:54
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:05:36
│  ├─ nano_graphrag_cache_2025-02-20-00:06:14
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:06:43
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:06:47
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:09:02
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:09:30
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:09:44
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:11:06
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:11:33
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:11:36
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:14:52
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:15:30
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:15:34
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:19:29
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:19:51
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:20:20
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:21:45
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:22:30
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-20-00:22:42
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-03:18:45
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-03:19:07
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-03:19:10
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-04:06:36
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-04:06:54
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ nano_graphrag_cache_2025-02-21-04:06:59
│  │  ├─ graph_chunk_entity_relation.graphml
│  │  ├─ kv_store_community_reports.json
│  │  ├─ kv_store_full_docs.json
│  │  ├─ kv_store_llm_response_cache.json
│  │  ├─ kv_store_text_chunks.json
│  │  └─ vdb_entities.json
│  ├─ readme.md
│  ├─ requirements-dev.txt
│  ├─ requirements.txt
│  ├─ setup.py
│  └─ tests
│     ├─ __init__.py
│     ├─ entity_extraction
│     │  ├─ __init__.py
│     │  ├─ test_extract.py
│     │  ├─ test_metric.py
│     │  └─ test_module.py
│     ├─ fixtures
│     │  └─ mock_cache.json
│     ├─ mock_data.txt
│     ├─ test_graphrag.py
│     ├─ test_hnsw_vector_storage.py
│     ├─ test_json_parsing.py
│     ├─ test_neo4j_storage.py
│     ├─ test_networkx_storage.py
│     ├─ test_o.py
│     ├─ test_openai.py
│     ├─ test_rag.py
│     ├─ test_splitter.py
│     └─ zhuyuanzhang.txt
├─ nano_graphrag_cache_2025-02-21-04:20:58
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-04:21:16
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-04:21:19
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:07:45
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:08:08
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:08:21
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:25:06
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:25:29
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ nano_graphrag_cache_2025-02-21-05:25:32
│  ├─ graph_chunk_entity_relation.graphml
│  ├─ kv_store_community_reports.json
│  ├─ kv_store_full_docs.json
│  ├─ kv_store_llm_response_cache.json
│  ├─ kv_store_text_chunks.json
│  └─ vdb_entities.json
├─ package-lock.json
├─ pytest.ini
├─ requirements.txt
├─ scripts
│  ├─ __init__.py
│  ├─ agentic_ds.py
│  ├─ agentic_reason
│  │  ├─ __init__.py
│  │  ├─ cache.py
│  │  ├─ config.py
│  │  ├─ context_manager.py
│  │  ├─ data_loader.py
│  │  ├─ generation.py
│  │  ├─ knowledge_synthesizer.py
│  │  ├─ models.py
│  │  ├─ prompt_manager.py
│  │  ├─ reasoning_validator.py
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
│  │  │  ├─ compute_test_output_prediction_metrics.py
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
│  ├─ minimal_discourse_manager.py
│  ├─ minimal_lm_configs.py
│  ├─ project_context.txt
│  ├─ prompts.py
│  ├─ quicksum.py
│  ├─ run_agentic_reason.py
│  ├─ test_agentic_reasoning.py
│  ├─ test_minimal.py
│  ├─ test_qdrant_store.py
│  ├─ test_utils.py
│  ├─ tools
│  │  ├─ __init__.py
│  │  ├─ bing_search.py
│  │  ├─ creat_graph.py
│  │  ├─ duck_search.py
│  │  ├─ run_code.py
│  │  ├─ run_search.py
│  │  └─ temp.py
│  └─ utils
│     ├─ math_equivalence.py
│     └─ remote_llm.py
├─ setup.py
├─ temp.py
├─ tests
│  ├─ kv_store_llm_response_cache.json
│  ├─ nano_graphrag_cache_TEST
│  └─ test_discourse_manager.py
├─ tokenizers-main
│  ├─ .DS_Store
│  ├─ CITATION.cff
│  ├─ LICENSE
│  ├─ README.md
│  ├─ RELEASE.md
│  ├─ bindings
│  │  ├─ node
│  │  │  ├─ .cargo
│  │  │  │  └─ config.toml
│  │  │  ├─ .editorconfig
│  │  │  ├─ .eslintrc.yml
│  │  │  ├─ .prettierignore
│  │  │  ├─ .taplo.toml
│  │  │  ├─ .yarn
│  │  │  │  └─ releases
│  │  │  │     └─ yarn-3.5.1.cjs
│  │  │  ├─ .yarnrc.yml
│  │  │  ├─ Cargo.toml
│  │  │  ├─ LICENSE
│  │  │  ├─ Makefile
│  │  │  ├─ README.md
│  │  │  ├─ build.rs
│  │  │  ├─ examples
│  │  │  │  └─ documentation
│  │  │  │     ├─ pipeline.test.ts
│  │  │  │     └─ quicktour.test.ts
│  │  │  ├─ index.d.ts
│  │  │  ├─ index.js
│  │  │  ├─ jest.config.js
│  │  │  ├─ npm
│  │  │  │  ├─ android-arm-eabi
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ android-arm64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ darwin-arm64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ darwin-x64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ freebsd-x64
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-arm-gnueabihf
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-arm64-gnu
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-arm64-musl
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-x64-gnu
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ linux-x64-musl
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ win32-arm64-msvc
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  ├─ win32-ia32-msvc
│  │  │  │  │  ├─ README.md
│  │  │  │  │  └─ package.json
│  │  │  │  └─ win32-x64-msvc
│  │  │  │     ├─ README.md
│  │  │  │     └─ package.json
│  │  │  ├─ package.json
│  │  │  ├─ rustfmt.toml
│  │  │  ├─ src
│  │  │  │  ├─ arc_rwlock_serde.rs
│  │  │  │  ├─ decoders.rs
│  │  │  │  ├─ encoding.rs
│  │  │  │  ├─ lib.rs
│  │  │  │  ├─ models.rs
│  │  │  │  ├─ normalizers.rs
│  │  │  │  ├─ pre_tokenizers.rs
│  │  │  │  ├─ processors.rs
│  │  │  │  ├─ tasks
│  │  │  │  │  ├─ mod.rs
│  │  │  │  │  ├─ models.rs
│  │  │  │  │  └─ tokenizer.rs
│  │  │  │  ├─ tokenizer.rs
│  │  │  │  ├─ trainers.rs
│  │  │  │  └─ utils.rs
│  │  │  ├─ tsconfig.json
│  │  │  ├─ types.ts
│  │  │  └─ yarn.lock
│  │  └─ python
│  │     ├─ .cargo
│  │     │  └─ config.toml
│  │     ├─ CHANGELOG.md
│  │     ├─ Cargo.toml
│  │     ├─ MANIFEST.in
│  │     ├─ Makefile
│  │     ├─ README.md
│  │     ├─ benches
│  │     │  └─ test_tiktoken.py
│  │     ├─ conftest.py
│  │     ├─ examples
│  │     │  ├─ custom_components.py
│  │     │  ├─ example.py
│  │     │  ├─ train_bert_wordpiece.py
│  │     │  ├─ train_bytelevel_bpe.py
│  │     │  ├─ train_with_datasets.py
│  │     │  └─ using_the_visualizer.ipynb
│  │     ├─ py_src
│  │     │  └─ tokenizers
│  │     │     ├─ __init__.py
│  │     │     ├─ __init__.pyi
│  │     │     ├─ decoders
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ implementations
│  │     │     │  ├─ __init__.py
│  │     │     │  ├─ base_tokenizer.py
│  │     │     │  ├─ bert_wordpiece.py
│  │     │     │  ├─ byte_level_bpe.py
│  │     │     │  ├─ char_level_bpe.py
│  │     │     │  ├─ sentencepiece_bpe.py
│  │     │     │  └─ sentencepiece_unigram.py
│  │     │     ├─ models
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ normalizers
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ pre_tokenizers
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ processors
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __init__.pyi
│  │     │     ├─ tools
│  │     │     │  ├─ __init__.py
│  │     │     │  ├─ visualizer-styles.css
│  │     │     │  └─ visualizer.py
│  │     │     └─ trainers
│  │     │        ├─ __init__.py
│  │     │        └─ __init__.pyi
│  │     ├─ pyproject.toml
│  │     ├─ rust-toolchain
│  │     ├─ scripts
│  │     │  ├─ convert.py
│  │     │  ├─ sentencepiece_extractor.py
│  │     │  └─ spm_parity_check.py
│  │     ├─ setup.cfg
│  │     ├─ src
│  │     │  ├─ decoders.rs
│  │     │  ├─ encoding.rs
│  │     │  ├─ error.rs
│  │     │  ├─ lib.rs
│  │     │  ├─ models.rs
│  │     │  ├─ normalizers.rs
│  │     │  ├─ pre_tokenizers.rs
│  │     │  ├─ processors.rs
│  │     │  ├─ token.rs
│  │     │  ├─ tokenizer.rs
│  │     │  ├─ trainers.rs
│  │     │  └─ utils
│  │     │     ├─ iterators.rs
│  │     │     ├─ mod.rs
│  │     │     ├─ normalization.rs
│  │     │     ├─ pretokenization.rs
│  │     │     ├─ regex.rs
│  │     │     └─ serde_pyo3.rs
│  │     ├─ stub.py
│  │     ├─ test.txt
│  │     └─ tests
│  │        ├─ __init__.py
│  │        ├─ bindings
│  │        │  ├─ __init__.py
│  │        │  ├─ test_decoders.py
│  │        │  ├─ test_encoding.py
│  │        │  ├─ test_models.py
│  │        │  ├─ test_normalizers.py
│  │        │  ├─ test_pre_tokenizers.py
│  │        │  ├─ test_processors.py
│  │        │  ├─ test_tokenizer.py
│  │        │  └─ test_trainers.py
│  │        ├─ documentation
│  │        │  ├─ __init__.py
│  │        │  ├─ test_pipeline.py
│  │        │  ├─ test_quicktour.py
│  │        │  └─ test_tutorial_train_from_iterators.py
│  │        ├─ implementations
│  │        │  ├─ __init__.py
│  │        │  ├─ test_base_tokenizer.py
│  │        │  ├─ test_bert_wordpiece.py
│  │        │  ├─ test_byte_level_bpe.py
│  │        │  ├─ test_char_bpe.py
│  │        │  └─ test_sentencepiece.py
│  │        ├─ test_serialization.py
│  │        └─ utils.py
│  ├─ docs
│  │  ├─ Makefile
│  │  ├─ README.md
│  │  ├─ source
│  │  │  ├─ _ext
│  │  │  │  ├─ entities.py
│  │  │  │  ├─ rust_doc.py
│  │  │  │  └─ toctree_tags.py
│  │  │  ├─ _static
│  │  │  │  ├─ css
│  │  │  │  │  ├─ Calibre-Light.ttf
│  │  │  │  │  ├─ Calibre-Medium.otf
│  │  │  │  │  ├─ Calibre-Regular.otf
│  │  │  │  │  ├─ Calibre-Thin.otf
│  │  │  │  │  ├─ code-snippets.css
│  │  │  │  │  └─ huggingface.css
│  │  │  │  └─ js
│  │  │  │     └─ custom.js
│  │  │  ├─ api
│  │  │  │  ├─ node.inc
│  │  │  │  ├─ python.inc
│  │  │  │  ├─ reference.rst
│  │  │  │  └─ rust.inc
│  │  │  ├─ components.rst
│  │  │  ├─ conf.py
│  │  │  ├─ entities.inc
│  │  │  ├─ index.rst
│  │  │  ├─ installation
│  │  │  │  ├─ main.rst
│  │  │  │  ├─ node.inc
│  │  │  │  ├─ python.inc
│  │  │  │  └─ rust.inc
│  │  │  ├─ pipeline.rst
│  │  │  ├─ quicktour.rst
│  │  │  └─ tutorials
│  │  │     └─ python
│  │  │        └─ training_from_memory.rst
│  │  └─ source-doc-builder
│  │     ├─ _toctree.yml
│  │     ├─ api
│  │     │  ├─ added-tokens.mdx
│  │     │  ├─ decoders.mdx
│  │     │  ├─ encode-inputs.mdx
│  │     │  ├─ encoding.mdx
│  │     │  ├─ input-sequences.mdx
│  │     │  ├─ models.mdx
│  │     │  ├─ normalizers.mdx
│  │     │  ├─ post-processors.mdx
│  │     │  ├─ pre-tokenizers.mdx
│  │     │  ├─ tokenizer.mdx
│  │     │  ├─ trainers.mdx
│  │     │  └─ visualizer.mdx
│  │     ├─ components.mdx
│  │     ├─ index.mdx
│  │     ├─ installation.mdx
│  │     ├─ pipeline.mdx
│  │     ├─ quicktour.mdx
│  │     └─ training_from_memory.mdx
│  └─ tokenizers
│     ├─ CHANGELOG.md
│     ├─ Cargo.toml
│     ├─ LICENSE
│     ├─ Makefile
│     ├─ README.md
│     ├─ README.tpl
│     ├─ benches
│     │  ├─ bert_benchmark.rs
│     │  ├─ bpe_benchmark.rs
│     │  ├─ common
│     │  │  └─ mod.rs
│     │  ├─ layout_benchmark.rs
│     │  ├─ llama3.rs
│     │  └─ unigram_benchmark.rs
│     ├─ examples
│     │  ├─ encode_batch.rs
│     │  ├─ serialization.rs
│     │  └─ unstable_wasm
│     │     ├─ Cargo.toml
│     │     ├─ README.md
│     │     ├─ src
│     │     │  ├─ lib.rs
│     │     │  └─ utils.rs
│     │     ├─ tests
│     │     │  └─ web.rs
│     │     └─ www
│     │        ├─ .bin
│     │        │  └─ create-wasm-app.js
│     │        ├─ .travis.yml
│     │        ├─ LICENSE-APACHE
│     │        ├─ LICENSE-MIT
│     │        ├─ README.md
│     │        ├─ bootstrap.js
│     │        ├─ index.html
│     │        ├─ index.js
│     │        ├─ package-lock.json
│     │        ├─ package.json
│     │        └─ webpack.config.js
│     ├─ rust-toolchain
│     ├─ src
│     │  ├─ decoders
│     │  │  ├─ bpe.rs
│     │  │  ├─ byte_fallback.rs
│     │  │  ├─ ctc.rs
│     │  │  ├─ fuse.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ sequence.rs
│     │  │  ├─ strip.rs
│     │  │  └─ wordpiece.rs
│     │  ├─ lib.rs
│     │  ├─ models
│     │  │  ├─ bpe
│     │  │  │  ├─ mod.rs
│     │  │  │  ├─ model.rs
│     │  │  │  ├─ serialization.rs
│     │  │  │  ├─ trainer.rs
│     │  │  │  └─ word.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ unigram
│     │  │  │  ├─ lattice.rs
│     │  │  │  ├─ mod.rs
│     │  │  │  ├─ model.rs
│     │  │  │  ├─ serialization.rs
│     │  │  │  ├─ trainer.rs
│     │  │  │  └─ trie.rs
│     │  │  ├─ wordlevel
│     │  │  │  ├─ mod.rs
│     │  │  │  ├─ serialization.rs
│     │  │  │  └─ trainer.rs
│     │  │  └─ wordpiece
│     │  │     ├─ mod.rs
│     │  │     ├─ serialization.rs
│     │  │     └─ trainer.rs
│     │  ├─ normalizers
│     │  │  ├─ bert.rs
│     │  │  ├─ byte_level.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ precompiled.rs
│     │  │  ├─ prepend.rs
│     │  │  ├─ replace.rs
│     │  │  ├─ strip.rs
│     │  │  ├─ unicode.rs
│     │  │  └─ utils.rs
│     │  ├─ pre_tokenizers
│     │  │  ├─ bert.rs
│     │  │  ├─ byte_level.rs
│     │  │  ├─ delimiter.rs
│     │  │  ├─ digits.rs
│     │  │  ├─ metaspace.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ punctuation.rs
│     │  │  ├─ sequence.rs
│     │  │  ├─ split.rs
│     │  │  ├─ unicode_scripts
│     │  │  │  ├─ mod.rs
│     │  │  │  ├─ pre_tokenizer.rs
│     │  │  │  └─ scripts.rs
│     │  │  └─ whitespace.rs
│     │  ├─ processors
│     │  │  ├─ bert.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ roberta.rs
│     │  │  ├─ sequence.rs
│     │  │  └─ template.rs
│     │  ├─ tokenizer
│     │  │  ├─ added_vocabulary.rs
│     │  │  ├─ encoding.rs
│     │  │  ├─ mod.rs
│     │  │  ├─ normalizer.rs
│     │  │  ├─ pattern.rs
│     │  │  ├─ pre_tokenizer.rs
│     │  │  └─ serialization.rs
│     │  └─ utils
│     │     ├─ cache.rs
│     │     ├─ fancy.rs
│     │     ├─ from_pretrained.rs
│     │     ├─ iter.rs
│     │     ├─ mod.rs
│     │     ├─ onig.rs
│     │     ├─ padding.rs
│     │     ├─ parallelism.rs
│     │     ├─ progress.rs
│     │     └─ truncation.rs
│     └─ tests
│        ├─ added_tokens.rs
│        ├─ common
│        │  └─ mod.rs
│        ├─ documentation.rs
│        ├─ from_pretrained.rs
│        ├─ offsets.rs
│        ├─ serialization.rs
│        ├─ stream.rs
│        ├─ training.rs
│        └─ unigram.rs
├─ tree.md
└─ venv311
   ├─ bin
   │  ├─ Activate.ps1
   │  ├─ activate
   │  ├─ activate.csh
   │  ├─ activate.fish
   │  ├─ alembic
   │  ├─ chroma
   │  ├─ coloredlogs
   │  ├─ datasets-cli
   │  ├─ distro
   │  ├─ dotenv
   │  ├─ email_validator
   │  ├─ esprima
   │  ├─ f2py
   │  ├─ fastapi
   │  ├─ fastavro
   │  ├─ fonttools
   │  ├─ futurize
   │  ├─ get_gprof
   │  ├─ get_objgraph
   │  ├─ griffe
   │  ├─ gunicorn
   │  ├─ httpx
   │  ├─ huggingface-cli
   │  ├─ humanfriendly
   │  ├─ isympy
   │  ├─ jp.py
   │  ├─ json_repair
   │  ├─ jsonschema
   │  ├─ litellm
   │  ├─ mako-render
   │  ├─ markdown-it
   │  ├─ normalizer
   │  ├─ numba
   │  ├─ onnxruntime_test
   │  ├─ openai
   │  ├─ opentelemetry-bootstrap
   │  ├─ opentelemetry-instrument
   │  ├─ optuna
   │  ├─ pasteurize
   │  ├─ pip
   │  ├─ pip3
   │  ├─ pip3.11
   │  ├─ py.test
   │  ├─ pyftmerge
   │  ├─ pyftsubset
   │  ├─ pygmentize
   │  ├─ pyproject-build
   │  ├─ pyrsa-decrypt
   │  ├─ pyrsa-encrypt
   │  ├─ pyrsa-keygen
   │  ├─ pyrsa-priv2pub
   │  ├─ pyrsa-sign
   │  ├─ pyrsa-verify
   │  ├─ pytest
   │  ├─ python
   │  ├─ python3
   │  ├─ python3.11
   │  ├─ rq
   │  ├─ rqinfo
   │  ├─ rqworker
   │  ├─ tqdm
   │  ├─ ttx
   │  ├─ typer
   │  ├─ undill
   │  ├─ uvicorn
   │  ├─ watchfiles
   │  ├─ wheel
   │  └─ wsdump
   ├─ include
   │  └─ python3.11
   ├─ pyvenv.cfg
   └─ share
      └─ man
         └─ man1
            ├─ isympy.1
            └─ ttx.1

```
>>>>>>> merge-from-agenticgroking
