"""Test script that adds the current directory to the Python path."""

import os
import sys

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
    print(f"Added {current_dir} to Python path")

# Minimal test of our import changes
try:
    print("\nImporting from interface.py...")
    import agentic_research.interface
    print("Successfully imported agentic_research.interface module")
    
    # Check for specific classes
    if hasattr(agentic_research.interface, 'Agent'):
        print("✅ Agent class is available")
    if hasattr(agentic_research.interface, 'ConversationTurn'):
        print("✅ ConversationTurn class is available")
    if hasattr(agentic_research.interface, 'KnowledgeBase'):
        print("✅ KnowledgeBase class is available")
except Exception as e:
    print(f"❌ Failed to import from interface.py: {e}")

try:
    print("\nImporting from turn_policy.py...")
    import agentic_research.collaborative_storm.turn_policy
    print("Successfully imported turn_policy module")
    
    # Check for TurnPolicySpec
    if hasattr(agentic_research.collaborative_storm.turn_policy, 'TurnPolicySpec'):
        print("✅ TurnPolicySpec class is available")
except Exception as e:
    print(f"❌ Failed to import from turn_policy.py: {e}")

try:
    print("\nImporting from co_storm_agents.py...")
    import agentic_research.collaborative_storm.modules.co_storm_agents
    print("Successfully imported co_storm_agents module")
    
    # Check for specific classes
    module = agentic_research.collaborative_storm.modules.co_storm_agents
    if hasattr(module, 'SimulatedUser'):
        print("✅ SimulatedUser class is available")
    if hasattr(module, 'PureRAGAgent'):
        print("✅ PureRAGAgent class is available")
    if hasattr(module, 'Moderator'): 
        print("✅ Moderator class is available")
    if hasattr(module, 'CoStormExpert'):
        print("✅ CoStormExpert class is available")
except Exception as e:
    print(f"❌ Failed to import from co_storm_agents.py: {e}")