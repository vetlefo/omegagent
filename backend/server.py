from fastapi import FastAPI, WebSocket
from backend.agents.coder_agent import CoderAgent
from agentic_research.collaborative_storm.discourse_manager import DiscourseManager
import dspy
import logging
import asyncio

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Initialize components
lm = dspy.OpenAI(model="gpt-4")
coder_agent = CoderAgent(lm=lm, logger=logger)
discourse_manager = DiscourseManager()

@app.get("/")
async def root():
    return {"message": "AI Codepilot Server"}

@app.websocket("/ws/discourse")
async def websocket_endpoint(websocket: WebSocket):
    """Stream DiscourseManager actions to the frontend."""
    await websocket.accept()
    try:
        while True:
            # Simulate DiscourseManager updates (replace with actual logic)
            action = discourse_manager.get_latest_action()
            if action:
                await websocket.send_json({"action": action})
            await asyncio.sleep(1)  # Poll every second
    except Exception as e:
        await websocket.close()
        logger.error(f"WebSocket error: {e}")

@app.post("/generate_code")
async def generate_code(prompt: str, context: str | None = None):
    """API endpoint to generate code."""
    code = coder_agent.generate_code(prompt, context)
    return {"code": code}

# Assume DiscourseManager has a method to get latest action
# This is a placeholder; integrate actual DiscourseManager logic as needed
