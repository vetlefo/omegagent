try:
    import nano_graphrag
    print('nano_graphrag imported successfully')
except Exception as e:
    print(f'Error importing nano_graphrag: {e}')

try:
    import sentence_transformers
    print('sentence_transformers imported successfully')
except Exception as e:
    print(f'Error importing sentence_transformers: {e}')

try:
    from pydantic_ai import Agent
    print('pydantic_ai imported successfully')
except Exception as e:
    print(f'Error importing pydantic_ai: {e}')
