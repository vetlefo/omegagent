# Agentic-Reasoning Codebase Improvement Roadmap

This document outlines a structured approach to improving the Agentic-Reasoning codebase for production readiness. Each phase has specific objectives, success criteria, and rules for progression.

## Phase 1: Foundation - State Management & Configuration

### 1.1 Session Management System (Priority: MUST HAVE, Size: L)

#### Technology Decision
- **Selected Technology**: Redis for session storage
  - Justification: Provides in-memory performance with persistence, suitable for scaling
  - Alternative: PostgreSQL if long-term analytics on sessions is needed

#### Tasks (in priority order)
1. Implement Redis connection pool with proper error handling
2. Create session data structure with TTL (time-to-live)
   - Design the Pydantic model for session data (user ID, conversation history, file paths, configuration settings)
   - Create a dedicated session ID generation utility function
3. Add WebSocket session tracking with unique IDs
4. Build session recovery mechanism for disconnections
5. Implement session cleanup for expired sessions
6. Implement set_session to serialize and store session data
7. Implement get_session to deserialize and retrieve session data
8. Integrate session management with WebSocket connection handling
9. Add comprehensive tests for all session operations

**Example Session Data Model:**
```python
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import time
import uuid

def generate_session_id() -> str:
    """Generate a unique session ID using UUID4."""
    return str(uuid.uuid4())

class SessionData(BaseModel):
    """Data structure for session state."""
    session_id: str = Field(..., description="Unique identifier for the session")
    user_id: Optional[str] = Field(None, description="User identifier if authentication is used")
    conversation_history: List[Dict] = Field(default_factory=list, description="History of the conversation")
    repo_stub: str = Field("", description="Generated repository stub")
    current_task: Optional[str] = Field(None, description="Currently executing task")
    config: Dict = Field(default_factory=dict, description="Session configuration")
    last_active: float = Field(default_factory=time.time, description="Timestamp of last activity")
    
    class Config:
        """Pydantic config."""
        extra = "allow"  # Allow additional fields for future extensibility
```

**Success Criteria:**
- WebSocket sessions persist across disconnections and reconnections
- Session data is properly stored and retrieved from Redis
- Sessions expire after appropriate TTL
- Client can reconnect using the same session ID and retrieve the previous state
- System handles Redis connection failures gracefully

**Rule to Proceed:** Must pass automated tests for session persistence that verify reconnection with state preservation.

### 1.2 Centralized Configuration System (Priority: MUST HAVE, Size: M)

#### Technology Decision
- **Selected Technology**: Pydantic for configuration management
  - Justification: Type safety, validation, and environment variable loading

#### Tasks (in priority order)
1. Create `config.py` using Pydantic's BaseSettings
2. Define configuration schema with all environment variables
3. Add validation for required settings with meaningful error messages
4. Implement configuration injection pattern
5. Add unit tests for configuration validation
6. Migrate existing environment variable usage to the new configuration system
7. Create a `.env.example` file as a template for required settings

**Example Implementation:**
```python
# backend/config.py
from pydantic import BaseSettings, Field, validator, RedisDsn

class Settings(BaseSettings):
    # API Keys
    openai_api_key: str
    bing_api_key: str = None
    gemini_api_key: str = None
    
    # LLM Configuration
    default_model: str = "gpt-4o"
    temperature: float = Field(0.7, ge=0, le=1.0)
    
    # Session Management
    redis_url: RedisDsn = "redis://localhost:6379/0"
    session_ttl: int = 86400  # 24 hours
    
    # Feature Flags
    use_semantic_analysis: bool = False
    use_storm: bool = False
    
    @validator('openai_api_key')
    def validate_openai_api_key(cls, v):
        if not v:
            raise ValueError("OpenAI API key is required")
        if not v.startswith("sk-"):
            raise ValueError("OpenAI API key must start with 'sk-'")
        return v
    
    class Config:
        env_file = ".env"
```

**Example .env.example:**
```
# Required API Keys
OPENAI_API_KEY=sk-your-openai-key-here
BING_API_KEY=your-bing-key-here
GEMINI_API_KEY=your-gemini-key-here

# LLM Configuration
DEFAULT_MODEL=gpt-4o
TEMPERATURE=0.7

# Session Management
REDIS_URL=redis://localhost:6379/0
SESSION_TTL=86400

# Feature Flags
USE_SEMANTIC_ANALYSIS=false
USE_STORM=false
```

**Success Criteria:**
- No direct `os.getenv()` calls outside config.py
- All components receive configuration via constructor injection
- Default values are provided for optional settings
- Configuration validation prevents missing critical settings
- Meaningful error messages for invalid configuration
- A clear `.env.example` template is provided for new developers

**Rule to Proceed:** All environment variables must be centralized and pass validation tests. No direct env var access in core code.

## Phase 2: Architecture - Component Refactoring

### 2.1 LM System Simplification (Priority: MUST HAVE, Size: M)

#### Tasks (in priority order)
1. Create centralized DSPy configuration in main application entry point
2. Remove nested `dspy.settings.context` blocks
3. Simplify LM class hierarchy
4. Implement clear provider interfaces for all LLM providers (OpenAI, Azure, Gemini, etc.) with consistent input/output formats
5. Add proper error handling for all LLM API calls
6. Remove or update deprecated code related to old DSPy and LM APIs

**Example Refactoring:**
```python
# Before (scattered throughout codebase):
with dspy.settings.context(lm=self.lm_config.some_lm):
    # Do something with LM
    
# After (in config.py or main.py):
import dspy
from agentic_research.lm import LitellmModel

# Load configuration
settings = Settings()
llm = LitellmModel(
    model=settings.default_model,
    api_key=settings.openai_api_key
)
dspy.settings.configure(lm=llm)

# In other modules:
class SomeModule:
    def __init__(self, lm: dspy.LM):  # Inject the LM
        self.lm = lm
        # Use self.lm directly, no context manager needed
```

