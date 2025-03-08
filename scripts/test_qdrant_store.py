"""Test script using Qdrant as vector store instead of local graph."""

from qdrant_client import QdrantClient
from agentic_research.collaborative_storm.discourse_manager import DiscourseManager
from agentic_research.collaborative_storm.lm_configs import CollaborativeStormLMConfigs
from agentic_research.collaborative_storm.runner_args import RunnerArgument
from agentic_research.interface import ConversationTurn
from test_utils import MockBingSearch, MockEncoder, MockCallbackHandler, MockLoggingWrapper

class QdrantStore:
    """Qdrant-based vector store implementation."""
    def __init__(self, url="http://localhost:6333"):
        self.client = QdrantClient(url)
        self.collection_name = "agentic_reasoning_test"
        
    def setup_collection(self):
        """Ensure collection exists."""
        collections = self.client.get_collections().collections
        exists = any(c.name == self.collection_name for c in collections)
        if not exists:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config={"size": 384, "distance": "Cosine"}
            )

def main():
    # Initialize vector store
    vector_store = QdrantStore()
    vector_store.setup_collection()
    
    # Initialize components
    lm_configs = CollaborativeStormLMConfigs()
    lm_configs.init(lm_type="openai", temperature=0.7, top_p=0.9)
    
    runner_args = RunnerArgument(
        topic="Palindromes in programming",
        disable_multi_experts=True,  # Disable expert generation to avoid graph dependencies
        rag_only_baseline_mode=False,
        disable_moderator=False,
        moderator_override_N_consecutive_answering_turn=2
    )
    
    logging_wrapper = MockLoggingWrapper()
    rm = MockBingSearch(api_key=None)
    encoder = MockEncoder()
    callback_handler = MockCallbackHandler()

    # Set up DiscourseManager
    dm = DiscourseManager(
        lm_config=lm_configs,
        runner_argument=runner_args,
        logging_wrapper=logging_wrapper,
        rm=rm,
        encoder=encoder,
        callback_handler=callback_handler
    )

    # Simulate a 3-turn conversation
    print("\nStarting conversation simulation...")
    
    # Initial question from user
    history = [
        ConversationTurn(
            role="Guest",
            raw_utterance="What is a palindrome?",
            utterance_type="Original Question"
        )
    ]
    print(f"\nTurn 1 - {history[0].role}: {history[0].raw_utterance}")

    # Get responses for next 2 turns
    for turn in range(2):
        policy = dm.get_next_turn_policy(history, simulate_user=False)
        response = f"{policy.agent.role_name} explains palindromes"
        history.append(
            ConversationTurn(
                role=policy.agent.role_name,
                raw_utterance=response,
                utterance_type="Response"
            )
        )
        print(f"\nTurn {turn + 2} - {policy.agent.role_name}:")
        print(f"Action: {policy}")
        print(f"Response: {response}")

    print("\nConversation simulation completed.")

if __name__ == "__main__":
    main()