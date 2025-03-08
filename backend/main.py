# main.py
import uvicorn
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        uvicorn.run("backend.server:app", host="0.0.0.0", port=8000, reload=False)
    except Exception as e:
        logger.exception(f"Error during server startup: {e}")