**Example Provider Interface:**
```python
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List

class LLMProvider(ABC):
    """Abstract interface for LLM providers."""
    
    @abstractmethod
    async def generate(self, 
                      prompt: str, 
                      temperature: float = 0.7, 
                      max_tokens: Optional[int] = None, 
                      stop_sequences: Optional[List[str]] = None) -> Dict[str, Any]:
        """Generate text from the LLM.
        
        Args:
            prompt: The prompt to send to the LLM
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens to generate
            stop_sequences: Optional list of stop sequences
            
        Returns:
            Dictionary containing at minimum:
                - text: The generated text
                - usage: Token usage information
        """
        pass
```

**Success Criteria:**
- Single initialization point for DSPy settings
- Clean separation between interface and implementation
- Simplified calling pattern for LM operations
- Proper error handling for LM calls with specific exception types
- No nested context managers for LM calls
- All deprecated LM code is removed or updated
- Consistent interface for all LLM providers

**Rule to Proceed:** LM module must have 80% or higher test coverage and demonstrate reconnection capabilities.

### 2.2 Knowledge Base Refactoring (Priority: SHOULD HAVE, Size: L)

#### Tasks (in priority order)
1. Define the data structures for KnowledgeNode and the overall KnowledgeStore
2. Define clear interfaces for knowledge components
3. Split KnowledgeBase into focused components:
   - Core KnowledgeStore (data structure)
   - KnowledgeOrganizer (reorganization logic)
   - ReportGenerator (report creation)
   - KnowledgeSummarizer (summarization logic)
   - KnowledgeRetriever (search and retrieval logic)
4. Implement proper dependency injection
5. Create unit tests for each component
6. Benchmark performance against original implementation

**Example Interface Design:**
```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class KnowledgeNode(BaseModel):
    """Concrete implementation of a knowledge node."""
    id: str = Field(..., description="Unique identifier for this node")
    content: Dict[str, Any] = Field(..., description="Node content")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata about the node")
    created_at: float = Field(..., description="Timestamp when the node was created")
    updated_at: Optional[float] = None

class KnowledgeStore(ABC):
    """Interface for the core knowledge storage"""
    @abstractmethod
    async def add_node(self, node: KnowledgeNode) -> None:
        """Add a node to the knowledge store"""
        pass
    
    @abstractmethod
    async def get_node(self, node_id: str) -> Optional[KnowledgeNode]:
        """Retrieve a node by ID"""
        pass
    
    @abstractmethod
    async def search(self, query: str) -> List[KnowledgeNode]:
        """Search for nodes matching the query"""
        pass
    
    @abstractmethod
    async def delete_node(self, node_id: str) -> bool:
        """Delete a node from the store"""
        pass
    
    @abstractmethod
    async def update_node(self, node_id: str, updates: Dict[str, Any]) -> Optional[KnowledgeNode]:
        """Update a node in the store"""
        pass

class KnowledgeRetriever(ABC):
    """Interface for knowledge retrieval mechanisms"""
    @abstractmethod
    async def retrieve(self, query: str, top_k: int = 5) -> List[KnowledgeNode]:
        """Retrieve relevant knowledge nodes for a query"""
        pass
    
    @abstractmethod
    async def retrieve_by_metadata(self, metadata_filter: Dict[str, Any], top_k: int = 5) -> List[KnowledgeNode]:
        """Retrieve nodes matching metadata criteria"""
        pass

# Additional interfaces for KnowledgeOrganizer, ReportGenerator, etc.
```

**Success Criteria:**
- Each component has a single responsibility
- Clear interfaces between components
- Improved testability with isolated components
- Equal or better performance to original implementation
- 80% or higher test coverage for each component
- Asynchronous operations for potentially blocking operations
- Comprehensive test suite covering edge cases

**Rule to Proceed:** All components must have unit tests and demonstrate equal or better performance compared to original.

### 2.3 Prompt Library and Model Router (Priority: MUST HAVE, Size: L)

#### Tasks (in priority order)
1. Create core Prompt and ModelCapability classes
2. Implement prompt storage and retrieval system 
3. Build model selection logic based on task requirements
4. Develop performance tracking for model-prompt combinations
5. Create initial set of specialized prompts for common tasks
6. Add support for different system prompts based on model or role
7. Implement prompt versioning and testing mechanisms
8. Create a dedicated directory structure for prompt management

**Example Data Structure:**
```python
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from enum import Enum

class PromptType(str, Enum):
    """Types of prompts in the system."""
    SYSTEM = "system"
    USER = "user"
    CODE_GENERATION = "code_generation"
    CODE_REVIEW = "code_review"
    QUESTION_ANSWERING = "question_answering"
    PLANNING = "planning"
    SUMMARIZATION = "summarization"

class Prompt(BaseModel):
    """Model for a prompt template."""
    name: str = Field(..., description="Unique name of the prompt")
    version: str = Field(..., description="Version of the prompt (semver)")
    content: str = Field(..., description="The actual prompt template text")
    model_style: Optional[str] = Field(None, description="Specific model this prompt is optimized for")
    task_type: PromptType = Field(..., description="Type of task this prompt is for")
    tags: List[str] = Field(default_factory=list, description="Tags for categorizing prompts")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    created_at: float = Field(..., description="Creation timestamp")
    
    class Config:
        """Pydantic config."""
        use_enum_values = True
```

