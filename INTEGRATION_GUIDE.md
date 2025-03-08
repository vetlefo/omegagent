# Agentic-Reasoning Integration Guide

This technical guide outlines the implementation steps for completing the integration of Agentic-Reasoning with AI Codepilot. It provides detailed instructions for developers working on the remaining integration components.

## 1. Integrating `agentic_research.encoder`

The `Encoder` class provides advanced embeddings for better semantic understanding of code and text. This integration enhances the repository mapping and search capabilities.

### Implementation Steps

1. **Create an Encoder Wrapper in `backend/utils.py`**:

```python
# Add to backend/utils.py
import os
from typing import List, Optional
from agentic_research.encoder import Encoder

class AgenticEncoderFunction:
    """Wrapper for Agentic-Reasoning's Encoder class for embeddings."""
    
    def __init__(self):
        """Initialize the encoder based on environment variables."""
        self.use_encoder = os.environ.get("USE_AGENTIC_ENCODER", "false").lower() == "true"
        
        if self.use_encoder:
            api_type = os.environ.get("ENCODER_API_TYPE", "openai")
            model_name = None
            
            if api_type == "openai":
                model_name = os.environ.get("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
            elif api_type == "azure":
                model_name = os.environ.get("AZURE_EMBEDDING_MODEL", "text-embedding-3-small")
            
            try:
                self.encoder = Encoder(api_type=api_type, model_name=model_name)
                print(f"Initialized Agentic Encoder with {api_type} API and model {model_name}")
            except Exception as e:
                print(f"Failed to initialize Agentic Encoder: {e}")
                self.use_encoder = False
                self.encoder = None
        else:
            self.encoder = None
    
    def get_embeddings(self, texts: List[str]) -> Optional[List[List[float]]]:
        """Get embeddings for a list of texts."""
        if not self.use_encoder or self.encoder is None:
            return None
            
        try:
            return self.encoder.get_embeddings(texts)
        except Exception as e:
            print(f"Error getting embeddings: {e}")
            return None
            
    def similarity(self, text1: str, text2: str) -> Optional[float]:
        """Calculate similarity between two texts."""
        if not self.use_encoder or self.encoder is None:
            return None
            
        try:
            return self.encoder.similarity(text1, text2)
        except Exception as e:
            print(f"Error calculating similarity: {e}")
            return None
```

2. **Enhance Search Functionality in `backend/utils.py`**:

```python
# Modify the existing get_relevant_snippets function in backend/utils.py
from typing import List, Dict, Any, Tuple
import chromadb
import backoff

# Initialize the encoder
agentic_encoder = AgenticEncoderFunction()

@backoff.on_exception(backoff.expo, Exception, max_tries=3)
def get_relevant_snippets(query: str, collection_name: str, n_results: int = 5) -> List[Dict[str, Any]]:
    """Get relevant code snippets using semantic search."""
    client = chromadb.Client()
    
    try:
        collection = client.get_collection(name=collection_name)
    except ValueError:
        print(f"Collection {collection_name} not found")
        return []
    
    # Use agentic encoder if available
    if agentic_encoder.use_encoder:
        # Get query embedding
        query_embedding = agentic_encoder.get_embeddings([query])[0]
        
        # Search using the embedding
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            include=["documents", "metadatas", "distances"]
        )
    else:
        # Fall back to standard search
        results = collection.query(
            query_texts=[query],
            n_results=n_results,
            include=["documents", "metadatas", "distances"]
        )
    
    # Process results
    snippets = []
    for i in range(len(results["documents"][0])):
        snippets.append({
            "content": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i] if "distances" in results else None
        })
    
    return snippets
```

3. **Update Repository Mapping in `backend/repo_map.py`**:

