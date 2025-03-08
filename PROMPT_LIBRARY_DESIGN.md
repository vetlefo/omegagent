# Prompt Library and Model Router Design

This document outlines the design for a comprehensive prompt library and model routing system that will serve as a foundation for our Agentic-Reasoning platform.

## Overview

The system will consist of two main components:

1. **Prompt Library**: A structured collection of prompts organized by task, complexity, and purpose
2. **Model Router**: A service that matches the optimal model-prompt combination for each specific task

This design allows us to:
- Maintain a consistent, versioned library of high-quality prompts
- Select the most appropriate model for each task based on capabilities and costs
- A/B test different prompts against the same models
- Track performance metrics for continuous improvement

## Prompt Library Structure

### 1. Core Components

```python
class Prompt:
    """Base class for all prompts in the library."""
    
    def __init__(
        self, 
        name: str,
        description: str,
        template: str,
        version: str,
        parameters: List[str],
        tags: List[str],
        author: str,
        created_at: datetime,
        updated_at: datetime
    ):
        self.name = name
        self.description = description
        self.template = template
        self.version = version
        self.parameters = parameters
        self.tags = tags
        self.author = author
        self.created_at = created_at
        self.updated_at = updated_at
        
    def format(self, **kwargs) -> str:
        """Format the prompt template with the provided parameters."""
        # Validate that all required parameters are provided
        missing_params = set(self.parameters) - set(kwargs.keys())
        if missing_params:
            raise ValueError(f"Missing required parameters: {missing_params}")
        
        # Format the template with the provided parameters
        return self.template.format(**kwargs)
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert the prompt to a dictionary for storage."""
        return {
            "name": self.name,
            "description": self.description,
            "template": self.template,
            "version": self.version,
            "parameters": self.parameters,
            "tags": self.tags,
            "author": self.author,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Prompt":
        """Create a Prompt instance from a dictionary."""
        return cls(
            name=data["name"],
            description=data["description"],
            template=data["template"],
            version=data["version"],
            parameters=data["parameters"],
            tags=data["tags"],
            author=data["author"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"])
        )
```

### 2. Prompt Categories

Our prompt library will be organized into the following categories:

#### Task-Specific Prompts

- **Code Analysis**: Prompts for analyzing code structure, patterns, and relationships
- **Code Generation**: Prompts for generating code based on requirements
- **Code Modification**: Prompts for modifying existing code
- **Documentation**: Prompts for documenting code and creating guides
- **Planning**: Prompts for planning software architecture and tasks
- **Debugging**: Prompts for identifying and fixing issues

#### Reasoning Patterns

- **Chain-of-Thought**: Prompts that encourage step-by-step reasoning
- **Tree-of-Thought**: Prompts that explore multiple reasoning paths
- **ReAct**: Prompts that alternate between reasoning and acting
- **Reflexion**: Prompts that include self-reflection and correction

#### Model-Specific Optimizations

- **OpenAI-Optimized**: Prompts tailored for GPT-4, GPT-4o, etc.
- **Anthropic-Optimized**: Prompts tailored for Claude models
- **Gemini-Optimized**: Prompts tailored for Gemini's capabilities
- **Open Source-Optimized**: Prompts for Llama, Mistral, etc.

## Model Router Design

### 1. Core Components