**Example Implementation:**
```python
class PromptLibrary:
    """Manages a library of prompts organized by task and purpose."""
    
    def __init__(self, storage_dir: str):
        self.storage_dir = storage_dir
        self.prompts = {}
        self._load_prompts()
        
    def get_prompt(self, name: str, version: str = None, model: str = None) -> Prompt:
        """Get a prompt by name and optional version, with model-specific overrides."""
        if name not in self.prompts:
            raise ValueError(f"Prompt '{name}' not found in library")
        
        # Check for model-specific version first
        if model and f"{name}_{model}" in self.prompts:
            prompt_dict = self.prompts[f"{name}_{model}"]
        else:
            prompt_dict = self.prompts[name]
            
        if version is None:
            # Return the latest version
            return max(prompt_dict.values(), key=lambda p: p.version)
            
        if version not in prompt_dict:
            raise ValueError(f"Version '{version}' of prompt '{name}' not found")
            
        return prompt_dict[version]
        
    def add_prompt(self, prompt: Prompt) -> None:
        """Add a new prompt to the library."""
        if prompt.name not in self.prompts:
            self.prompts[prompt.name] = {}
            
        self.prompts[prompt.name][prompt.version] = prompt
        self._save_prompt(prompt)
        
    def test_prompt(self, prompt: Prompt, test_cases: List[Dict], model: str = None) -> Dict:
        """Test a prompt against a set of test cases and return performance metrics."""
        results = []
        for test_case in test_cases:
            # Run test case and capture performance metrics
            # ...
            
        return {
            "prompt": prompt.name,
            "version": prompt.version,
            "model": model,
            "avg_score": sum(r["score"] for r in results) / len(results),
            "test_results": results
        }
        
    def _load_prompts(self) -> None:
        """Load prompts from the prompts directory."""
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir, exist_ok=True)
            return
            
        # Load all prompt files from the directory
        for filename in os.listdir(self.storage_dir):
            if filename.endswith('.json'):
                prompt_path = os.path.join(self.storage_dir, filename)
                with open(prompt_path, 'r') as f:
                    prompt_data = json.load(f)
                    prompt = Prompt(**prompt_data)
                    
                    if prompt.name not in self.prompts:
                        self.prompts[prompt.name] = {}
                    self.prompts[prompt.name][prompt.version] = prompt
            
    def _save_prompt(self, prompt: Prompt) -> None:
        """Save a prompt to an individual file."""
        # Create directory if it doesn't exist
        os.makedirs(self.storage_dir, exist_ok=True)
        
        # Save prompt to a file named by its unique identifier
        filename = f"{prompt.name}_v{prompt.version}.json"
        if prompt.model_style:
            filename = f"{prompt.name}_{prompt.model_style}_v{prompt.version}.json"
            
        file_path = os.path.join(self.storage_dir, filename)
        
        with open(file_path, 'w') as f:
            f.write(prompt.json(indent=2))
```

**Directory Structure:**
```
/prompts
  /system
    system_prompt_v1.0.0.json
    system_prompt_claude_v1.0.0.json
  /code_generation
    generate_class_v1.0.0.json
    refactor_function_v1.0.0.json
  /planning
    create_implementation_plan_v1.0.0.json
  /question_answering
    technical_qa_v1.0.0.json
```

**Success Criteria:**
- System can select appropriate model-prompt combinations based on task requirements
- Library includes at least 10 specialized prompts for common tasks
- Performance metrics are tracked for each model-prompt combination
- Users can add new prompts and update existing ones
- Implementation supports versioning and rollback
- System handles different system prompts for different models/roles
- Prompt testing mechanism ensures quality before deployment
- Prompts are stored in a structured, maintainable way

**Rule to Proceed:** Must demonstrate improved performance compared to generic prompts in A/B testing.

### 2.4 Gemini Integration for Holistic Codebase Analysis (Priority: MUST HAVE, Size: L)

#### Tasks (in priority order)
1. Create codebase ingestion service for Gemini
2. Implement Gemini API client with proper authentication
3. Build structured output parser for Gemini responses
4. Develop intelligent file filtering for large repositories
5. Add caching layer for repeated analyses
6. Implement token counting and truncation strategies for large codebases
7. Build fallback mechanism if Gemini analysis fails

**Example Implementation:**
```python
from typing import Dict, List, Optional, Any
import logging
import hashlib
import json

class GeminiCodeAnalyzer:
    def __init__(self, api_key: str, config: Config):
        self.gemini_client = GeminiClient(api_key)
        self.config = config
        self.cache = {}  # Simple in-memory cache (would use Redis in production)
        
    async def analyze_codebase(self, context: CodebaseContext) -> CodebaseAnalysis:
        """Perform comprehensive analysis of the codebase using Gemini."""
        # Generate cache key based on codebase fingerprint
        cache_key = self._generate_cache_key(context)
        
        # Check cache first
        if self.config.use_cache and cache_key in self.cache:
            logging.info(f"Using cached analysis for {context.repo_path}")
            return self.cache[cache_key]
        
        # Prepare the codebase context, managing token budget
        prepared_context = self._prepare_codebase_context(context)
        prompt = self._build_analysis_prompt(prepared_context)
        
        try:
            # Calculate approximate token count
            approx_tokens = self._estimate_token_count(prompt)
            logging.info(f"Estimated token count for analysis: {approx_tokens}")
            
            # Check if we might exceed token limits
            if approx_tokens > self.config.max_gemini_tokens:
                # Apply truncation strategy
                prompt = self._apply_truncation_strategy(prompt, self.config.max_gemini_tokens)
                logging.warning(f"Truncated prompt to fit within token limit")
            
            response = await self.gemini_client.generate_content(
                prompt, 
                model=self.config.gemini_model,
                temperature=0.2  # Low temperature for analytical tasks
            )
            
            # Parse structured response
            analysis = self._parse_structured_response(response)
            
            # Cache the result
            if self.config.use_cache:
                self.cache[cache_key] = analysis
                
            return analysis
            
        except GeminiAPIError as e:
            # Handle API errors with fallback
            logging.error(f"Gemini API error: {e}")
            if self.config.enable_fallback:
                logging.info("Falling back to standard OrchestratorAgent")
                return await self._fallback_analysis(context)
            raise
    
    def _generate_cache_key(self, context: CodebaseContext) -> str:
        """Generate a cache key based on repository state."""
        # Create a unique fingerprint of the codebase
        hasher = hashlib.sha256()
        
        # Add the repo path
        hasher.update(context.repo_path.encode())
        
        # Add file hashes for all tracked files
        for file_path, file_hash in sorted(context.file_hashes.items()):
            hasher.update(f"{file_path}:{file_hash}".encode())
            
        return hasher.hexdigest()
        
    def _prepare_codebase_context(self, context: CodebaseContext) -> CodebaseContext:
        """Prepare the codebase context for Gemini, filtering files intelligently."""
        # We can't send the entire codebase, so we need to be selective
        
        # Priority files (always include)
        priority_files = [
            'README.md', 'pyproject.toml', 'setup.py', 'requirements.txt',
            'package.json', 'Cargo.toml', 'Makefile', 'CMakeLists.txt'
        ]
        
        # Filter context to prioritize important files
        filtered_files = {}
        
        # First add priority files
        for file_path, content in context.files.items():
            if any(file_path.endswith(p) for p in priority_files):
                filtered_files[file_path] = content
                
        # Then add important code files (using heuristics or explicit configuration)
        # ...
                
        # Create new context with filtered files
        filtered_context = context.copy(update={'files': filtered_files})
        return filtered_context

    def _estimate_token_count(self, text: str) -> int:
        """Estimate the number of tokens in a text string."""
        # Simple estimation: ~1.3 tokens per word
        return int(len(text.split()) * 1.3)
        
    def _apply_truncation_strategy(self, prompt: str, max_tokens: int) -> str:
        """Apply truncation strategy to fit within token limits."""
        # This is a simplistic approach; in practice you'd use a more sophisticated strategy
        # For example, you might summarize large files or extract key functions
        
        # For now, just truncate to fit
        current_tokens = self._estimate_token_count(prompt)
        if current_tokens <= max_tokens:
            return prompt
            
        # Calculate roughly how much we need to reduce
        reduction_factor = max_tokens / current_tokens
        
        # Split into header (instructions) and content (code files)
        prompt_parts = prompt.split("====CODE FILES====")
        header = prompt_parts[0]
        content = prompt_parts[1] if len(prompt_parts) > 1 else ""
        
        # Keep the header intact, truncate the content
        header_tokens = self._estimate_token_count(header)
        content_tokens = current_tokens - header_tokens
        
        # Calculate max content tokens
        max_content_tokens = max_tokens - header_tokens
        
        # If content is too long, truncate it
        if content_tokens > max_content_tokens:
            # For now, just do a simple truncation
            # In practice, you'd want to truncate at file boundaries or use other strategies
            content_chars = int(len(content) * (max_content_tokens / content_tokens) * 0.95)  # 5% safety margin
            content = content[:content_chars] + "\n... [content truncated to fit token limit] ...\n"
            
        return header + "====CODE FILES====" + content
        
    async def _fallback_analysis(self, context: CodebaseContext) -> CodebaseAnalysis:
        """Fallback to a standard analysis if Gemini fails."""
        # Use standard OrchestratorAgent for analysis
        orchestrator = OrchestratorAgent(self.config)
        return await orchestrator.analyze_codebase(context)
```

