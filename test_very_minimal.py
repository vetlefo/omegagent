"""Very minimal test script to verify just our changes to import paths."""

import sys
import importlib
import types

# Create mock modules for any dependencies we don't want to load
mock_modules = [
    'nano_graphrag', 
    'langchain',
    'langchain.tools',
    'dspy',
    'agentic_research.storm_analysis',
]

for mod_name in mock_modules:
    if mod_name not in sys.modules:
        sys.modules[mod_name] = types.ModuleType(mod_name)
        # For submodules, make sure parent modules exist
        if '.' in mod_name:
            parent = mod_name.rsplit('.', 1)[0]
            if parent not in sys.modules:
                sys.modules[parent] = types.ModuleType(parent)
            setattr(sys.modules[parent], mod_name.rsplit('.', 1)[1], sys.modules[mod_name])

# Mock GraphRAG and QueryParam
class MockGraphRAG:
    def __init__(self, working_dir=None):
        pass
    def insert(self, content):
        pass
    def query(self, query, param=None):
        return "Mock query result"

class MockQueryParam:
    def __init__(self, mode=None):
        self.mode = mode

# Add these to the mock nano_graphrag module
sys.modules['nano_graphrag'].GraphRAG = MockGraphRAG
sys.modules['nano_graphrag'].QueryParam = MockQueryParam

# Also create a mock for BaseTool
class MockBaseTool:
    pass

sys.modules['langchain.tools'].BaseTool = MockBaseTool
sys.modules['langchain.tools'].StructuredTool = MockBaseTool
sys.modules['langchain.tools'].tool = lambda x: x

# Functions to directly import and verify the specific modules and classes
def test_interface_imports():
    try:
        # Direct import of the module without going through __init__
        spec = importlib.util.find_spec('agentic_research.interface')
        interface_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(interface_module)
        
        # Check if our class exists in the module
        assert hasattr(interface_module, 'Agent'), "Agent class not found"
        assert hasattr(interface_module, 'ConversationTurn'), "ConversationTurn class not found"
        assert hasattr(interface_module, 'KnowledgeBase'), "KnowledgeBase class not found"
        
        print("✅ Interface imports verified successfully")
        return True
    except Exception as e:
        print(f"❌ Interface imports verification failed: {e}")
        return False

def test_turn_policy_imports():
    try:
        # Direct import of the module without going through __init__
        spec = importlib.util.find_spec('agentic_research.collaborative_storm.turn_policy')
        turn_policy_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(turn_policy_module)
        
        # Check if our class exists in the module
        assert hasattr(turn_policy_module, 'TurnPolicySpec'), "TurnPolicySpec class not found"
        
        print("✅ TurnPolicySpec imports verified successfully")
        return True
    except Exception as e:
        print(f"❌ TurnPolicySpec imports verification failed: {e}")
        return False

def test_co_storm_agents_imports():
    try:
        # Direct import of the module without going through __init__
        spec = importlib.util.find_spec('agentic_research.collaborative_storm.modules.co_storm_agents')
        co_storm_agents_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(co_storm_agents_module)
        
        # Check if our classes exist in the module
        assert hasattr(co_storm_agents_module, 'SimulatedUser'), "SimulatedUser class not found"
        assert hasattr(co_storm_agents_module, 'PureRAGAgent'), "PureRAGAgent class not found"
        assert hasattr(co_storm_agents_module, 'Moderator'), "Moderator class not found"
        assert hasattr(co_storm_agents_module, 'CoStormExpert'), "CoStormExpert class not found"
        
        print("✅ Co_storm_agents imports verified successfully")
        return True
    except Exception as e:
        print(f"❌ Co_storm_agents imports verification failed: {e}")
        return False

# Run the tests
print("\n==== Testing Import Paths ====\n")
interface_success = test_interface_imports()
turn_policy_success = test_turn_policy_imports()
co_storm_agents_success = test_co_storm_agents_imports()

if interface_success and turn_policy_success and co_storm_agents_success:
    print("\n✅ All import paths verified successfully!")
else:
    print("\n❌ Some import paths failed verification")