```python
class ModelCapability:
    """Defines the capabilities of a specific model."""
    
    def __init__(
        self,
        model_id: str,
        provider: str,
        context_length: int,
        strengths: List[str],
        weaknesses: List[str],
        cost_per_1k_input_tokens: float,
        cost_per_1k_output_tokens: float,
        average_latency_ms: int,
        max_parallel_requests: int
    ):
        self.model_id = model_id
        self.provider = provider
        self.context_length = context_length
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.cost_per_1k_input_tokens = cost_per_1k_input_tokens
        self.cost_per_1k_output_tokens = cost_per_1k_output_tokens
        self.average_latency_ms = average_latency_ms
        self.max_parallel_requests = max_parallel_requests
        
class ModelRouter:
    """Routes tasks to the optimal model-prompt combination."""
    
    def __init__(
        self,
        prompt_library: Dict[str, Prompt],
        model_capabilities: Dict[str, ModelCapability],
        performance_metrics: Dict[str, Dict[str, float]]
    ):
        self.prompt_library = prompt_library
        self.model_capabilities = model_capabilities
        self.performance_metrics = performance_metrics
        
    def select_model_and_prompt(
        self,
        task: str,
        constraints: Dict[str, Any] = None
    ) -> Tuple[str, Prompt]:
        """
        Select the optimal model and prompt for a given task.
        
        Args:
            task: The task to perform
            constraints: Optional constraints like max_cost, max_latency, etc.
            
        Returns:
            A tuple of (model_id, prompt) to use for the task
        """
        # Implementation would consider:
        # 1. Task requirements
        # 2. Model capabilities
        # 3. Historical performance
        # 4. User constraints (budget, latency, etc.)
        # 5. A/B testing needs
        
        # For now, simplified implementation
        recommended_models = self._match_task_to_models(task, constraints)
        recommended_prompts = self._match_task_to_prompts(task)
        
        # Select the best combination based on historical performance
        best_score = -1
        best_model = None
        best_prompt = None
        
        for model in recommended_models:
            for prompt in recommended_prompts:
                key = f"{model.model_id}_{prompt.name}"
                score = self.performance_metrics.get(key, {}).get("success_rate", 0)
                
                if score > best_score:
                    best_score = score
                    best_model = model.model_id
                    best_prompt = prompt
        
        return best_model, best_prompt
    
    def _match_task_to_models(
        self,
        task: str,
        constraints: Dict[str, Any]
    ) -> List[ModelCapability]:
        """Match a task to suitable models based on capabilities and constraints."""
        # Implementation would filter and rank models
        pass
        
    def _match_task_to_prompts(self, task: str) -> List[Prompt]:
        """Match a task to suitable prompts from the library."""
        # Implementation would filter and rank prompts
        pass
```

## Example Library Implementation

### 1. Code Analysis Prompts

```python
# Repository Structure Analysis Prompt
repo_structure_analysis_prompt = Prompt(
    name="repository_structure_analysis",
    description="Analyzes the structure of a repository to identify key components and relationships",
    template="""
    You are an expert software architect tasked with analyzing a codebase.
    
    REPOSITORY CONTEXT:
    {repo_stub}
    
    TASK:
    Analyze this codebase and provide:
    1. The main architectural components and their relationships
    2. Key design patterns used
    3. Potential areas for refactoring or improvement
    4. Dependencies between modules
    
    FORMAT YOUR RESPONSE WITH THESE SECTIONS:
    - Architecture Overview
    - Component Relationships
    - Design Patterns
    - Refactoring Opportunities
    """,
    version="1.0.0",
    parameters=["repo_stub"],
    tags=["code_analysis", "architecture", "gemini_optimized"],
    author="Agentic-Reasoning Team",
    created_at=datetime.now(),
    updated_at=datetime.now()
)

# Function Analysis Prompt
function_analysis_prompt = Prompt(
    name="function_analysis",
    description="Analyzes a specific function to understand its purpose, inputs, outputs, and behavior",
    template="""
    You are an expert code reviewer analyzing a function.
    
    FUNCTION CODE:
    {function_code}
    
    CONTEXT:
    {context}
    
    TASK:
    Analyze this function and provide:
    1. A clear description of what this function does
    2. The inputs and outputs with their types and meanings
    3. The algorithm or approach used
    4. Any edge cases or potential bugs
    5. Suggestions for improvement
    
    FORMAT YOUR RESPONSE WITH THESE SECTIONS:
    - Function Purpose
    - Inputs and Outputs
    - Algorithm Description
    - Edge Cases
    - Improvement Suggestions
    """,
    version="1.0.0",
    parameters=["function_code", "context"],
    tags=["code_analysis", "function", "claude_optimized"],
    author="Agentic-Reasoning Team",
    created_at=datetime.now(),
    updated_at=datetime.now()
)
```

### 2. Model Capabilities Registry