**Success Criteria:**
- Gemini can process the entire codebase in a single context (up to 2M tokens)
- Analysis identifies key components, patterns, and relationships
- Implementation includes proper error handling and fallbacks
- Caching reduces redundant API calls for unchanged repositories
- Token budget management prevents exceeding API limits
- System gracefully handles large codebases that exceed Gemini's context window
- Fallback to standard orchestrator if Gemini analysis fails

**Rule to Proceed:** Analysis quality must be validated against manual expert analysis with at least 85% accuracy.

### 2.4 CoStormRunner Refactoring with Gemini (Priority: MUST HAVE, Size: XL)

#### Tasks (in priority order)
1. Modify StormOrchestratorAgent to use Gemini as first agent
2. Define clear interfaces for conversation management
3. Implement DiscourseManager pattern with Gemini integration
4. Create knowledge sharing protocols between agents
5. Build guided context provision for specialized agents
6. Add comprehensive logging for conversation flow

**Example Implementation:**
```python
class StormOrchestratorAgent:
    def __init__(self, config: Config):
        self.config = config
        self.gemini_analyzer = GeminiCodeAnalyzer(config.gemini_api_key, config)
        self.specialist_agents = self._initialize_specialist_agents()
        
    async def orchestrate(self, repo_path: str, user_query: str) -> Response:
        """Orchestrate the multi-agent storm process starting with Gemini."""
        # Step 1: Gemini whole-codebase analysis
        ingestion_service = CodebaseIngestionService(repo_path, self.config)
        codebase_context = await ingestion_service.process_repository()
        
        # Step 2: Get holistic analysis from Gemini
        analysis = await self.gemini_analyzer.analyze_codebase(codebase_context)
        
        # Step 3: Generate subqueries and context for specialist agents
        subqueries = self._generate_subqueries(user_query, analysis)
        
        # Step 4: Dispatch specialist agents with targeted context
        specialist_responses = []
        for subquery in subqueries:
            context = self._extract_relevant_context(analysis, subquery)
            agent = self._select_appropriate_agent(subquery)
            response = await agent.process(subquery, context)
            specialist_responses.append(response)
            
        # Step 5: Synthesize final response
        return self._synthesize_response(user_query, specialist_responses, analysis)
```

**Success Criteria:**
- Code follows single responsibility principle
- Each component is independently testable
- Specialist agents receive targeted, relevant context from Gemini analysis
- Clear separation of concerns
- Proper logging of conversation state transitions
- End-to-end response time improves by at least 30%

**Rule to Proceed:** Must demonstrate the refactored components working together in an end-to-end test.

## Phase 3: Resilience - Error Handling & Robustness

### 3.1 Exception System (Priority: MUST HAVE, Size: M)

#### Tasks (in priority order)
1. Define custom exception hierarchy
2. Implement consistent error handling strategy
3. Add proper error recovery mechanisms
4. Ensure all external API calls have error handling
5. Create comprehensive logging for exceptions
6. Handle asyncio.CancelledError appropriately in WebSocket handlers