```python
# Add to backend/repo_map.py
import os
from typing import Dict, List, Optional, Set, Tuple
import pathspec
from agentic_research.encoder import Encoder

class RepoMap:
    # ... existing code ...
    
    def __init__(self, root_directory: str = ".", use_semantic_analysis: bool = False):
        """Initialize the repository mapper."""
        self.root_directory = os.path.abspath(root_directory)
        self.files = {}
        self.gitignore_spec = self._load_gitignore()
        self.use_semantic_analysis = use_semantic_analysis and os.environ.get("USE_SEMANTIC_ANALYSIS", "false").lower() == "true"
        
        # Initialize encoder for semantic analysis if enabled
        if self.use_semantic_analysis:
            api_type = os.environ.get("ENCODER_API_TYPE", "openai")
            model_name = None
            
            if api_type == "openai":
                model_name = os.environ.get("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
            elif api_type == "azure":
                model_name = os.environ.get("AZURE_EMBEDDING_MODEL", "text-embedding-3-small")
            
            try:
                self.encoder = Encoder(api_type=api_type, model_name=model_name)
                print(f"Initialized Semantic Analysis with {api_type} API and model {model_name}")
            except Exception as e:
                print(f"Failed to initialize Semantic Analysis: {e}")
                self.use_semantic_analysis = False
                self.encoder = None
        else:
            self.encoder = None
            
        # Store semantic relationships
        self.semantic_relationships = {}
    
    # ... existing code ...
    
    def analyze_semantic_relationships(self):
        """Analyze semantic relationships between code components."""
        if not self.use_semantic_analysis or self.encoder is None:
            return
            
        print("Analyzing semantic relationships between code components...")
        
        # Extract code components (functions, classes, etc.)
        components = []
        component_texts = []
        
        for file_path, file_info in self.files.items():
            if file_info.get("type") == "python":
                for func_name, func_info in file_info.get("functions", {}).items():
                    components.append({
                        "type": "function",
                        "name": func_name,
                        "file": file_path,
                        "signature": func_info.get("signature", "")
                    })
                    component_texts.append(func_info.get("signature", "") + "\n" + func_info.get("docstring", ""))
                
                for class_name, class_info in file_info.get("classes", {}).items():
                    components.append({
                        "type": "class",
                        "name": class_name,
                        "file": file_path,
                        "signature": class_info.get("signature", "")
                    })
                    class_text = class_info.get("signature", "") + "\n" + class_info.get("docstring", "")
                    
                    # Add method information
                    for method_name, method_info in class_info.get("methods", {}).items():
                        class_text += "\n" + method_info.get("signature", "") + "\n" + method_info.get("docstring", "")
                    
                    component_texts.append(class_text)
        
        # Get embeddings for all components
        try:
            embeddings = self.encoder.get_embeddings(component_texts)
            
            # Calculate similarities and store relationships
            for i in range(len(components)):
                self.semantic_relationships[f"{components[i]['type']}:{components[i]['name']}"] = []
                
                for j in range(len(components)):
                    if i != j:
                        similarity = self.encoder.similarity_from_embeddings(embeddings[i], embeddings[j])
                        
                        # Store relationships with similarity above threshold
                        if similarity > 0.7:  # Adjust threshold as needed
                            self.semantic_relationships[f"{components[i]['type']}:{components[i]['name']}"].append({
                                "type": components[j]['type'],
                                "name": components[j]['name'],
                                "file": components[j]['file'],
                                "similarity": similarity
                            })
            
            print(f"Analyzed {len(components)} components and found {sum(len(v) for v in self.semantic_relationships.values())} relationships")
        except Exception as e:
            print(f"Error analyzing semantic relationships: {e}")
    
    def build_map(self):
        """Build the repository map."""
        # ... existing code ...
        
        # After building the standard map, analyze semantic relationships if enabled
        if self.use_semantic_analysis and self.encoder is not None:
            self.analyze_semantic_relationships()
    
    def to_python_stub(self, include_semantic_relationships: bool = False):
        """Generate a Python-like stub of the repository structure."""
        # ... existing code ...
        
        # Add semantic relationships if requested
        if include_semantic_relationships and self.use_semantic_analysis and self.semantic_relationships:
            stub += "\n\n# Semantic Relationships\n"
            stub += "'''\n"
            
            for component, relationships in self.semantic_relationships.items():
                if relationships:
                    stub += f"{component} is related to:\n"
                    
                    for rel in sorted(relationships, key=lambda x: x['similarity'], reverse=True):
                        stub += f"  - {rel['type']}:{rel['name']} (in {rel['file']}) with similarity {rel['similarity']:.2f}\n"
                    
                    stub += "\n"
            
            stub += "'''\n"
        
        return stub
```

## 2. Integrating `agentic_research.collaborative_storm`

The CollaborativeStorm framework enables multiple specialized expert agents to analyze problems collaboratively. This integration enhances the orchestration capabilities.

### Implementation Steps

1. **Create a StormOrchestratorAgent in `backend/agents/storm_orchestrator_agent.py`**:

