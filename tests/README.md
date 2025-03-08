# Testing Framework for Agentic-Reasoning-Master

This directory contains the testing infrastructure for the Agentic-Reasoning-Master project.

## Directory Structure

- `unit/`: Unit tests for individual components and classes
- `integration/`: Integration tests that test multiple components working together
- `utils/`: Test utilities and mock objects

## Running Tests

You can run all tests using pytest:

```bash
pytest -v
```

Or run specific test categories:

```bash
# Run only unit tests
pytest -v tests/unit/

# Run only integration tests
pytest -v tests/integration/

# Run tests with coverage report
pytest --cov=agentic_research tests/
```

## Test Files

### Unit Tests
- `test_discourse_manager.py`: Tests for the DiscourseManager component

### Integration Tests
- `test_agentic_reasoning.py`: Tests the entire DiscourseManager functionality
- `test_minimal.py`: Minimal test setup with dummy modules
- `test_qdrant_store.py`: Tests integration with Qdrant vector store

### Utilities
- `test_utils.py`: Mock classes for testing (BingSearch, Encoder, etc.)

## Writing Tests

When adding new tests:

1. **Unit tests** should be placed in the `unit/` directory and focus on testing a single component in isolation.
2. **Integration tests** should be placed in the `integration/` directory and test how components work together.
3. **Test utilities** should be placed in the `utils/` directory.

All test files should begin with `test_` and test functions should also begin with `test_`.

## Mock Objects

The `utils/test_utils.py` file contains mock implementations of:
- MockBingSearch
- MockEncoder
- MockCallbackHandler
- MockLoggingWrapper

These can be used to isolate components for testing without external dependencies.