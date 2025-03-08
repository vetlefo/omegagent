"""
Test script to verify all imports are working correctly in utils.py and rm.py
"""

print("Testing imports from utils.py...")
try:
    import dspy
    import toml
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    import trafilatura
    from qdrant_client import QdrantClient
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_qdrant import Qdrant
    import pandas as pd
    print("All utils.py imports successful!")
except ImportError as e:
    print(f"Error importing: {e}")

print("\nTesting imports from rm.py...")
try:
    import dspy
    from duckduckgo_search import DDGS
    import tavily
    from googleapiclient.discovery import build
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    print("All rm.py imports successful!")
except ImportError as e:
    print(f"Error importing: {e}")