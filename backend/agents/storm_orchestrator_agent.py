from typing import List, Any, Dict, Optional
import asyncio
import os
from agentic_research.collaborative_storm.modules.callback import BaseCallbackHandler
# Fix for the missing RunResult import
from pydantic_ai.result import FinalResult as RunResult
from agentic_research.rm import BingSearch
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.result import RunContext
from backend.agents.planner_agent import PlannerAgent, Plan
from backend.agents.coder_agent import CoderAgent, FullCodeUpdates
from backend.utils import build_full_context, get_file_content, get_relevant_snippets
from backend.agents.utils import send_usage
from backend.repo_map import RepoMap
from backend.models.shared import RelevantFiles, RelevantFile
from backend.communication import WebSocketCommunicator
import difflib

# Import CollaborativeStorm components from agentic_research
from agentic_research.collaborative_storm.engine import CollaborativeStormLMConfigs, RunnerArgument, CoStormRunner 
from agentic_research.collaborative_storm.discourse_manager import DiscourseManager
from agentic_research.collaborative_storm.turn_policy import TurnPolicySpec
from agentic_research.logging_wrapper import LoggingWrapper
from agentic_research.interface import ConversationTurn

# Import MCP Tool for flexible model selection and Ollama integration
from scripts.tools.mcp_tool import MCPTool
from scripts.tools.ollama_client import OllamaClient

import logging
logger = logging.getLogger(__name__)

