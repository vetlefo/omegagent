from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
import asyncio
from backend.repo_map import RepoMap
from backend.agents.orchestrator_agent import OrchestratorAgent
from backend.agents.storm_orchestrator_agent import StormOrchestratorAgent
from backend.communication import WebSocketCommunicator
from backend.agents.coder_agent import CoderAgent
from agentic_research.collaborative_storm.discourse_manager import DiscourseManager
try:
    import dspy
    from dspy.backends.openai import OpenAIBackend
except ImportError:
    dspy = None
from backend.utils import get_file_content
import logging

# Load environment variables
load_dotenv()

# Validate required environment variables
required_vars = ['OPENAI_API_KEY', 'GEMINI_API_KEY']
missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize LM and coder agent
if dspy is not None:
    try:
        # Use the available DSPy 2.6.x API
        from openai import OpenAI as OpenAIClient
        
        # Create a simple LM class that wraps OpenAI - compatible with CoderAgent
        class DSPyOpenAIWrapper:
            def __init__(self, model="gpt-4"):
                self.model = model
                self.client = OpenAIClient()
                
            def __call__(self, prompt, **kwargs):
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                )
                return response.choices[0].message.content
        
        # Initialize DSPy global configuration
        dspy.settings.configure(lm=DSPyOpenAIWrapper(model="gpt-4"))
        
        # For CoderAgent we need the same model object
        lm = DSPyOpenAIWrapper(model="gpt-4")
        logger.info("Using custom DSPyOpenAIWrapper for coder agent")
    except Exception as e:
        logger.error(f"Error initializing DSPy: {e}")
        # Fallback to pydantic_ai
        from pydantic_ai.models.openai import OpenAIModel
        lm = OpenAIModel("gpt-4")
        logger.warning(f"DSPy initialization failed, using pydantic_ai.models.openai.OpenAIModel instead. Error: {e}")
else:
    # Fallback to a mock LM if dspy is not available
    from pydantic_ai.models.openai import OpenAIModel
    lm = OpenAIModel("gpt-4")
    logger.warning("dspy not available, using pydantic_ai.models.openai.OpenAIModel instead")

coder_agent = CoderAgent(lm=lm, logger=logger)
app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")


# Serve the frontend page.
@app.get("/")
async def get_index():
    logger.info("Received request for index page.")
    try:
        with open(os.path.join(os.getcwd(), "frontend/index.html"), "r", encoding="utf-8") as f:
            html_content = f.read()
        logger.info("Successfully read index.html.")
        return HTMLResponse(html_content)
    except Exception as e:
        logger.error(f"Error serving index page: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")



async def listen_for_stop(comm: WebSocketCommunicator):
    """
    Listen for a stop command from the frontend.
    Assumes that a message with {"type": "stop"} is sent.
    """
    message = await comm.receive("stop")
    # If None is returned, the connection is likely closed
    if message is None:
        logger.info("No stop message received or connection closed")
        return {"type": "stop", "content": "Connection closed"}
    return message

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    logger.info("WebSocket connection initiated.")
    await websocket.accept()
    comm = WebSocketCommunicator(websocket)
    orchestration_task = None
    
    try:
        # Start the message router and wait for it to be ready
        await comm.start()
        logger.info("WebSocket communicator started.")
        
        # Wait for the initial message containing the user request
        init_msg = await comm.receive("default")
        if not init_msg:
            logger.error("No initial message received or connection was closed")
            await comm.send("error", "Connection issue or no initial message received")
            return
            
        user_prompt = init_msg.get("content", "")
        if not user_prompt:
            logger.error("No user prompt in initial message")
            await comm.send("error", "No user prompt provided in message")
            return

        logger.info(f"Received user prompt: {user_prompt}")

        # Extract config from init message
        config = init_msg.get("config", {})
        review = config.get("review", True)
        max_iterations = config.get("max_iterations", 1)
        root_directory = config.get("root_directory", ".")
        logger.info(f"Received root_directory: {root_directory}")

        # Extract additional config options for enhanced features
        use_storm = config.get("use_storm", False)
        include_semantic_relationships = config.get("include_semantic_relationships", False)
        use_mcp = config.get("use_mcp", False)
        use_ollama = config.get("use_ollama", False)
        
        # Build the repository map and generate the stub.
        rm = RepoMap(root_directory, use_semantic_analysis=include_semantic_relationships)
        rm.build_map()
        
        # Generate stub with semantic relationships if requested
        if include_semantic_relationships:
            repo_stub = rm.to_python_stub(include_semantic_relationships=True)
            logger.info("Repository map built with semantic relationships")
        else:
            repo_stub = rm.to_python_stub()
            logger.info("Repository map built (standard)")
            
        # Check if we should use StormOrchestratorAgent or standard OrchestratorAgent
        if use_storm and os.getenv("USE_STORM", "false").lower() == "true":
            logger.info("Creating StormOrchestratorAgent for enhanced reasoning")
            orchestrator = StormOrchestratorAgent(
                repo_stub, 
                comm, 
                review=review, 
                max_iterations=max_iterations, 
                root_directory=root_directory,
                use_storm=True,
                include_semantic_relationships=include_semantic_relationships,
                use_mcp=use_mcp,
                use_ollama=use_ollama
            )
            await comm.send("log", "Starting orchestration with CollaborativeStorm reasoning...")
        else:
            logger.info("Creating standard OrchestratorAgent")
            orchestrator = OrchestratorAgent(
                repo_stub, 
                comm, 
                review=review, 
                max_iterations=max_iterations, 
                root_directory=root_directory
            )
        await comm.send("log", "Starting orchestration...")
        logger.info("Starting orchestration.")
        
        # Start the orchestration task and stop listener
        orchestration_task = asyncio.create_task(orchestrator.run(user_prompt))
        stop_task = asyncio.create_task(listen_for_stop(comm))
        
        # Wait until one of the tasks completes
        done, pending = await asyncio.wait(
            [orchestration_task, stop_task], return_when=asyncio.FIRST_COMPLETED
        )
        
        if stop_task in done:
            if not orchestration_task.done():
                orchestration_task.cancel()
                await comm.send("log", "Orchestration cancelled by user.")
                logger.info("Orchestration cancelled by user.")
        else:
            stop_task.cancel()
            await comm.send("completed", "Orchestration completed successfully.")
            
    except WebSocketDisconnect:
        logger.info("WebSocket client disconnected.")
    except asyncio.CancelledError:
        logger.info("Orchestration task cancelled.")
    except Exception as e:
        logger.error(f"Error in WebSocket communication: {str(e)}")
        await comm.send("error", str(e))
    finally:
        await comm.stop()
        if orchestration_task and not orchestration_task.done():
            orchestration_task.cancel()

@app.post("/generate_code")
async def generate_code(prompt: str, context: str | None = None):
    """API endpoint to generate code."""
    code = coder_agent.generate_code(prompt, context)
    return {"code": code}