```python
model_capabilities = {
    "gpt-4o": ModelCapability(
        model_id="gpt-4o",
        provider="openai",
        context_length=128000,
        strengths=["code_generation", "reasoning", "instruction_following"],
        weaknesses=["long_context_understanding", "mathematical_reasoning"],
        cost_per_1k_input_tokens=0.01,
        cost_per_1k_output_tokens=0.03,
        average_latency_ms=1500,
        max_parallel_requests=100
    ),
    
    "claude-3-5-sonnet": ModelCapability(
        model_id="claude-3-5-sonnet",
        provider="anthropic",
        context_length=200000,
        strengths=["reasoning", "instruction_following", "nuance"],
        weaknesses=["code_generation"],
        cost_per_1k_input_tokens=0.003,
        cost_per_1k_output_tokens=0.015,
        average_latency_ms=1000,
        max_parallel_requests=100
    ),
    
    "gemini-1.5-pro": ModelCapability(
        model_id="gemini-1.5-pro",
        provider="google",
        context_length=2000000,
        strengths=["long_context_understanding", "code_analysis", "multimodal"],
        weaknesses=["instruction_following"],
        cost_per_1k_input_tokens=0.00125,
        cost_per_1k_output_tokens=0.00375,
        average_latency_ms=2000,
        max_parallel_requests=50
    )
}
```

## Implementation Plan

### Phase 1: Core Library and Basic Router

1. Create the prompt library structure with JSON storage
2. Implement basic Prompt and ModelCapability classes
3. Build a simple ModelRouter with hardcoded rules
4. Add the first 10 essential prompts for common tasks

### Phase 2: Expanded Library and Dynamic Routing

1. Expand to 30+ prompts covering all task categories
2. Implement performance tracking and metrics collection
3. Enhance ModelRouter to use historical performance data
4. Add A/B testing capabilities for prompt optimization

### Phase 3: Advanced Features

1. Add prompt versioning and migration tools
2. Implement prompt composition for complex tasks
3. Build a prompt testing and validation framework
4. Create a UI for browsing and editing the prompt library

## Integration with Agent Orchestration

The Prompt Library and Model Router will integrate with our agent orchestration system as follows:

1. **StormOrchestratorAgent** will use the ModelRouter to:
   - Select Gemini for initial whole-codebase analysis
   - Route specific specialist tasks to appropriate models with tailored prompts

2. **During Agent Creation**:
   ```python
   def initialize_specialist_agents(self):
       """Initialize specialist agents with optimal model-prompt combinations."""
       
       # Get model-prompt combinations for each specialist
       code_analyzer_model, code_analyzer_prompt = self.model_router.select_model_and_prompt("code_analysis")
       code_generator_model, code_generator_prompt = self.model_router.select_model_and_prompt("code_generation")
       planner_model, planner_prompt = self.model_router.select_model_and_prompt("planning")
       
       # Initialize agents with their specialized prompts
       self.code_analyzer = Agent(code_analyzer_model, prompt=code_analyzer_prompt)
       self.code_generator = Agent(code_generator_model, prompt=code_generator_prompt)
       self.planner = Agent(planner_model, prompt=planner_prompt)
   ```

3. **During Task Execution**:
   ```python
   async def execute_task(self, task, context):
       """Execute a task using the appropriate agent."""
       
       # Dynamically select the model and prompt for this specific task
       model_id, prompt = self.model_router.select_model_and_prompt(
           task=task.type,
           constraints={
               "max_cost": self.budget_remaining,
               "max_latency": self.latency_requirement
           }
       )
       
       # Execute the task with the selected model and prompt
       result = await self.execute_with_model(model_id, prompt, task, context)
       
       # Log performance metrics
       self.log_performance(model_id, prompt.name, task.type, result)
       
       return result
   ```

## Success Metrics

We will measure the success of the Prompt Library and Model Router by tracking:

1. **Task Success Rate**: Percentage of tasks completed successfully
2. **Cost Efficiency**: Average cost per successful task
3. **Latency**: Average time to complete tasks
4. **User Satisfaction**: Ratings and feedback from users
5. **Coverage**: Percentage of task types with specialized prompts

The system will continuously optimize these metrics by learning from past performance and adapting its routing decisions.