**Example Exception Hierarchy:**
```python
# backend/exceptions.py
class AgenticReasoningError(Exception):
    """Base class for all custom exceptions in the project."""
    pass

class ConfigurationError(AgenticReasoningError):
    """Raised when configuration is invalid."""
    pass

class SessionError(AgenticReasoningError):
    """Raised when session operations fail."""
    pass

class LLMError(AgenticReasoningError):
    """Base class for LLM-related errors."""
    pass

class LLMConnectionError(LLMError):
    """Raised when connection to LLM API fails."""
    pass

class LLMRateLimitError(LLMError):
    """Raised when LLM API rate limit is exceeded."""
    pass

class SearchError(AgenticReasoningError):
    """Raised when search operations fail."""
    pass

# Usage example:
try:
    # Code that might raise an exception
    result = llm_client.complete(prompt)
except LLMRateLimitError as e:
    logging.warning(f"Rate limit exceeded: {e}. Retrying with backoff...")
    # Handle with specific retry logic
except LLMConnectionError as e:
    logging.error(f"Connection error: {e}")
    # Try fallback LLM or inform user
except LLMError as e:
    logging.error(f"Generic LLM error: {e}")
    # Generic LLM error handling
except asyncio.CancelledError:
    # Handle WebSocket cancellation gracefully
    logging.info("Operation cancelled by client")
    # Clean up resources
    raise  # Re-raise to properly cancel the task
except Exception as e:
    logging.exception(f"Unexpected error: {e}")  # Includes traceback
    # Generic error handling
```

**Success Criteria:**
- All exceptions are properly caught and handled with specific exception types
- Custom exceptions for different error categories
- Meaningful error messages for debugging
- Graceful degradation on failures with clear fallback paths
- All exceptions are properly logged with appropriate severity levels
- Proper handling of asyncio cancellation in WebSocket handlers

**Rule to Proceed:** System must handle all identified error scenarios in testing without crashing.

### 3.2 Retry Mechanism (Priority: SHOULD HAVE, Size: M)

#### Tasks (in priority order)
1. Add proper backoff limits to prevent infinite loops
2. Implement circuit breakers for external services
3. Create fallback mechanisms for critical services
4. Add logging for retry attempts
5. Add specific exceptions to backoff decorators for targeted retry handling

**Example Implementation:**
```python
import backoff
import requests
from typing import Any, Dict, Optional
from backend.exceptions import LLMConnectionError, LLMRateLimitError

def on_backoff(details):
    """Log backoff details."""
    logging.warning(
        f"Backing off {details['wait']:0.1f}s after {details['tries']} tries "
        f"calling function {details['target'].__name__}"
    )

@backoff.on_exception(
    backoff.expo,
    (LLMConnectionError, LLMRateLimitError, requests.exceptions.RequestException),
    max_tries=5,  # Limit retries to prevent infinite loops
    max_delay=30,  # Maximum delay between retries (30 seconds)
    on_backoff=on_backoff,  # Log each backoff
    giveup=lambda e: isinstance(e, LLMRateLimitError) and e.retry_after > 60,  # Don't retry long waits
)
async def generate_with_retry(
    prompt: str, 
    model: Optional[str] = None, 
    temperature: float = 0.7
) -> Dict[str, Any]:
    """Generate text with LLM using exponential backoff retry."""
    try:
        return await llm_client.generate(
            prompt=prompt, 
            model=model,
            temperature=temperature
        )
    except LLMConnectionError as e:
        # Check circuit breaker state
        if circuit_breaker.is_open():
            # Circuit is open, use fallback immediately
            return await call_fallback_llm(prompt, model, temperature)
        # Otherwise, let backoff handle the retry
        raise
```

**Circuit Breaker Implementation:**
```python
class CircuitBreaker:
    """Circuit breaker to prevent cascading failures."""
    
    def __init__(self, failure_threshold: int = 5, reset_timeout: int = 60):
        """Initialize circuit breaker.
        
        Args:
            failure_threshold: Number of failures before opening the circuit
            reset_timeout: Seconds to wait before attempting to close the circuit
        """
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN
        self.lock = asyncio.Lock()
        
    async def record_failure(self) -> None:
        """Record a failure and potentially open the circuit."""
        async with self.lock:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
                logging.warning(f"Circuit breaker opened after {self.failure_count} failures")
    
    async def record_success(self) -> None:
        """Record a success and potentially close the circuit."""
        async with self.lock:
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
                logging.info("Circuit breaker closed after successful operation")
    
    def is_open(self) -> bool:
        """Check if the circuit is open."""
        # If it's been long enough since the last failure, try a half-open state
        if self.state == "OPEN" and time.time() - self.last_failure_time > self.reset_timeout:
            self.state = "HALF-OPEN"
            logging.info("Circuit breaker half-open, allowing test request")
            
        return self.state == "OPEN"
```

**Success Criteria:**
- No possibility of infinite retry loops with clear max_tries limits
- Circuit breakers prevent cascading failures
- System degrades gracefully when services are unavailable
- All retry attempts are properly logged
- Fallback mechanisms are properly tested
- Specific exception types are properly targeted for retries
- Maximum delay between retries is capped to prevent excessive waits

**Rule to Proceed:** System must demonstrate graceful handling of simulated service outages.

### 3.3 Input Validation (Priority: MUST HAVE, Size: M)

#### Tasks (in priority order)
1. Add validation for all external inputs (API and WebSocket)
2. Implement proper type checking with Pydantic models
3. Create sanitization for user inputs
4. Add schema validation for structured data
5. Add client-side validation in Svelte components for immediate feedback

**Example Implementation:**
```python
from pydantic import BaseModel, Field, validator

class UserPrompt(BaseModel):
    """Model for validating user prompts."""
    content: str = Field(..., min_length=1, max_length=4000)
    config: dict = Field(default_factory=dict)
    
    @validator('content')
    def validate_content(cls, v):
        # Remove potentially harmful characters
        sanitized = v.replace('<script>', '').replace('</script>', '')
        return sanitized

# In WebSocket handler:
async def websocket_endpoint(websocket: WebSocket):
    try:
        # Receive message
        data = await websocket.receive_json()
        
        # Validate with Pydantic
        user_prompt = UserPrompt(**data)
        
        # Use validated data
        await process_prompt(user_prompt.content, user_prompt.config)
    except ValidationError as e:
        # Send validation error back to client
        await websocket.send_json({
            "type": "error",
            "content": f"Invalid input: {e}"
        })
```

**Frontend Validation Example:**
```javascript
// In a Svelte component
<script>
  import { validatePrompt } from '../utils/validation';
  
  let prompt = '';
  let errors = [];
  
  function validateInput() {
    errors = validatePrompt(prompt);
    return errors.length === 0;
  }
  
  function handleSubmit() {
    if (validateInput()) {
      // Send to backend
      sendPrompt(prompt);
    }
  }
</script>

<div class="prompt-form">
  <textarea bind:value={prompt} on:blur={validateInput}></textarea>
  {#if errors.length > 0}
    <div class="error-messages">
      {#each errors as error}
        <p class="error">{error}</p>
      {/each}
    </div>
  {/if}
  <button on:click={handleSubmit} disabled={errors.length > 0}>Submit</button>
</div>
```

