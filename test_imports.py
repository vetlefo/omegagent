"""Test script to verify our import changes."""

# Directly import from the files we modified
try:
    print("Testing imports from interface.py...")
    from agentic_research.interface import Agent, ConversationTurn, KnowledgeBase
    print("✅ Interface imports successful")
except Exception as e:
    print(f"❌ Interface imports failed: {e}")

try:
    print("\nTesting imports from discourse_manager.py...")
    from agentic_research.collaborative_storm.discourse_manager import DiscourseManager
    print("✅ Discourse manager imports successful")
except Exception as e:
    print(f"❌ Discourse manager imports failed: {e}")

try:
    print("\nTesting imports from co_storm_agents.py...")
    from agentic_research.collaborative_storm.modules.co_storm_agents import (
        SimulatedUser, PureRAGAgent, Moderator, CoStormExpert
    )
    print("✅ Co_storm_agents imports successful")
except Exception as e:
    print(f"❌ Co_storm_agents imports failed: {e}")

try:
    print("\nTesting imports from turn_policy.py...")
    from agentic_research.collaborative_storm.turn_policy import TurnPolicySpec
    print("✅ Turn policy imports successful")
except Exception as e:
    print(f"❌ Turn policy imports failed: {e}")

print("\nAll import tests completed.")