```python
# Create backend/agents/storm_orchestrator_agent.py
import os
import asyncio
from typing import List, Dict, Any, Optional
import pydantic_ai
from pydantic_ai.result import StreamedRunResult
from backend.agents.orchestrator_agent import OrchestratorAgent
from backend.agents.utils import send_usage
from agentic_research.collaborative_storm.engine import CollaborativeStormEngine
from agentic_research.collaborative_storm.modules.co_storm_agents import ExpertAgent

class StormOrchestratorAgent(OrchestratorAgent):
    """Enhanced orchestrator agent that uses CollaborativeStorm for reasoning."""
    
    def __init__(
        self, 
        repo_stub: str, 
        comm, 
        review: bool = True, 
        max_iterations: int = 1, 
        root_directory: str = ".",
        use_storm: bool = True,
        include_semantic_relationships: bool = False,
        use_mcp: bool = False,
        use_ollama: bool = False
    ):
        """Initialize the StormOrchestratorAgent."""
        super().__init__(repo_stub, comm, review, max_iterations, root_directory)
        
        self.use_storm = use_storm
        self.include_semantic_relationships = include_semantic_relationships
        self.use_mcp = use_mcp
        self.use_ollama = use_ollama
        
        # Initialize CollaborativeStorm engine if enabled
        if self.use_storm:
            try:
                self.storm_engine = CollaborativeStormEngine()
                
                # Define expert agents
                self.experts = [
                    ExpertAgent(name="CodeArchitect", expertise="software architecture and design patterns"),
                    ExpertAgent(name="SecurityExpert", expertise="code security and vulnerability detection"),
                    ExpertAgent(name="PerformanceOptimizer", expertise="code performance and optimization"),
                    ExpertAgent(name="TestingSpecialist", expertise="software testing and quality assurance")
                ]
                
                print("Initialized CollaborativeStorm engine with expert agents")
            except Exception as e:
                print(f"Failed to initialize CollaborativeStorm engine: {e}")
                self.use_storm = False
                self.storm_engine = None
        else:
            self.storm_engine = None
    
    async def run(self, user_prompt: str) -> None:
        """Run the orchestration process with CollaborativeStorm if enabled."""
        if not self.use_storm or self.storm_engine is None:
            # Fall back to standard orchestration
            await super().run(user_prompt)
            return
        
        await self.comm.send("log", "Starting orchestration with CollaborativeStorm...")
        
        # Step 1: Generate a plan using CollaborativeStorm
        await self.comm.send("log", "Generating plan with expert collaboration...")
        
        try:
            # Prepare context for the experts
            context = f"""
            Repository Structure:
            {self.repo_stub}
            
            User Request:
            {user_prompt}
            """
            
            # Run collaborative planning
            plan_result = self.storm_engine.run_collaborative_session(
                context=context,
                experts=self.experts,
                task="Analyze this repository and user request, then create a detailed plan for implementing the requested changes.",
                max_turns=3
            )
            
            # Extract the plan from the collaborative session
            plan_text = plan_result.get("final_output", "")
            
            # Parse the plan into tasks
            tasks = self.planner_agent.parse_plan(plan_text)
            
            await self.comm.send("log", f"Generated plan with {len(tasks)} tasks")
            
            # Step 2: Execute the plan (similar to standard orchestration)
            iteration = 0
            while iteration < self.max_iterations and tasks:
                iteration += 1
                await self.comm.send("log", f"Starting iteration {iteration}/{self.max_iterations}")
                
                # Process each task in the plan
                for i, task in enumerate(tasks):
                    await self.comm.send("log", f"Processing task {i+1}/{len(tasks)}: {task.description}")
                    
                    # Get relevant files for the task
                    relevant_files = await self.get_relevant_files(task.description)
                    
                    # Generate code updates
                    updates = await self.generate_code_updates(task, relevant_files)
                    
                    # Apply and review updates
                    await self.apply_and_review_updates(updates)
                
                # Check if we need another iteration
                if iteration < self.max_iterations:
                    # Generate a new plan based on what's been done
                    await self.comm.send("log", f"Completed iteration {iteration}. Generating new plan...")
                    
                    # Use CollaborativeStorm to analyze the current state and generate a new plan
                    updated_context = f"""
                    Repository Structure:
                    {self.repo_stub}
                    
                    User Request:
                    {user_prompt}
                    
                    Completed Tasks:
                    {self._format_completed_tasks(tasks)}
                    
                    What additional tasks should be performed to complete the user's request?
                    """
                    
                    new_plan_result = self.storm_engine.run_collaborative_session(
                        context=updated_context,
                        experts=self.experts,
                        task="Analyze the current state and determine what additional tasks are needed.",
                        max_turns=2
                    )
                    
                    new_plan_text = new_plan_result.get("final_output", "")
                    tasks = self.planner_agent.parse_plan(new_plan_text)
                    
                    if not tasks:
                        await self.comm.send("log", "No additional tasks needed. Orchestration complete.")
                        break
                    
                    await self.comm.send("log", f"Generated new plan with {len(tasks)} additional tasks")
            
            await self.comm.send("log", "Orchestration with CollaborativeStorm completed successfully")
            
        except Exception as e:
            await self.comm.send("error", f"Error in StormOrchestratorAgent: {str(e)}")
            raise
    
    def _format_completed_tasks(self, tasks: List[Any]) -> str:
        """Format completed tasks for context."""
        formatted = ""
        for i, task in enumerate(tasks):
            formatted += f"{i+1}. {task.description}\n"
        return formatted
```