**Success Criteria:**
- All inputs are validated before processing
- Invalid inputs are rejected with clear error messages
- System is protected against malformed inputs
- Input validation performance is acceptable
- Frontend provides immediate validation feedback to users
- Validation rules are consistent between frontend and backend

**Rule to Proceed:** Must pass security review focused on input handling.

## Phase 4: Usability - Continuous Orchestration

### 4.1 Continuous Conversation System (Priority: MUST HAVE, Size: L)

#### Tasks (in priority order)
1. Define conversation state machine
2. Implement feedback loop in orchestration
3. Add conversation continuation mechanisms
4. Create proper conversation state management
5. Preserve context across multiple exchanges
6. Handle edge cases such as user messages during long-running tasks

**Example Conversation Flow:**
```
┌─────────────┐
│             │
│   Initial   │
│   Prompt    │
│             │
└──────┬──────┘
       │
       ▼
┌─────────────┐         ┌─────────────┐
│             │         │             │
│    Agent    │         │    User     │
│   Response  │────────▶│   Feedback  │
│             │         │             │
└──────┬──────┘         └──────┬──────┘
       │                       │
       │                       │
       ▼                       ▼
┌─────────────┐         ┌─────────────┐
│             │         │             │
│ Conversation│◀────────│   Updated   │
│  Continues  │         │    Agent    │
│             │         │   Response  │
└─────────────┘         └─────────────┘
```

**Example Implementation:**
```python
async def run(self, user_prompt: str):
    """Starts the agentic process with continuous feedback loop."""
    try:
        self.user_prompt = user_prompt
        initial_prompt = f"User Request: {self.user_prompt}\n\nRepository Context:\n{self.repo_stub}"
        
        # Start a task for the agent run (potentially long-running)
        self.current_task = asyncio.create_task(self.agent.run(initial_prompt))
        
        # Set up message queue for handling interruptions
        self.message_queue = asyncio.Queue()
        
        # Start a background task to listen for user messages during agent execution
        self.message_listener = asyncio.create_task(self._listen_for_messages())
        
        # Wait for agent response or user interruption
        response = await self.current_task
        
        # Format response
        final_response = "".join(response.data) if isinstance(response.data, tuple) else str(response.data)
        await self.comm.send("log", f"[Agent Response]:\n{final_response}")
        
        # Ask if the user wants to continue
        await self.comm.send("continue", {
            "message": final_response,
            "options": ["Continue with feedback", "Complete this task"]
        })
        
        # Wait for user's decision
        continue_response = await self.comm.receive("continue")
        choice = continue_response.get("content", "").lower()
        
        if "continue" in choice or "feedback" in choice:
            # Get feedback and continue conversation
            await self.comm.send("question", "What feedback would you like to provide?")
            feedback = await self.comm.receive("question")
            feedback_text = feedback.get("content", "")
            
            # Continue conversation with feedback
            new_prompt = (
                f"User's original request: {self.user_prompt}\n\n"
                f"My previous response: {final_response}\n\n"
                f"User's feedback: {feedback_text}"
            )
            
            # Recursive call with new context
            return await self.run(new_prompt)
        else:
            # Complete the task
            await self.comm.send("completed", "Orchestration completed.")
            
    except asyncio.CancelledError:
        # Handle user interruption gracefully
        await self.comm.send("info", "Your request was interrupted. What would you like to do next?")
        raise
    except Exception as e:
        error_msg = f"Error during orchestration: {str(e)}"
        await self.comm.send("error", error_msg)
        raise
        
    async def _listen_for_messages(self):
        """Listen for user messages during agent execution."""
        try:
            while True:
                msg = await self.comm.receive_any()
                if msg.get("type") == "interrupt":
                    # User wants to interrupt current task
                    if self.current_task and not self.current_task.done():
                        self.current_task.cancel()
                        await self.comm.send("info", "Processing interrupted")
                else:
                    # Queue message for later processing
                    await self.message_queue.put(msg)
        except Exception as e:
            logging.error(f"Error in message listener: {e}")
```

**Success Criteria:**
- Users can provide feedback after agent responses
- Conversations continue naturally across multiple exchanges
- Context is preserved throughout the conversation
- System properly manages conversation state
- Conversation history is properly stored in session
- System handles user messages during long-running tasks
- Graceful interruption and recovery is possible

**Rule to Proceed:** End-to-end testing must demonstrate multi-turn conversations with context preservation.

### 4.2 Frontend Enhancements (Priority: SHOULD HAVE, Size: M)

#### Tasks (in priority order)
1. Add robust error handling for WebSocket issues
2. Implement improved loading states
3. Create better user feedback mechanisms
4. Add session recovery UI
5. Implement responsive design for mobile compatibility

**Frontend Message Protocol:**
```typescript
// Message types for WebSocket communication
interface BaseMessage {
  type: string;
  content: any;
}

interface LogMessage extends BaseMessage {
  type: "log";
  content: string;
}

interface ErrorMessage extends BaseMessage {
  type: "error";
  content: string;
}

interface ContinueMessage extends BaseMessage {
  type: "continue";
  content: {
    message: string;
    options: string[];
  };
}

interface QuestionMessage extends BaseMessage {
  type: "question";
  content: string;
}

interface SessionMessage extends BaseMessage {
  type: "session";
  content: {
    session_id: string;
  };
}
```

**Success Criteria:**
- User-friendly error messages for all error states
- Clear loading indicators for long-running operations
- Intuitive feedback submission interface
- Smooth session recovery experience
- Mobile-friendly responsive design

**Rule to Proceed:** Must pass usability testing with target users.

## Phase 5: Quality - Documentation & Testing

### 5.1 Documentation (Priority: MUST HAVE, Size: L)

