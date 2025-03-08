"""Minimal test script using MinimalDiscourseManager and MinimalLMConfigs.

All necessary dummy modules for 'agentic_research.storm_analysis' and its submodules are injected
at the very beginning to bypass external dependencies.
"""

import sys
import types

# Inject dummy modules BEFORE any other imports occur
dummy_storm_analysis = types.ModuleType("agentic_research.storm_analysis")
dummy_storm_analysis.__dict__["__all__"] = []
sys.modules["agentic_research.storm_analysis"] = dummy_storm_analysis

dummy_storm_analysis_modules = types.ModuleType("agentic_research.storm_analysis.modules")
dummy_storm_analysis_modules.__dict__["__all__"] = []
sys.modules["agentic_research.storm_analysis.modules"] = dummy_storm_analysis_modules

# Inject dummy for 'agentic_research.storm_analysis.modules.knowledge_curation'
dummy_knowledge_curation = types.ModuleType("agentic_research.storm_analysis.modules.knowledge_curation")
dummy_knowledge_curation.AskQuestionWithPersona = lambda *args, **kwargs: None
sys.modules["agentic_research.storm_analysis.modules.knowledge_curation"] = dummy_knowledge_curation

# Inject dummy for 'agentic_research.storm_analysis.modules.outline_generation'
dummy_outline_generation = types.ModuleType("agentic_research.storm_analysis.modules.outline_generation")
dummy_outline_generation.WritePageOutline = lambda *args, **kwargs: None
sys.modules["agentic_research.storm_analysis.modules.outline_generation"] = dummy_outline_generation

# Now import pydantic and override its BaseModel config
import pydantic
pydantic.BaseModel.model_config = {"arbitrary_types_allowed": True}

from minimal_lm_configs import MinimalLMConfigs
from agentic_research.collaborative_storm.runner_args import RunnerArgument
from agentic_research.dataclass import ConversationTurn
from test_utils import MockBingSearch, MockEncoder, MockCallbackHandler, MockLoggingWrapper
from minimal_discourse_manager import MinimalDiscourseManager

def main():
    # Initialize minimal LM configurations
    lm_configs = MinimalLMConfigs()
    lm_configs.init(lm_type="openai", temperature=0.7, top_p=0.9)
    
    runner_args = RunnerArgument(
        topic="Palindromes in programming",
        disable_multi_experts=True,  # Disable expert generation to avoid additional dependencies
        rag_only_baseline_mode=False,
        disable_moderator=False,
        moderator_override_N_consecutive_answering_turn=2
    )
    
    logging_wrapper = MockLoggingWrapper()
    rm = MockBingSearch(api_key=None)
    encoder = MockEncoder()
    callback_handler = MockCallbackHandler()

    # Set up MinimalDiscourseManager
    dm = MinimalDiscourseManager(
        lm_config=lm_configs,
        runner_argument=runner_args,
        logging_wrapper=logging_wrapper,
        rm=rm,
        encoder=encoder,
        callback_handler=callback_handler
    )

    # Simulate a 3-turn conversation
    print("\nStarting conversation simulation with minimal setup...")
    
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