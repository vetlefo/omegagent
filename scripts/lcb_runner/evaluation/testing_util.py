# This file was created to provide the run_test function needed by compute_code_generation_metrics.py
import json
import os
import tempfile
from .utils_execute import check_correctness

def run_test(sample, test, debug=False, timeout=6):
    """
    Run test cases for a given code sample.
    
    Args:
        sample: The sample containing input_output test cases
        test: The code to test
        debug: Whether to print debug information
        timeout: Timeout for each test case
        
    Returns:
        A list of test results and metadata
    """
    try:
        input_output = json.loads(sample["input_output"])
        inputs = input_output["inputs"]
        outputs = input_output["outputs"]
        
        results = []
        for i, (input_case, expected_output) in enumerate(zip(inputs, outputs)):
            # Create a test program that runs the code with the input
            test_program = f"""
{test}

# Test case {i}
input_case = {repr(input_case)}
expected_output = {repr(expected_output)}
result = None
try:
    # Assuming the function is called 'solution'
    result = solution(input_case)
    assert result == expected_output, f"Expected {{expected_output}}, got {{result}}"
except Exception as e:
    raise Exception(f"Test case {i} failed: {{e}}")
"""
            
            if debug:
                print(f"Running test case {i}")
                print(test_program)
                
            # Run the test
            passed = check_correctness(test_program, timeout=timeout)
            results.append(passed)
            
            if debug:
                print(f"Test case {i} result: {passed}")
                
        metadata = {
            "results": results,
            "num_tests": len(inputs),
            "passed": sum(results),
            "failed": len(inputs) - sum(results)
        }
        
        return results, metadata
        
    except Exception as e:
        if debug:
            print(f"Error running tests: {e}")
        return [-1], {"error": str(e), "error_code": -1, "error_message": str(e)}