#### Tasks (in priority order)
1. Add docstrings to all public classes and functions
2. Create API documentation with Sphinx
3. Implement consistent documentation style (Google style)
4. Add architectural overview documentation
5. Create developer setup guide
6. Create a contribution guide (CONTRIBUTING.md)

**Example Docstring Format:**
```python
def get_relevant_snippets(
    search_terms: str,
    root_directory: str,
    top_k: int = 10
) -> List[Dict[str, str]]:
    """
    Searches through files in the codebase for search_terms using ChromaDB with 
    semantic search capabilities.
    
    This function:
    1. Uses semantic understanding to match concepts rather than just keywords
    2. Provides a relevance score based on semantic similarity 
    3. Optionally returns full file content or just the relevant chunks
    
    Args:
        search_terms: The search query to match against code
        root_directory: The root directory of the codebase
        top_k: Maximum number of relevant snippets to return
        
    Returns:
        List of dictionaries containing:
            - filename: Path to the file
            - snippet: Matching content from the file
            - distance: Distance metric (lower is better match)
            - relevance_score: Normalized score (higher is better match)
            
    Raises:
        FileNotFoundError: If root_directory doesn't exist
        SearchError: If search index building fails
    """
```

**CONTRIBUTING.md Outline:**
```markdown
# Contributing to Agentic-Reasoning

## Development Environment Setup
- Step-by-step guide to set up the development environment
- Required dependencies and tools

## Code Style and Standards
- PEP 8 guidelines
- Documentation requirements
- Naming conventions

## Development Workflow
- Branch naming convention
- Commit message guidelines
- Pull request process

## Testing
- How to run tests
- Requirements for new code (test coverage)
- Types of tests needed

## Documentation
- How to update documentation
- Where to add new documentation

## Code Review Process
- What to expect in code reviews
- Review criteria

## Getting Help
- Where to ask questions
- Resources for learning
```

**Success Criteria:**
- All public APIs have complete docstrings
- Generated documentation is comprehensive
- Documentation follows consistent style
- Architecture is well-documented for new developers
- Setup guide enables new developers to get started quickly
- Contribution guide eases onboarding of new contributors

**Rule to Proceed:** Documentation must be complete and pass review by team members.

### 5.2 Testing Infrastructure (Priority: MUST HAVE, Size: XL)

#### Tasks (in priority order)
1. Define testing strategy for different module types
2. Set up pytest and pytest-asyncio
3. Write unit tests for backend/utils.py
4. Write unit tests for backend/repo_map.py
5. Write integration tests for agent interactions
6. Implement comprehensive unit test suite
7. Add integration tests for component interactions
8. Create end-to-end tests for critical flows
9. Implement performance tests for critical paths
10. Set up a CI/CD pipeline using GitHub Actions to run tests automatically

**Example Test Strategy:**
```python
# Unit test example for LM module
import pytest
from unittest.mock import patch, MagicMock
from backend.exceptions import LLMConnectionError, LLMRateLimitError
from agentic_research.lm import LitellmModel

class TestLitellmModel:
    def setup_method(self):
        self.model = LitellmModel(model="gpt-4o")
    
    @patch("litellm.completion")
    def test_successful_completion(self, mock_completion):
        # Setup mock
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Test response"
        mock_completion.return_value = mock_response
        
        # Test completion
        result = self.model.complete("Test prompt")
        
        # Verify completion was called with expected params
        mock_completion.assert_called_once()
        assert "Test prompt" in str(mock_completion.call_args)
        assert result == "Test response"
    
    @patch("litellm.completion")
    def test_rate_limit_error(self, mock_completion):
        # Setup mock to raise rate limit error
        mock_completion.side_effect = Exception("Rate limit exceeded")
        
        # Test that our custom exception is raised
        with pytest.raises(LLMRateLimitError):
            self.model.complete("Test prompt")
```

**GitHub Actions CI Configuration:**
```yaml
# .github/workflows/test.yml
name: Test Suite

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[dev]"
    - name: Run tests
      run: |
        pytest -v --cov=agentic_research --cov=backend
    - name: Upload coverage reports
      uses: codecov/codecov-action@v3
```

**Testing Levels:**
- **Unit Tests**: Test individual components in isolation (80% coverage target)
- **Integration Tests**: Test interactions between components
- **End-to-End Tests**: Test complete user flows
- **Performance Tests**: Test system under load
- **Security Tests**: Test for vulnerabilities

**Success Criteria:**
- Core components have 80%+ test coverage
- All critical flows have end-to-end tests
- Integration tests verify component interactions
- Performance tests validate system under load
- Test suite runs automatically in CI/CD pipeline

**Rule to Proceed:** All tests must pass and coverage goals must be met.

## Phase 6: Optimization - Performance & Scalability

### 6.1 Performance Optimization (Priority: SHOULD HAVE, Size: M)

