from agentic_research.collaborative_storm.discourse_manager import DiscourseManager
from agentic_research.collaborative_storm.lm_configs import CollaborativeStormLMConfigs
from agentic_research.collaborative_storm.runner_args import RunnerArgument
from agentic_research.logging_wrapper import LoggingWrapper
from agentic_research.rm import BingSearch
from agentic_research.encoder import Encoder
from agentic_research.collaborative_storm.modules.callback import LocalConsolePrintCallBackHandler
from agentic_research.dataclass import ConversationTurn

def main():
    # Initialize components
    lm_configs = CollaborativeStormLMConfigs()
    lm_configs.init(lm_type="openai", temperature=0.7, top_p=0.9)
    runner_args = RunnerArgument(topic="Palindromes in programming")
    logging_wrapper = LoggingWrapper()
    rm = BingSearch(api_key=None)  # Mocked; replace with real key if needed
    encoder = Encoder()
    callback_handler = LocalConsolePrintCallBackHandler()

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
    history = [ConversationTurn(role="Guest", raw_utterance="What is a palindrome?", utterance_type="Original Question")]
    for _ in range(3):
        policy = dm.get_next_turn_policy(history, simulate_user=False)
        print(f"Agent: {policy.agent.role_name}, Action: {policy}")
        history.append(ConversationTurn(role=policy.agent.role_name, raw_utterance=f"{policy.agent.role_name} responds", utterance_type="Response"))

if __name__ == "__main__":
    main()