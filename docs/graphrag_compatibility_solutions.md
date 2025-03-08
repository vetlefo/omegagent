# nano_graphrag Compatibility Solutions

## Issue Summary

During the setup of the Agentic Reasoning project, an issue was encountered while trying to install the `nano_graphrag` dependency and its dependency chain (`gensim`, `scipy`). The root cause appears to be compatibility issues related to the need for a Fortran compiler.

## Minimal Testing Approach

To work around this issue and verify the core functionality of the `DiscourseManager` component, a minimal testing approach was implemented. This approach bypasses the graph-related features and dependencies, allowing for basic testing and development to proceed.

The minimal testing approach includes the following files:

- `scripts/minimal_lm_configs.py`: Minimal LM configuration module with dummy model initializations.
- `scripts/minimal_discourse_manager.py`: Stripped-down `DiscourseManager` implementation without graph dependencies.
- `scripts/test_minimal.py`: Test script using the minimal components and injecting dummy modules to bypass graph imports.
- `scripts/test_utils.py`: Helper module with mock classes for components like `BingSearch`, `Encoder`, etc.

To run the minimal test:

```bash
python scripts/test_minimal.py
```

This will simulate a 3-turn conversation between a "Guest" and the "General Knowledge Provider" agent, verifying the core turn policy determination and agent interaction.

## Suggested Solutions

Here are some potential solutions to address the `nano_graphrag` compatibility issue:

1. **Remote GPU or Cloud Service**: Explore the possibility of using a remote GPU or cloud service like Google Colab, which may have the necessary dependencies pre-installed or easier to set up. This could involve running the project remotely or offloading the graph-related computations to the remote environment.

2. **Alternative Graph Libraries**: Investigate alternative graph libraries or implementations that may have fewer dependency conflicts or be easier to set up in the current environment. Some options to research could include NetworkX, igraph, or other Python graph libraries.

3. **Reach Out to nano_graphrag Developers**: Contact the developers of the `nano_graphrag` library for support and guidance on resolving the compatibility issues. They may have additional insights or workarounds specific to the project's environment.

4. **Fortran Compiler Setup**: If the above solutions are not feasible or successful, revisit the setup for installing a Fortran compiler (e.g., gfortran) on the specific operating system. Ensure that all system-level dependencies are properly configured to enable the successful installation of `nano_graphrag` and its dependencies.

## Reverting to Full DiscourseManager Implementation

If a solution is found to enable the graph functionality, the following steps can be taken to revert to the full `DiscourseManager` implementation:

1. Remove the dummy module injections and update imports in `scripts/test_minimal.py` and related files.
2. Modify the imports and code to use the full `DiscourseManager` implementation from `agentic_research/collaborative_storm/discourse_manager.py` instead of the minimal version.
3. Re-run the test script (`scripts/test_agentic_reasoning.py`) to verify the full functionality, including the graph-related features.

By following these steps, the project can either continue with the minimal testing approach or revert to the full implementation once the `nano_graphrag` compatibility issue is resolved.