#### Caching Strategy
- **Repository Maps**: Cache with TTL of 5 minutes
- **Embeddings**: Cache indefinitely (they don't change)
- **Search Results**: Cache with TTL of 1 hour
- **LLM Responses**: Do not cache (dynamic content)

#### Tasks (in priority order)
1. Implement caching for expensive operations
2. Optimize database queries and storage
3. Reduce LLM token usage where possible
4. Minimize unnecessary computations
5. Implement performance monitoring
6. Identify and address performance bottlenecks using profiling tools

#### Performance Targets
- Average response time under 3 seconds for standard queries
- Search operations complete within 500ms
- LLM calls optimized to use minimum necessary tokens
- System handles concurrent users with minimal degradation

**Success Criteria:**
- System meets performance targets under load
- Response times are acceptable for user experience
- Resource usage is optimized
- Costs are minimized for LLM API usage
- Performance metrics are tracked and logged
- Identified bottlenecks are addressed

**Rule to Proceed:** Performance benchmarks must meet or exceed targets.

### 6.2 Scalability Enhancements (Priority: COULD HAVE, Size: L)

#### Tasks (in priority order)
1. Implement proper connection pooling for Redis and databases
2. Add horizontal scaling capabilities
3. Create load balancing strategy
4. Implement proper resource management
5. Add monitoring and alerting

**Success Criteria:**
- System can scale to handle increased load
- Resources are properly managed under stress
- No single points of failure in architecture
- System degrades gracefully under extreme load
- Monitoring alerts on potential issues

**Rule to Proceed:** Load testing must demonstrate linear scaling with added resources.

## Phase 7: Deployment & Distribution - User-Friendly Installation

### 7.1 Streamlit Integration (Priority: MUST HAVE, Size: M)

#### Tasks (in priority order)
1. Create Streamlit-compatible version of the application
2. Develop simplified configuration for Streamlit deployment
3. Build streamlined API for Streamlit components
4. Implement one-click setup process
5. Create comprehensive user guide for Streamlit version

**Success Criteria:**
- Streamlit app provides core functionality of the system
- Configuration is simple and well-documented
- Setup requires minimal technical knowledge
- Performance is acceptable within Streamlit constraints
- Non-technical users can successfully use the application

**Rule to Proceed:** Non-technical users must be able to successfully install and run the application.

### 7.2 Containerization (Priority: SHOULD HAVE, Size: M)

#### Tasks (in priority order)
1. Create Docker setup for easy deployment
2. Implement docker-compose for multi-container setup
3. Add Kubernetes configuration for scalable deployment
4. Build automated CI/CD pipeline
5. Optimize container size and startup time

**Example Dockerfile:**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV USE_SEMANTIC_ANALYSIS=false
ENV USE_STORM=false

# Expose ports
EXPOSE 8000

# Run the application
CMD ["uvicorn", "backend.server:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Success Criteria:**
- Docker image builds successfully and runs reliably
- Multi-container setup works with minimal configuration
- Kubernetes deployment scales properly
- CI/CD pipeline automates testing and deployment
- Containers are optimized for size and startup time

**Rule to Proceed:** Container deployment must be reliable and well-documented.

### 7.3 Installation Package (Priority: SHOULD HAVE, Size: M)

#### Tasks (in priority order)
1. Create installable Python package with pyproject.toml
2. Build simple CLI for management
3. Implement automatic dependency resolution
4. Develop comprehensive quickstart guide
5. Publish to PyPI

**Example pyproject.toml:**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "agentic-reasoning"
version = "0.1.0"
description = "An agentic reasoning system for advanced natural language processing"
readme = "README.md"
requires-python = ">=3.10"
license = { file = "LICENSE" }
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
dependencies = [
    "fastapi>=0.100.0",
    "uvicorn>=0.22.0",
    "pydantic>=2.0.0",
    "dspy-ai>=2.0.0",
    "redis>=4.5.0",
    # Core dependencies only
]

[project.optional-dependencies]
dev = [
    "pytest>=7.3.1",
    "black>=23.3.0",
    "isort>=5.12.0",
    "mypy>=1.3.0",
]
streamlit = [
    "streamlit>=1.22.0",
]
ollama = [
    "ollama>=0.1.0",
]

[project.scripts]
agentic-reasoning = "agentic_research.cli:main"

[tool.hatch.build.targets.wheel]
packages = ["agentic_research", "backend"]
```

**Success Criteria:**
- Package installs cleanly via pip
- CLI provides essential management functions
- Dependencies are properly resolved during installation
- Quickstart guide enables successful first-time use
- Package is published on PyPI

**Rule to Proceed:** Package passes PyPI standards and installs successfully in clean environments.

### 7.4 Cloud Deployment Templates (Priority: COULD HAVE, Size: M)

#### Tasks (in priority order)
1. Create AWS CloudFormation template
2. Build Azure Resource Manager template
3. Develop Google Cloud Deployment Manager template
4. Implement cost optimization for cloud deployments
5. Create detailed deployment guides for each platform

**Success Criteria:**
- Templates deploy successfully on respective cloud platforms
- Configuration is minimal and well-documented
- Deployed system operates correctly
- Cost estimates are accurate and reasonable
- Deployment guides are comprehensive and easy to follow

**Rule to Proceed:** Non-expert users should be able to deploy to cloud environments using the templates.

## Implementation Guidelines

1. **Start Small**: Begin with the most critical components first.
2. **Continuous Integration**: Keep the system running throughout refactoring.
3. **Test-Driven**: Write tests before implementation where possible.
4. **Incremental Delivery**: Deliver value at the end of each phase.
5. **Documentation First**: Update documentation before changing interfaces.
6. **Code Reviews**: Require reviews for all significant changes.
7. **Performance Awareness**: Monitor performance impact of all changes.
8. **Type Hints**: Add return type hints to all functions for improved code quality.
9. **Structured Logging**: Use structured logging (e.g., with structlog) for better log analysis.
10. **Code Sandboxing**: Ensure any code execution from user input happens in a sandboxed environment.

## Security Considerations

### Authentication & Authorization
- Implement API key authentication for server access
- Add user authentication for multi-user deployments
- Create proper role-based access control

### Data Protection
- Sanitize all user inputs to prevent injection attacks
- Validate file paths to prevent directory traversal
- Implement proper encryption for sensitive data
- Use dedicated libraries for HTML/Markdown sanitization (e.g., bleach) to prevent XSS vulnerabilities

### API Security
- Rate limit API endpoints to prevent abuse and prevent denial-of-service attacks
- Implement proper CORS settings
- Add request validation for all endpoints

### Dependency Security
- Regularly scan dependencies for vulnerabilities
- Pin dependency versions to prevent supply chain attacks
- Use trusted sources for dependencies

## Logging Strategy

### Logging Levels
- **ERROR**: Unexpected errors that require attention
- **WARNING**: Potential issues that might require attention
- **INFO**: Important operational events
- **DEBUG**: Detailed information for debugging

### Logging Content
- Timestamps for all log entries
- Request IDs for tracing requests across the system
- User IDs for user-specific actions
- Structured logging for machine parsing

## Progress Tracking

Track progress on this roadmap using GitHub Projects. Each phase should be broken down into individual tasks with clear acceptance criteria.

- Create a GitHub Project for the roadmap
- Add issues for each task with proper labeling
- Track progress with kanban-style columns
- Conduct regular reviews of roadmap progress

Update this document as implementation progresses to reflect lessons learned and evolving priorities.