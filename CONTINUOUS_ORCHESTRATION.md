# Continuous Orchestration Implementation

Based on our analysis of the orchestration issues, here's a proposal to prevent the conversation from resetting and allow continuous feedback between the agent and user.

## Current Issue

The current implementation has these key issues that prevent continuous interaction:

1. **Task Completion**: Once the agent completes a task, the orchestration ends with a "completed" message, which resets the conversation.
2. **No Feedback Loop**: After the agent generates a response, there's no mechanism to provide feedback or continue the conversation.
3. **Fixed Orchestration Cycle**: The orchestration follows a linear process: receive prompt → process → complete, with no path for circularity.

## Proposed Solution

### 1. Modify the `run` Method in OrchestratorAgent

Replace the current completion message with a continuation mechanism:

```python
async def run(self, user_prompt: str):
    """Starts the agentic process to solve the user request."""
    try:
        self.user_prompt = user_prompt  # Set the user_prompt attribute
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
        await self.comm.send("log", f"[Agent Response]:\n{final_response}")
        
        # Ask if the user wants to continue the conversation instead of ending it
        await self.comm.send("continue", {
            "message": final_response,
            "options": ["Continue with feedback", "Complete this task"]
        })
        
        # Wait for user's decision
        continue_response = await self.comm.receive("continue")
        choice = continue_response.get("content", "").lower()
        
        if "continue" in choice or "feedback" in choice:
            # Get the user's feedback
            await self.comm.send("question", "What feedback or follow-up would you like to provide?")
            feedback = await self.comm.receive("question")
            feedback_text = feedback.get("content", "")
            
            # Start a new orchestration with the feedback
            new_prompt = f"User's original request: {self.user_prompt}\n\nMy previous response: {final_response}\n\nUser's feedback: {feedback_text}"
            
            # Recursive call with the new prompt
            return await self.run(new_prompt)
        else:
            # Complete the orchestration if user doesn't want to continue
            await self.comm.send("completed", "Orchestration completed successfully.")
            
    except Exception as e:
        error_msg = f"Error during orchestration: {str(e)}"
        await self.comm.send("error", error_msg)
        raise  # Re-raise the exception for proper logging in the server
```

### 2. Modify the WebSocket Handler

Update the WebSocket endpoint to support the continuous conversation flow:

```python
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # ... existing code ...
    
    # Change this part:
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
        # Don't send the completion message here, let the orchestrator handle it
        # await comm.send("completed", "Orchestration completed successfully.")
        
    # Add a loop to keep the websocket alive after task completion
    while True:
        try:
            # Wait for any message
            message = await comm.receive("default")
            
            # Check if it's a new prompt to continue conversation
            if message.get("type") == "continue":
                new_prompt = message.get("content", "")
                if new_prompt:
                    logger.info(f"Continuing conversation with: {new_prompt}")
                    orchestration_task = asyncio.create_task(orchestrator.run(new_prompt))
                    stop_task = asyncio.create_task(listen_for_stop(comm))
                    
                    done, pending = await asyncio.wait(
                        [orchestration_task, stop_task], return_when=asyncio.FIRST_COMPLETED
                    )
                    
                    if stop_task in done:
                        if not orchestration_task.done():
                            orchestration_task.cancel()
                    else:
                        stop_task.cancel()
            
            # Handle explicit close request
            elif message.get("type") == "close":
                logger.info("Received close request")
                break
                
        except WebSocketDisconnect:
            logger.info("WebSocket client disconnected.")
            break
        except Exception as e:
            logger.error(f"Error in continuous websocket: {e}")
            await comm.send("error", f"Error: {str(e)}")
```

### 3. Add Frontend Support for Continuous Conversation

```javascript
// When receiving a "continue" message type
socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    
    if (data.type === "continue") {
        // Show options to the user
        const options = data.content.options;
        
        // Create buttons for each option
        const optionButtons = options.map(option => {
            const button = document.createElement("button");
            button.textContent = option;
            button.onclick = () => {
                // Send the selected option back
                socket.send(JSON.stringify({
                    type: "continue",
                    content: option
                }));
            };
            return button;
        });
        
        // Display message and options to the user
        displayMessage(data.content.message);
        displayOptions(optionButtons);
    }
    
    // Handle question message type for feedback
    else if (data.type === "question") {
        // Show input field for feedback
        const feedbackForm = createFeedbackForm(response => {
            socket.send(JSON.stringify({
                type: "question",
                content: response
            }));
        });
        
        displayFeedbackForm(feedbackForm);
    }
    
    // Other message types...
};
```

## Benefits of This Approach

1. **Continuous Conversation**: The conversation doesn't end after a single response, allowing for iterations and refinement.

2. **User Control**: Users can choose when to end the conversation, rather than having it end automatically.

3. **Feedback Loop**: Direct feedback mechanism allows users to guide the AI's responses.

4. **Context Preservation**: The full conversation history is maintained, helping the agent understand follow-up requests.

5. **Graceful WebSocket Handling**: The WebSocket connection stays open but is properly managed with explicit close paths.

## Implementation Strategy

1. Update `OrchestratorAgent` to support the feedback loop
2. Modify the WebSocket handler to maintain the connection
3. Update the frontend to handle the new message types
4. Add proper error handling and connection management

This approach creates a much more interactive and conversational system that can maintain context across multiple exchanges, even if the WebSocket connection is refreshed.