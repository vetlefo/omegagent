import unittest from agentic_research.collaborative_storm.discourse_manager import DiscourseManager from agentic_research.collaborative_storm.lm_configs import CollaborativeStormLMConfigs from agentic_research.collaborative_storm.runner_args import RunnerArgument from agentic_research.logging_wrapper import LoggingWrapper from agentic_research.rm import BingSearch from agentic_research.encoder import Encoder from agentic_research.collaborative_storm.modules.callback import LocalConsolePrintCallBackHandler from agentic_research.dataclass import ConversationTurn
class TestDiscourseManager(unittest.TestCase):
def setUp(self):
self.lm_configs = CollaborativeStormLMConfigs()
self.lm_configs.init(lm_type="openai", temperature=0.7, top_p=0.9)
self.runner_args = RunnerArgument(topic="Test Topic")
self.logging_wrapper = LoggingWrapper()
self.rm = BingSearch(api_key=None)  # Mocked
self.encoder = Encoder()
self.callback_handler = LocalConsolePrintCallBackHandler()
self.dm = DiscourseManager(
lm_config=self.lm_configs,
runner_argument=self.runner_args,
logging_wrapper=self.logging_wrapper,
rm=self.rm,
encoder=self.encoder,
callback_handler=self.callback_handler
)

def test_initialization(self):
self.assertIsNotNone(self.dm.simulated_user)
self.assertIsNotNone(self.dm.moderator)
self.assertIsNotNone(self.dm.pure_rag_agent)
self.assertIsNotNone(self.dm.general_knowledge_provider)
self.assertEqual(len(self.dm.experts), 0)

def test_get_next_turn_policy(self):
history = [ConversationTurn(role="Guest", raw_utterance="Test question", utterance_type="Original Question")]
policy = self.dm.get_next_turn_policy(history, dry_run=True)
self.assertIsNotNone(policy.agent)
self.assertIn(policy.agent.role_name, ["PureRAG", "Moderator", "General Knowledge Provider"])

if name == "main":
unittest.main()