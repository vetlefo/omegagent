"""Minimal test script to verify only our specific import paths."""

import importlib.util
import sys
from importlib.abc import Loader

# Mock the nano_graphrag module to prevent import errors
class MockLoader(Loader):
    def create_module(self, spec):
        return type('MockModule', (), {})
    
    def exec_module(self, module):
        pass

# Register our mock for nano_graphrag
mock_spec = importlib.machinery.ModuleSpec('nano_graphrag', MockLoader())
sys.modules['nano_graphrag'] = importlib.util.module_from_spec(mock_spec)

# Now test our specific imports
try:
    # Import specific classes
    from agentic_research.interface import Agent, ConversationTurn, KnowledgeBase
    from agentic_research.collaborative_storm.turn_policy import TurnPolicySpec
    from agentic_research.collaborative_storm.modules.co_storm_agents import (
        SimulatedUser, PureRAGAgent, Moderator, CoStormExpert
    )
    
    print("✅ All imports successful!")
    
    # Check that these classes are actually the ones we expect
    print("\nVerifying class imports:")
    print(f"- Agent is imported from: {Agent.__module__}")
    print(f"- TurnPolicySpec is imported from: {TurnPolicySpec.__module__}")
    print(f"- SimulatedUser is imported from: {SimulatedUser.__module__}")
    print(f"- PureRAGAgent is imported from: {PureRAGAgent.__module__}")
    print(f"- Moderator is imported from: {Moderator.__module__}")
    print(f"- CoStormExpert is imported from: {CoStormExpert.__module__}")
    print(f"- ConversationTurn is imported from: {ConversationTurn.__module__}")
    print(f"- KnowledgeBase is imported from: {KnowledgeBase.__module__}")
    
except Exception as e:
    print(f"❌ Import test failed: {e}")