2. **Update the Server to Support StormOrchestratorAgent**:

This has already been implemented in the current `backend/server.py` file.

## 3. Implementing Ollama Integration

The Ollama integration connects to a locally running Ollama server for LLM inference, reducing API costs and providing offline capabilities.

### Implementation Steps

1. **Create an OllamaClient in `scripts/tools/ollama_client.py`**:

```python
# Create scripts/tools/ollama_client.py
import os
import json
import requests
from typing import List, Dict, Any, Optional, Union

class OllamaClient:
    """Client for interacting with a local Ollama server."""
    
    def __init__(self, base_url: str = "http://localhost:11434"):
        """Initialize the Ollama client."""
        self.base_url = base_url
        self.model = os.environ.get("OLLAMA_MODEL", "llama3")
        self.api_endpoint = f"{self.base_url}/api/generate"
        
        # Verify connection
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            if response.status_code == 200:
                available_models = [model["name"] for model in response.json().get("models", [])]
                if self.model not in available_models:
                    print(f"Warning: Model {self.model} not found in Ollama. Available models: {available_models}")
                else:
                    print(f"Successfully connected to Ollama server with model {self.model}")
            else:
                print(f"Warning: Could not connect to Ollama server at {self.base_url}")
        except Exception as e:
            print(f"Error connecting to Ollama server: {e}")
    
    def generate(
        self, 
        prompts: List[str], 
        temperature: float = 0.7, 
        top_p: float = 0.9, 
        top_k: int = 40, 
        repetition_penalty: float = 1.1, 
        max_tokens: int = 2048
    ) -> List[Any]:
        """Generate text completions for a list of prompts."""
        outputs = []
        
        for prompt in prompts:
            try:
                payload = {
                    "model": self.model,
                    "prompt": prompt,
                    "temperature": temperature,
                    "top_p": top_p,
                    "top_k": top_k,
                    "repeat_penalty": repetition_penalty,
                    "num_predict": max_tokens,
                    "stream": False
                }
                
                response = requests.post(self.api_endpoint, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Create a response object similar to vllm's output format
                    output = type('OllamaOutput', (), {})()
                    output.outputs = [type('OllamaOutputText', (), {'text': result.get('response', '')})]
                    
                    # Add usage tracking
                    output.usage = lambda: type('OllamaUsage', (), {
                        'request_tokens': result.get('prompt_eval_count', 0),
                        'response_tokens': result.get('eval_count', 0)
                    })
                    
                    outputs.append(output)
                else:
                    print(f"Error from Ollama API: {response.text}")
                    # Create an error output
                    output = type('OllamaOutput', (), {})()
                    output.outputs = [type('OllamaOutputText', (), {'text': f"Error: {response.text}"})]
                    output.usage = lambda: type('OllamaUsage', (), {'request_tokens': 0, 'response_tokens': 0})
                    outputs.append(output)
            
            except Exception as e:
                print(f"Error generating with Ollama: {e}")
                # Create an error output
                output = type('OllamaOutput', (), {})()
                output.outputs = [type('OllamaOutputText', (), {'text': f"Error: {str(e)}"})]
                output.usage = lambda: type('OllamaUsage', (), {'request_tokens': 0, 'response_tokens': 0})
                outputs.append(output)
        
        return outputs
    
    def chat(self, prompt: str, temperature: float = 0.7, max_tokens: int = 2048) -> Any:
        """Generate a chat completion for a single prompt."""
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "temperature": temperature,
                "num_predict": max_tokens,
                "stream": False
            }
            
            response = requests.post(self.api_endpoint, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                
                # Create a response object
                output = type('OllamaOutput', (), {})()
                output.content = result.get('response', '')
                
                # Add usage tracking
                output.usage = lambda: type('OllamaUsage', (), {
                    'request_tokens': result.get('prompt_eval_count', 0),
                    'response_tokens': result.get('eval_count', 0)
                })
                
                return output
            else:
                print(f"Error from Ollama API: {response.text}")
                return f"Error: {response.text}"
        
        except Exception as e:
            print(f"Error chatting with Ollama: {e}")
            return f"Error: {str(e)}"
```