class StormOrchestratorAgent:
    """
    Enhanced version of OrchestratorAgent that uses agentic_research's CollaborativeStorm
    capabilities for improved reasoning and planning.
    
    This agent leverages the multi-agent collaborative architecture from CollaborativeStorm
    to provide more comprehensive analysis and planning while maintaining compatibility
    with the existing AI Codepilot infrastructure.
    """
    MODEL_NAME = "gpt-4o"

    def __init__(
        self, 
        repo_stub: str, 
        comm: WebSocketCommunicator, 
        review: bool = True, 
        max_iterations: int = 1, 
        root_directory: str = ".",
        use_storm: bool = True,
        include_semantic_relationships: bool = False,
        use_mcp: bool = False,
        use_ollama: bool = False
    ):
        self.discourse_manager = None  # Initialize to None, will be set in _initialize_storm if use_storm is True
        # Configure the model based on environment variables and parameters
        model_provider = os.getenv("MODEL_PROVIDER", "openai")
        model_name = os.getenv("MODEL_NAME", self.MODEL_NAME)
        self.use_mcp = use_mcp or os.getenv("USE_MCP", "false").lower() == "true"
        self.use_ollama = use_ollama or os.getenv("USE_OLLAMA", "false").lower() == "true"
        
        # Initialize core attributes
        self.repo_stub = repo_stub
        self.comm = comm
        self.planner = PlannerAgent(comm=comm)
        self.review = review
        self.max_iterations = max_iterations
        self.root_directory = root_directory
        self.coder = CoderAgent(review=self.review, max_iterations=self.max_iterations, comm=comm, root_directory=root_directory)
        self.user_prompt = None
        self.include_semantic_relationships = include_semantic_relationships
        
        # Initialize the model (standard, MCP, or Ollama)
        if self.use_mcp:
            # Get MCP configuration from environment variables or defaults
            primary_provider = os.getenv("MCP_PRIMARY_PROVIDER", "openai")
            primary_model = os.getenv("MCP_PRIMARY_MODEL", self.MODEL_NAME)
            fallback_provider = os.getenv("MCP_FALLBACK_PROVIDER", "ollama")
            fallback_model = os.getenv("MCP_FALLBACK_MODEL", "llama3")
            
            try:
                self.model = MCPTool(
                    primary_provider=primary_provider,
                    primary_model=primary_model,
                    fallback_provider=fallback_provider,
                    fallback_model=fallback_model,
                    temperature=0.7,
                    max_tokens=2000
                )
                available_models = self.model.list_available_models()
                logger.info(f"Initialized MCP Tool with models: {available_models}")
            except Exception as e:
                logger.error(f"Failed to initialize MCP Tool: {e}. Falling back to standard OpenAI model.")
                self.model = OpenAIModel(self.MODEL_NAME)
                self.use_mcp = False
        elif self.use_ollama:
            # Use Ollama directly
            ollama_model = os.getenv("OLLAMA_MODEL", "llama3")
            try:
                self.model = OllamaClient(
                    model=ollama_model,
                    temperature=0.7,
                    max_tokens=2000
                )
                logger.info(f"Initialized Ollama client with model: {ollama_model}")
            except Exception as e:
                logger.error(f"Failed to initialize Ollama client: {e}. Falling back to standard OpenAI model.")
                self.model = OpenAIModel(self.MODEL_NAME)
                self.use_ollama = False
        else:
            # Use standard OpenAI model
            self.model = OpenAIModel(self.MODEL_NAME)
        
        # Initialize CollaborativeStorm components if enabled
        self.use_storm = use_storm and os.getenv("USE_STORM", "false").lower() == "true"
        self.storm_runner = None
        self.use_discourse_manager = os.getenv("USE_DISCOURSE_MANAGER", "false").lower() == "true"
        
        if self.use_storm:
            try:
                # Initialize CollaborativeStorm components
                self._initialize_storm()
                logger.info("CollaborativeStorm components initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize CollaborativeStorm components: {e}")
                self.use_storm = False
                
        # Set up the agent with enhanced system prompt to utilize collaborative reasoning
        enhanced_prompt = (
            """You are a senior developer responsible for fulfilling a user request within a codebase, 
            by planning and making incremental changes. You have access to a special collaborative reasoning 
            system that helps you analyze complex problems from multiple expert perspectives.
            
            Given the user request and the initial repository stub, use the available tools to:
            1. Analyze the problem collaboratively with various expert perspectives (using storm_analyze_problem)
            2. Create a comprehensive plan based on this analysis
            3. Identify relevant files and code components
            4. Search the codebase for relevant snippets
            5. Update code as needed
            
            Iterate using the tools until the user request is completely resolved. Only change the codebase when necessary.
            If the user simply asks for explanation, don't use the 'update_the_code' tool but leverage the storm_analyze_problem
            tool to provide a comprehensive explanation.
            
            Always use the 'read_file' tool to read the content of files that are relevant to fulfill the user's request.
            Use the 'search' tool to find specific code snippets in the codebase as needed."""
        )
        
        # Fall back to standard prompt if STORM isn't available
        if not self.use_storm:
            enhanced_prompt = (
                """You are a senior developer responsible for fulfilling a user request within a codebase, 
                by planning and making incremental changes. Given the user request and the initial repository stub, 
                use the available tools to create a plan, identify relevant files, read file contents, search codebase, and update code. 
                Iterate using the tools until the user request is completely resolved. Only change the codebase when necessary, 
                if the user simply asks for explanation, don't use the 'update_the_code' tool.
                Always use the 'read_file' tool to read the content of files that are relevant to fulfill the user's request.
                Use the 'search' tool to find specific code snippets in the codebase as needed. This is not a websearch!"""
            )
        
        self.agent = Agent(
            self.model,
            result_type=str,
            system_prompt=enhanced_prompt
        )
        
        # Register tools
        self._register_tools()
        
    def _initialize_storm(self):
        """Initialize CollaborativeStorm components for enhanced reasoning."""
        # Set up logging wrapper
        self.logging_wrapper = LoggingWrapper()
        
        # Configure LM models for STORM
        self.storm_lm_config = CollaborativeStormLMConfigs()
        lm_type = os.getenv("ENCODER_API_TYPE", "openai")
        self.storm_lm_config.init(lm_type=lm_type)
        
        # Initialize encoder
        from agentic_research.encoder import Encoder
        self.encoder = Encoder(encoder_type=lm_type)
        
        # Create RunnerArgument with default settings
        self.storm_runner_args = RunnerArgument(
            topic="code_analysis",  # Will be updated for each problem
            retrieve_top_k=5,
            max_search_queries=2,
            total_conv_turn=5,  # Limited for interactive use
            max_thread_num=3    # Limited for interactive use
        )
        
        # Create CoStormRunner instance (but don't run warm_start yet)
        self.storm_runner = CoStormRunner(
            lm_config=self.storm_lm_config,
            runner_argument=self.storm_runner_args,
            logging_wrapper=self.logging_wrapper,
        )
        
        # Initialize retrieval model (BingSearch)
        self.rm = BingSearch(k=10)  # Create a BingSearch instance with k=10
        
        # Initialize callback handler
        self.callback_handler = BaseCallbackHandler()  # Initialize a basic callback handler
        
        # Create DiscourseManager instance for conversational interactions
        self.discourse_manager = DiscourseManager(
            lm_config=self.storm_lm_config,
            runner_argument=self.storm_runner_args,
            logging_wrapper=self.logging_wrapper,
            rm=self.rm,
            encoder=self.encoder,
            callback_handler=self.callback_handler
        )
    
    def _register_tools(self):
        """Register the tools the agent can use."""
        
        async def create_plan_tool(ctx: RunContext[str], user_prompt: str) -> Plan:
            """Creates a plan to address the user's request based on the repository context."""
            log_msg = f"[Tool Call: create_plan] with user_prompt: {user_prompt}"
            await self.comm.send("log", log_msg)
            result = await self.planner.plan(user_prompt, self.repo_stub)
            
            # Send planner token usage using utility function
            await send_usage(self.comm, result, "orchestrator-planner")
                    
            await self.comm.send("log", f"[Tool Call: create_plan] returned: {result}")
            return result

        async def update_code_tool(ctx: RunContext[str], task: str, files: List[str] | RelevantFiles) -> str:
            """Updates code based on the task and relevant files."""
            # Convert files to RelevantFiles if it's a list of strings
            if isinstance(files, list):
                files = RelevantFiles(files=[RelevantFile(filename=f) for f in files])
            
            # Convert any relative paths in files to absolute paths
            for file in files.files:
                if not os.path.isabs(file.filename):
                    file.filename = os.path.join(self.root_directory, file.filename)

            # Build full context from the repository stub and relevant files.
            context = build_full_context(
                self.repo_stub, 
                files, 
                self.root_directory,
                include_semantic_relationships=self.include_semantic_relationships
            )
            
            # Add original user prompt to the context
            context += f"\n\nOriginal User Request:\n{self.user_prompt}\n"
            
            # If STORM is available, add STORM analysis to context
            if self.use_storm and self.storm_runner:
                storm_analysis = await self._get_storm_analysis(task, context)
                if storm_analysis:
                    context += f"\n\nCollaborative Expert Analysis:\n{storm_analysis}\n"
                    
            await self.comm.send("log", f"[Tool Call: update_code] with task: {task}\nuser_prompt: {self.user_prompt}\n{files}")

            # Get code updates from the coder agent.
            updates: FullCodeUpdates = await self.coder.update_code(task, context)
            await self.comm.send("log", f"[Tool Call: update_code] received updates for: {[u.filename for u in updates.updates]}")
            results = []
            
            # Process each update sequentially
            for update in updates.updates:
                # Ensure absolute path
                if not os.path.isabs(update.filename):
                    update.filename = os.path.join(self.root_directory, update.filename)

                # Generate a unified diff
                diff = difflib.unified_diff(
                    update.original_code.splitlines(),
                    update.updated_code.splitlines(),
                    fromfile=update.filename,
                    tofile=update.filename,
                    lineterm=""
                )
                diff_text = "\n".join(diff)
                await self.comm.send("diff", diff_text)

                # Handle user interaction for this specific update
                confirmed = False
                while not confirmed:
                    await self.comm.send("confirmation", f"Do you want to accept, discard, or provide feedback for the update for {update.filename}? (y/n/f)")
                    response = await self.comm.receive("confirmation")
                    choice = response.get("content", "").strip().lower()
                    
                    if choice == "f":
                        await self.comm.send("question", f"Please provide your feedback for the update of {update.filename}.")
                        feedback_response = await self.comm.receive("question")
                        feedback = feedback_response.get("content", "").strip()
                        await self.comm.send("log", f"User feedback for {update.filename}: {feedback}")
                        await self.comm.send("confirmation", f"Do you want to accept the update for {update.filename} now? (y/n)")
                        final_response = await self.comm.receive("confirmation")
                        final_choice = final_response.get("content", "").strip().lower()
                        
                        if final_choice == "y":
                            confirmed = True
                            try:
                                full_path = os.path.join(self.root_directory, update.filename)
                                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                                with open(full_path, "w", encoding="utf-8") as f:
                                    f.write(update.updated_code)
                                results.append(f"Updated {update.filename}. Feedback provided: {feedback}")
                                # Refresh repository stub
                                rm = RepoMap(self.root_directory)
                                rm.build_map()
                                self.repo_stub = rm.to_python_stub()
                            except Exception as e:
                                results.append(f"Failed to update {update.filename}: {e}")
                        else:
                            confirmed = True
                            results.append(f"Discarded update for {update.filename} after feedback. Feedback: {feedback}")
                    elif choice == "y":
                        confirmed = True
                        try:
                            full_path = os.path.join(self.root_directory, update.filename)
                            os.makedirs(os.path.dirname(full_path), exist_ok=True)
                            with open(full_path, "w", encoding="utf-8") as f:
                                f.write(update.updated_code)
                            results.append(f"Updated {update.filename}.")
                            # Refresh repository stub
                            rm = RepoMap(self.root_directory)
                            rm.build_map()
                            self.repo_stub = rm.to_python_stub()
                        except Exception as e:
                            results.append(f"Failed to update {update.filename}: {e}")
                    elif choice == "n":
                        confirmed = True
                        results.append(f"Discarded update for {update.filename}.")
                    else:
                        await self.comm.send("log", f"Invalid choice '{choice}'. Please enter 'y', 'n', or 'f'.")

            summary = "\n".join(results)
            await self.comm.send("log", f"[Tool Call: update_code] returned: {summary}")
            return summary

        async def ask_user_tool(ctx: RunContext[str], question: str) -> str:
            """Asks the user a question and returns the response."""
            await self.comm.send("question", question)
            try:
                # Specifically wait for a message of type "question"
                response = await self.comm.receive("question")
                return response.get("content", "")
            except Exception as e:
                await self.comm.send("error", f"Error getting user response: {str(e)}")
                return ""

        async def read_file_tool(ctx: RunContext[str], file_path: str) -> str:
            """Reads the content of a file."""
            # Ensure absolute path
            if not os.path.isabs(file_path):
                file_path = os.path.join(self.root_directory, file_path)
            await self.comm.send("log", f"[Tool Call: read_file] with filepath: {file_path}")
            content = get_file_content(file_path, root_directory=self.root_directory)
            return content

        async def search_tool(ctx: RunContext[str], search_terms: str) -> List[Dict[str, str]]:
            """Searches the codebase for the given search terms and returns relevant snippets with filenames."""
            await self.comm.send("log", f"[Tool Call: search] with search_terms: {search_terms}")
            try:
                snippets = await asyncio.to_thread(get_relevant_snippets, search_terms, self.root_directory)
                await self.comm.send("log", f"[Tool Call: search] found {len(snippets)} snippets.")
                return snippets
            except Exception as e:
                await self.comm.send("error", f"Search tool failed: {str(e)}")
                return []
                
        async def storm_analyze_problem_tool(ctx: RunContext[str], problem: str, context: Optional[str] = None) -> str:
            """
            Analyzes a problem using the CollaborativeStorm multi-agent architecture
            to provide a comprehensive analysis from multiple expert perspectives.
            
            Args:
                problem: The problem or question to analyze
                context: Additional context to inform the analysis (optional)
                
            Returns:
                A detailed analysis from multiple expert perspectives
            """
            if not self.use_storm or not self.storm_runner:
                await self.comm.send("log", "[Tool Call: storm_analyze_problem] STORM is not available, falling back to standard analysis")
                return f"Analysis of problem: {problem}\n\nSTORM analysis is not available. Please refer to the repository context to analyze this problem."
                
            await self.comm.send("log", f"[Tool Call: storm_analyze_problem] Analyzing problem: {problem}")
            
            try:
                # Update storm runner with appropriate topic
                self.storm_runner.runner_argument.topic = problem
                
                # Start analysis with a simulated user question
                initial_query = ConversationTurn(
                    role="Guest",
                    raw_utterance=problem,
                    utterance_type="Original Question"
                )
                
                # Reset conversation history and add initial query
                self.storm_runner.conversation_history = [initial_query]
                
                # Optional: Add context to knowledge base
                if context:
                    await self.comm.send("log", "[Tool Call: storm_analyze_problem] Adding context to knowledge base")
                    # Add context as a ConversationTurn from a system perspective
                    context_turn = ConversationTurn(
                        role="System",
                        raw_utterance=context,
                        utterance_type="Background Information"
                    )
                    self.storm_runner.knowledge_base.update_from_conv_turn(
                        conv_turn=context_turn,
                        allow_create_new_node=True
                    )
                
                # Run warm start to initialize collaborative agents
                await self.comm.send("log", "[Tool Call: storm_analyze_problem] Running warm start phase")
                self.storm_runner.warm_start()
                
                # Run a few steps of the analysis (limited to avoid excessive computation)
                analysis_steps = min(3, self.storm_runner.runner_argument.total_conv_turn)
                
                await self.comm.send("log", f"[Tool Call: storm_analyze_problem] Running {analysis_steps} analysis steps")
                for i in range(analysis_steps):
                    turn = self.storm_runner.step()
                    await self.comm.send("log", f"[STORM Step {i+1}] {turn.role}: {turn.raw_utterance[:100]}...")
                
                # Generate final report from knowledge base
                await self.comm.send("log", "[Tool Call: storm_analyze_problem] Generating final analysis")
                final_analysis = self.storm_runner.generate_report()
                
                # Get usage statistics
                usage = self.storm_lm_config.collect_and_reset_lm_usage()
                usage_data = {"model": "collaborative-storm", "usage": usage}
                await self.comm.send("usage", usage_data)
                
                # Log a summary of the analysis
                await self.comm.send("log", f"[Tool Call: storm_analyze_problem] Analysis complete: {len(final_analysis.split())} words")
                
                return final_analysis
                
            except Exception as e:
                error_msg = f"Error during STORM analysis: {str(e)}"
                await self.comm.send("error", error_msg)
                logger.exception("Error in storm_analyze_problem_tool")
                return f"Analysis failed: {str(e)}"

        # Register our wrapper functions as tools.
        self.agent.tool(create_plan_tool)
        self.agent.tool(update_code_tool)
        self.agent.tool(ask_user_tool)
        self.agent.tool(read_file_tool)
        self.agent.tool(search_tool)
        
        # Only register STORM tools if available
        if self.use_storm:
            self.agent.tool(storm_analyze_problem_tool)
            
    async def _get_storm_analysis(self, task: str, context: str) -> str:
        """
        Get a STORM analysis of the given task and context.
        This is used internally by update_code_tool to enhance code updates.
        
        Returns empty string if STORM is not available.
        """
        if not self.use_storm or not self.storm_runner:
            return ""
            
        try:
            # Update storm runner with appropriate topic
            self.storm_runner.runner_argument.topic = task
            
            # Start analysis with a simulated user question
            initial_query = ConversationTurn(
                role="Guest",
                raw_utterance=task,
                utterance_type="Original Question"
            )
            
            # Reset conversation history and add initial query
            self.storm_runner.conversation_history = [initial_query]
            
            # Add context to knowledge base
            context_turn = ConversationTurn(
                role="System",
                raw_utterance=context,
                utterance_type="Background Information"
            )
            self.storm_runner.knowledge_base.update_from_conv_turn(
                conv_turn=context_turn,
                allow_create_new_node=True
            )
            
            # Run warm start to initialize collaborative agents
            self.storm_runner.warm_start()
            
            # Run a single expert analysis step
            expert_turn = self.storm_runner.step()
            
            # Extract the expert analysis
            return expert_turn.raw_utterance
            
        except Exception as e:
            logger.error(f"Error getting STORM analysis: {e}")
            return ""

    async def run(self, user_prompt: str):
        """Starts the agentic process to solve the user request."""
        try:
            self.user_prompt = user_prompt  # Set the user_prompt attribute

            # Add notice if STORM is being used
            storm_status = "with CollaborativeStorm reasoning" if self.use_storm else "with standard reasoning"
            await self.comm.send("log", f"[StormOrchestratorAgent] Starting analysis {storm_status}")

            # Check if we should use DiscourseManager for this run
            should_use_discourse_manager = (self.use_storm and 
                                           self.discourse_manager is not None and
                                           self.use_discourse_manager)

            if should_use_discourse_manager:
                # Run using the DiscourseManager for a structured, multi-agent conversation
                await self.comm.send("log", "[StormOrchestratorAgent] Using DiscourseManager for structured conversation")
                await self.run_with_discourse_manager(user_prompt)
                await self.comm.send("completed", "Orchestration with DiscourseManager completed.")
            else:
                # Otherwise, use the standard pydantic_ai Agent approach
                initial_prompt = f"User Request: {self.user_prompt}\n\nRepository Context:\n{self.repo_stub}"
                response = await self.agent.run(initial_prompt)
                
                if response is None or response.data is None:
                    error_msg = "Agent returned no response"
                    await self.comm.send("error", error_msg)
                    return
                
                # Send token usage information
                await send_usage(self.comm, response, "orchestrator", self.MODEL_NAME)
                
                # If response.data is a tuple, join its parts; otherwise, use it as is
                final_response = "".join(response.data) if isinstance(response.data, tuple) else str(response.data)
                await self.comm.send("log", f"[Final Agent Response]:\n{final_response}")
                await self.comm.send("completed", "Orchestration completed.")

        except Exception as e:
            error_msg = f"Error during orchestration: {str(e)}"
            await self.comm.send("error", error_msg)
            logger.exception("Error in StormOrchestratorAgent.run")
            raise  # Re-raise the exception for proper logging in the server
            
    async def run_with_discourse_manager(self, user_prompt: str):
        """Run the agent using the DiscourseManager for a structured, multi-agent conversation flow."""
        try:
            # Initialize conversation with user prompt
            history = [
                ConversationTurn(
                    role="Guest",
                    raw_utterance=user_prompt,
                    utterance_type="Original Question"
                )
            ]
            
            # Add repository context to knowledge base
            context_turn = ConversationTurn(
                role="System",
                raw_utterance=f"Repository Context:\n{self.repo_stub}",
                utterance_type="Background Information"
            )
            self.discourse_manager.knowledge_base.update_from_conv_turn(
                conv_turn=context_turn,
                allow_create_new_node=True
            )
            
            # Setup the conversation parameters
            max_turns = int(os.getenv("MAX_STORM_TURNS", "5"))
            turn_count = 0
            
            await self.comm.send("log", f"[StormOrchestratorAgent] Starting collaborative conversation with {max_turns} max turns")
            
            # Use DiscourseManager to manage the conversation flow
            while turn_count < max_turns:
                turn_count += 1
                
                # Get next turn policy from discourse manager
                policy = self.discourse_manager.get_next_turn_policy(history)
                agent_name = policy.agent.__class__.__name__
                await self.comm.send("log", f"[Turn {turn_count}] Selected agent: {agent_name}")
                
                # Generate utterance based on the agent
                utterance = await self._generate_agent_utterance(policy.agent, history)
                
                # Create a new conversation turn
                new_turn = ConversationTurn(
                    role=policy.agent.role_name,
                    raw_utterance=utterance,
                    utterance_type=policy.utterance_type
                )
                
                # Add to history
                history.append(new_turn)
                
                # Send to the front-end
                await self.comm.send("log", f"[Turn {turn_count}: {policy.agent.role_name}] {utterance[:100]}...")
                
                # Check for stopping conditions
                if "FINAL ANSWER" in utterance or turn_count >= max_turns:
                    break
            
            # Generate a final summary from the conversation
            final_summary = await self._generate_final_summary(history)
            await self.comm.send("log", f"[Final Summary] {final_summary}")
            
            # Send token usage information
            usage = self.storm_lm_config.collect_and_reset_lm_usage()
            usage_data = {"model": "collaborative-storm-discourse", "usage": usage}
            await self.comm.send("usage", usage_data)
            
            return final_summary
        
        except Exception as e:
            error_msg = f"Error during discourse manager run: {str(e)}"
            await self.comm.send("error", error_msg)
            logger.exception("Error in StormOrchestratorAgent.run_with_discourse_manager")
            raise

    async def _generate_agent_utterance(self, agent, history):
        """Generate an utterance from the specified agent based on conversation history."""
        try:
            # Check if the agent has a generate_utterance method
            if hasattr(agent, "generate_utterance") and callable(getattr(agent, "generate_utterance")):
                # If the agent has a generate_utterance method, use it
                return await agent.generate_utterance(history)
            else:
                # Otherwise, fall back to using the model directly
                prompt = self._build_agent_prompt(agent, history)
                
                # Use the appropriate model for generation
                if self.use_mcp and hasattr(self.model, 'generate_text'):
                    response = await self.model.generate_text(prompt, max_tokens=1000)
                    return response
                elif self.use_ollama and hasattr(self.model, 'generate'):
                    response = await self.model.generate(prompt, max_tokens=1000)
                    return response.text
                else:
                    # Use OpenAI model
                    response = await self.model.generate(
                        prompt=prompt, 
                        max_tokens=1000,
                        temperature=0.7
                    )
                    return response.text
        except Exception as e:
            logger.exception(f"Error generating utterance for agent {agent.__class__.__name__}")
        return f"[Error generating response: {str(e)}]"

    async def _call_agent_generate_utterance(self, agent, history, knowledge_base=None):
        """Helper method to call agent.generate_utterance with knowledge_base if needed."""
        try:
            import inspect
            sig = inspect.signature(agent.generate_utterance)
            if 'knowledge_base' in sig.parameters:
                return await agent.generate_utterance(knowledge_base=knowledge_base, conversation_history=history)
            else:
                return await agent.generate_utterance(history)
        except Exception as e:
            logger.exception(f"Error in _call_agent_generate_utterance for {agent.__class__.__name__}")
            return f"[Error generating response: {str(e)}]"

    def _build_agent_prompt(self, agent, history):
        """Build a prompt for the agent based on conversation history."""
        # Construct a formatted history string
        history_text = "\n\n".join([
            f"{turn.role}: {turn.raw_utterance}" for turn in history
        ])
        
        # Create a system prompt for the agent
        system_prompt = f"You are {agent.role_name}, a {agent.role_description}. Please respond to the conversation below."
        
        # Combine system prompt and history
        full_prompt = f"{system_prompt}\n\nConversation History:\n{history_text}\n\n{agent.role_name}:"
        
        return full_prompt

    async def _generate_final_summary(self, history):
        """Generate a final summary of the conversation."""
        try:
            # Extract all agent utterances
            utterances = [
                f"{turn.role}: {turn.raw_utterance}" 
                for turn in history
            ]
            
            # Join the utterances
            conversation_log = "\n\n".join(utterances)
            
            # Generate a summary prompt
            summary_prompt = (
                "You are an AI assistant that summarizes collaborative discussions between experts. "
                "Below is a conversation history. Please provide a comprehensive summary of the key "
                "points, conclusions, and recommendations from this conversation.\n\n"
                f"Conversation History:\n{conversation_log}\n\nSummary:"
            )
            
            # Generate summary using the appropriate model
            if self.use_mcp and hasattr(self.model, 'generate_text'):
                response = await self.model.generate_text(summary_prompt, max_tokens=1500)
                return response
            elif self.use_ollama and hasattr(self.model, 'generate'):
                response = await self.model.generate(summary_prompt, max_tokens=1500)
                return response.text
            else:
                # Use OpenAI model
                response = await self.model.generate(
                    prompt=summary_prompt, 
                    max_tokens=1500,
                    temperature=0.7
                )
                return response.text
        except Exception as e:
            logger.exception("Error generating final summary")
            return f"[Error generating summary: {str(e)}]"