## 4. Implementing Model Control Protocol (MCP)

The Model Control Protocol provides a unified interface for different LLM providers with automatic fallback capabilities.

### Implementation Steps

1. **Create an MCPTool in `scripts/tools/mcp_tool.py`**:

```python
# Create scripts/tools/mcp_tool.py
import os
import time
from typing import Dict, List, Any, Optional, Union
from utils.remote_llm import RemoteAPILLM

class MCPTool:
    """Model Control Protocol tool for unified LLM access with fallback."""
    
    def __init__(self):
        """Initialize the MCP tool."""
        self.use_mcp = os.environ.get("USE_MCP", "false").lower() == "true"
        
        if not self.use_mcp:
            print("MCP is disabled. Set USE_MCP=true to enable.")
            return
        
        # Configure providers
        self.primary_provider = os.environ.get("MCP_PRIMARY_PROVIDER", "openai")
        self.primary_model = os.environ.get("MCP_PRIMARY_MODEL", "gpt-4o")
        
        self.fallback_provider = os.environ.get("MCP_FALLBACK_PROVIDER", "ollama")
        self.fallback_model = os.environ.get("MCP_FALLBACK_MODEL", "llama3")
        
        # Initialize providers
        self.providers = {}
        
        # Initialize OpenAI provider if needed
        if self.primary_provider == "openai" or self.fallback_provider == "openai":
            self.providers["openai"] = RemoteAPILLM(model_name=self.primary_model if self.primary_provider == "openai" else self.fallback_model)
        
        # Initialize Ollama provider if needed
        if self.primary_provider == "ollama" or self.fallback_provider == "ollama":
            try:
                from scripts.tools.ollama_client import OllamaClient
                self.providers["ollama"] = OllamaClient()
            except Exception as e:
                print(f"Failed to initialize Ollama provider: {e}")
                if self.primary_provider == "ollama":
                    print("Falling back to OpenAI as primary provider")
                    self.primary_provider = "openai"
        
        # Initialize performance tracking
        self.performance_metrics = {
            "openai": {"success": 0, "failure": 0, "latency": []},
            "ollama": {"success": 0, "failure": 0, "latency": []}
        }
        
        print(f"Initialized MCP with primary provider {self.primary_provider} ({self.primary_model}) and fallback provider {self.fallback_provider} ({self.fallback_model})")
    
    def generate(
        self, 
        prompts: List[str], 
        temperature: float = 0.7, 
        max_tokens: int = 2048,
        **kwargs
    ) -> List[Any]:
        """Generate text completions with automatic fallback."""
        if not self.use_mcp:
            # Fall back to direct RemoteAPILLM call
            llm = RemoteAPILLM(model_name=self.primary_model)
            return llm.generate(prompts, temperature=temperature, max_tokens=max_tokens, **kwargs)
        
        # Try primary provider first
        primary_provider = self.providers.get(self.primary_provider)
        if not primary_provider:
            print(f"Primary provider {self.primary_provider} not available")
            # Try fallback provider
            fallback_provider = self.providers.get(self.fallback_provider)
            if not fallback_provider:
                print(f"Fallback provider {self.fallback_provider} not available")
                # Fall back to direct RemoteAPILLM call
                llm = RemoteAPILLM(model_name=self.primary_model)
                return llm.generate(prompts, temperature=temperature, max_tokens=max_tokens, **kwargs)
            return self._generate_with_provider(self.fallback_provider, fallback_provider, prompts, temperature, max_tokens, **kwargs)
        
        # Try with primary provider
        try:
            start_time = time.time()
            outputs = primary_provider.generate(prompts, temperature=temperature, max_tokens=max_tokens, **kwargs)
            latency = time.time() - start_time
            
            # Update metrics
            self.performance_metrics[self.primary_provider]["success"] += 1
            self.performance_metrics[self.primary_provider]["latency"].append(latency)
            
            return outputs
        except Exception as e:
            print(f"Error with primary provider {self.primary_provider}: {e}")
            # Update metrics
            self.performance_metrics[self.primary_provider]["failure"] += 1
            
            # Try fallback provider
            fallback_provider = self.providers.get(self.fallback_provider)
            if not fallback_provider:
                print(f"Fallback provider {self.fallback_provider} not available")
                raise
            
            return self._generate_with_provider(self.fallback_provider, fallback_provider, prompts, temperature, max_tokens, **kwargs)
    
    def _generate_with_provider(
        self, 
        provider_name: str, 
        provider: Any, 
        prompts: List[str], 
        temperature: float, 
        max_tokens: int,
        **kwargs
    ) -> List[Any]:
        """Generate with a specific provider and track metrics."""
        try:
            start_time = time.time()
            outputs = provider.generate(prompts, temperature=temperature, max_tokens=max_tokens, **kwargs)
            latency = time.time() - start_time
            
            # Update metrics
            self.performance_metrics[provider_name]["success"] += 1
            self.performance_metrics[provider_name]["latency"].append(latency)
            
            return outputs
        except Exception as e:
            print(f"Error with provider {provider_name}: {e}")
            # Update metrics
            self.performance_metrics[provider_name]["failure"] += 1
            raise
    
    def chat(
        self, 
        prompt: str, 
        temperature: float = 0.7, 
        max_tokens: int = 2048,
        **kwargs
    ) -> Any:
        """Generate a chat completion with automatic fallback."""
        if not self.use_mcp:
            # Fall back to direct RemoteAPILLM call
            llm = RemoteAPILLM(model_name=self.primary_model)
            return llm.chat(prompt, temperature=temperature, max_tokens=max_tokens, **kwargs)
        
        # Try primary provider first
        primary_provider = self.providers.get(self.primary_provider)
        if not primary_provider:
            print(f"Primary provider {self.primary_provider} not available")
            # Try fallback provider
            fallback_provider = self.providers.get(self.fallback_provider)
            if not fallback_provider:
                print(f"Fallback provider {self.fallback_provider} not available")
                # Fall back to direct RemoteAPILLM call
                llm = RemoteAPILLM(model_name=self.primary_model)
                return llm.chat(prompt, temperature=temperature, max_tokens=max_tokens, **kwargs)
            return self._chat_with_provider(self.fallback_provider, fallback_provider, prompt, temperature, max_tokens, **kwargs)
        
        # Try with primary provider
        try:
            start_time = time.time()
            output = primary_provider.chat(prompt, temperature=temperature, max_tokens=max_tokens, **kwargs)
            latency = time.time() - start_time
            
            # Update metrics
            self.performance_metrics[self.primary_provider]["success"] += 1
            self.performance_metrics[self.primary_provider]["latency"].append(latency)
            
            return output
        except Exception as e:
            print(f"Error with primary provider {self.primary_provider}: {e}")
            # Update metrics
            self.performance_metrics[self.primary_provider]["failure"] += 1
            
            # Try fallback provider
            fallback_provider = self.providers.get(self.fallback_provider)
            if not fallback_provider:
                print(f"Fallback provider {self.fallback_provider} not available")
                raise
            
            return self._chat_with_provider(self.fallback_provider, fallback_provider, prompt, temperature, max_tokens, **kwargs)
    
    def _chat_with_provider(
        self, 
        provider_name: str, 
        provider: Any, 
        prompt: str, 
        temperature: float, 
        max_tokens: int,
        **kwargs
    ) -> Any:
        """Chat with a specific provider and track metrics."""
        try:
            start_time = time.time()
            output = provider.chat(prompt, temperature=temperature, max_tokens=max_tokens, **kwargs)
            latency = time.time() - start_time
            
            # Update metrics
            self.performance_metrics[provider_name]["success"] += 1
            self.performance_metrics[provider_name]["latency"].append(latency)
