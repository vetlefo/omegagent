import os
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from backend.models.shared import RelevantFiles
from typing import List, Dict, Optional, Any
import time
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern
import logging
import glob
import json
from backend.agents.models import CodeChunkUpdate
import threading
import backoff
import numpy as np

# Import Encoder from agentic_research for enhanced embeddings
from agentic_research.encoder import Encoder

logger = logging.getLogger(__name__)

# Cache for index
_index_cache = None
_last_index_update = 0
_INDEX_CACHE_TTL = 300  # 5 minutes
_index_lock = threading.Lock()

def _get_gitignore_spec(root_directory: str) -> PathSpec:
    """Build a PathSpec from all .gitignore files in the directory tree."""
    gitignore_patterns = []
    
    # Walk up the directory tree looking for .gitignore files
    current_dir = root_directory
    while True:
        gitignore_path = os.path.join(current_dir, '.gitignore')
        if os.path.isfile(gitignore_path):
            try:
                with open(gitignore_path, 'r') as f:
                    patterns = f.readlines()
                    gitignore_patterns.extend(p.strip() for p in patterns if p.strip() and not p.startswith('#'))
            except:
                pass
                
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # Reached root
            break
        current_dir = parent_dir
        
    return PathSpec.from_lines(GitWildMatchPattern, gitignore_patterns)

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
    """Splits the text into chunks with specified overlap."""
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap  # move start forward with overlap
    return chunks

class AgenticEncoderFunction:
    """Custom embedding function using Agentic-Reasoning's Encoder."""
    
    def __init__(self, encoder_type="openai", embedding_model=None):
        """
        Initialize the encoder function.
        
        Args:
            encoder_type: The type of encoder to use (openai, azure)
            embedding_model: The specific embedding model to use (e.g., text-embedding-3-small)
                             If None, uses the default from Encoder class
        """
        # Get embedding model from environment if not specified
        if embedding_model is None:
            embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
            
        # Initialize the encoder - pass embedding model if using OpenAI or Azure
        self.encoder = Encoder(
            encoder_type=encoder_type,
            embedding_model=embedding_model if encoder_type in ["openai", "azure"] else None
        )
        logger.info(f"Initialized AgenticEncoderFunction with {encoder_type} model: {embedding_model}")
        
    def __call__(self, texts):
        """Generate embeddings for the given texts."""
        if not texts:
            return []
        try:
            # Use Encoder's encode method to get embeddings
            embeddings = self.encoder.encode(texts)
            return embeddings.tolist()  # Convert numpy array to list
        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            # Determine embedding dimension based on model (defaults to 1536 for text-embedding-3-small)
            dim = 1536
            if hasattr(self.encoder, "embedding_dimension"):
                dim = self.encoder.embedding_dimension
            # Fallback to zeros if embedding fails
            return [[0.0] * dim] * len(texts)

class SearchIndex:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SearchIndex, cls).__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def __init__(self):
        if self._initialized:
            return
            
        with self._lock:
            if not self._initialized:
                self.client = chromadb.EphemeralClient(Settings(anonymized_telemetry=False))
                # Use advanced Agentic-Reasoning encoder if environment variable is set
                if os.getenv("USE_AGENTIC_ENCODER", "false").lower() == "true":
                    try:
                        # Get encoder type and embedding model from environment variables
                        encoder_type = os.getenv("ENCODER_API_TYPE", "openai")
                        embedding_model = None
                        
                        # Get the appropriate embedding model based on encoder type
                        if encoder_type.lower() == "openai":
                            embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
                        elif encoder_type.lower() == "azure":
                            embedding_model = os.getenv("AZURE_EMBEDDING_MODEL", "text-embedding-3-small")
                            
                        # Initialize the encoder with the specified model
                        self.embedding_function = AgenticEncoderFunction(
                            encoder_type=encoder_type,
                            embedding_model=embedding_model
                        )
                        logger.info(f"Using Agentic-Reasoning Encoder for embeddings: {encoder_type}/{embedding_model}")
                    except Exception as e:
                        logger.warning(f"Failed to initialize Agentic Encoder: {e}. Falling back to default.")
                        self.embedding_function = embedding_functions.DefaultEmbeddingFunction()
                else:
                    self.embedding_function = embedding_functions.DefaultEmbeddingFunction()
                    logger.info("Using default embedding function")
                
                self._create_collection()
                self._initialized = True
    
    @backoff.on_exception(backoff.expo, Exception, max_tries=3)
    def _create_collection(self):
        try:
            self.collection = self.client.create_collection(
                name='code_documents',
                embedding_function=self.embedding_function
            )
        except Exception as e:
            logger.warning(f"Failed to create collection: {e}")
            # If collection exists, try getting it
            try:
                self.collection = self.client.get_collection(
                    name='code_documents',
                    embedding_function=self.embedding_function
                )
            except Exception as inner_e:
                logger.error(f"Could not create or get collection: {inner_e}")
                raise
    
    @backoff.on_exception(backoff.expo, Exception, max_tries=3)
    def add_file(self, filepath: str, content: str, chunk_size: int = 500, overlap: int = 100):
        chunks = chunk_text(content, chunk_size=chunk_size, overlap=overlap)
        for i, chunk in enumerate(chunks):
            chunk_id = f"{filepath}::chunk{i}"
            try:
                self.collection.add(documents=[chunk], ids=[chunk_id])
            except Exception as e:
                logger.warning(f"Failed to add chunk {i} of {filepath}: {e}")
                raise

    @backoff.on_exception(backoff.expo, Exception, max_tries=3)
    def query(self, query_text: str, n_results: int = 10):
        return self.collection.query(query_texts=[query_text], n_results=n_results)

def get_file_content(file_path: str, root_directory: str = None) -> str:
    """Get the content of a file, ensuring absolute paths are used.
    
    Args:
        file_path: The path to the file to read
        root_directory: The root directory to resolve relative paths against. If None, uses current directory.
    """
    # Convert to absolute path if relative
    if not os.path.isabs(file_path):
        if root_directory:
            file_path = os.path.join(root_directory, file_path)
        else:
            file_path = os.path.join(os.getcwd(), file_path)
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return ""

def _build_search_index(root_directory: str) -> SearchIndex:
    index = SearchIndex()
    gitignore_spec = _get_gitignore_spec(root_directory)
    
    for root, dirs, files in os.walk(root_directory):
        # Filter out ignored directories to skip them entirely
        dirs[:] = [d for d in dirs if not gitignore_spec.match_file(os.path.join(root, d))]
        
        for file in files:
            if not file.endswith(('.py', '.js', '.ts', '.svelte', '.html', '.css')):
                continue
            
            file_path = os.path.join(root, file)
            # Skip files that match gitignore patterns
            if gitignore_spec.match_file(file_path):
                continue
            
            content = get_file_content(file_path, root_directory)
            index.add_file(file_path, content)
    
    return index

def _get_or_build_index(root_directory: str) -> SearchIndex:
    global _index_cache, _last_index_update
    
    current_time = time.time()
    if _index_cache is None or (current_time - _last_index_update) > _INDEX_CACHE_TTL:
        _index_cache = _build_search_index(root_directory)
        _last_index_update = current_time
    
    return _index_cache

def get_relevant_snippets(search_terms: str, root_directory: str, top_k: int = 10) -> List[Dict[str, str]]:
    """
    Searches through files in the codebase for search_terms using ChromaDB with 
    semantic search capabilities provided by Agentic-Reasoning's Encoder.
    
    This enhanced version:
    1. Uses semantic understanding to match concepts rather than just keywords
    2. Provides a relevance score based on semantic similarity 
    3. Optionally returns full file content or just the relevant chunks
    
    Args:
        search_terms: The search query to match against code
        root_directory: The root directory of the codebase
        top_k: Maximum number of relevant snippets to return
        
    Returns:
        List of dictionaries containing filename, snippet content, and relevance score
    """
    with _index_lock:
        index = _get_or_build_index(root_directory)
        try:
            # Get query results from ChromaDB using the semantic embeddings
            results = index.query(query_text=search_terms, n_results=top_k)
            snippets = []
            
            # Determine if we want full files or just matching chunks
            return_full_files = os.getenv("RETURN_FULL_FILES", "true").lower() == "true"
            
            for doc_id, document, distance in zip(
                results['ids'][0], 
                results['documents'][0], 
                results['distances'][0]
            ):
                filename = doc_id.split("::")[0]
                
                snippet = {
                    "filename": filename,
                    # Return either the full file or just the matching chunk
                    "snippet": get_file_content(filename, root_directory) if return_full_files else document,
                    "distance": distance,
                    "relevance_score": 1.0 - distance  # Convert distance to similarity score
                }
                snippets.append(snippet)
                
            # Sort by relevance (highest first)
            snippets.sort(key=lambda x: x["relevance_score"], reverse=True)
            return snippets
        except Exception as e:
            logger.error(f"Semantic search failed: {e}")
            return []

def build_full_context(repo_map: str, files: RelevantFiles, root_directory: str = None, 
                   include_semantic_relationships: bool = False) -> str:
    """
    Given a repo_map (as a string) and a list of file objects (each with a 'filename' key),
    read the contents of each file and concatenate them with the repo_map.
    
    Args:
        repo_map: A string containing the repository map
        files: RelevantFiles object containing the files to include
        root_directory: The root directory to resolve relative paths against
        include_semantic_relationships: Whether to include semantic relationships in the context
    
    Returns:
        A string containing the full context for AI agents to use
    """
    context_parts = [f"Repository Map:\n{repo_map}\n"]
    
    # Check if semantic relationships information is available
    if include_semantic_relationships:
        # Try to load semantic relationships from file
        relationships_path = os.path.join(root_directory or ".", "semantic_relationships.json")
        if os.path.exists(relationships_path):
            try:
                from agentic_research.utils import FileIOHelper
                relationships = FileIOHelper.load_json(relationships_path)
                
                # Add relationships to context
                context_parts.append("\nSemantic Component Relationships:")
                for comp_id, related in relationships.items():
                    context_parts.append(f"{comp_id} is related to:")
                    for rel_id, score in related:
                        context_parts.append(f"  - {rel_id} (similarity: {score:.2f})")
                context_parts.append("\n")
                
                logger.info("Added semantic relationships to context")
            except Exception as e:
                logger.warning(f"Failed to load semantic relationships: {e}")
    
    # Add file contents
    for file in files.files:
        filename = file.filename
        if not os.path.isabs(filename) and root_directory:
            filename = os.path.join(root_directory, filename)
        if filename and os.path.isfile(filename):
            content = get_file_content(filename, root_directory)
            context_parts.append(f"File: {filename}\n{content}\n")
        else:
            context_parts.append(f"File: {filename} not found.\n")
    
    # Final context
    full_context = "\n".join(context_parts)
    
    # Log the size of the context for debugging
    logger.info(f"Built full context: {len(full_context.split())} words, {len(full_context)} characters")
    
    return full_context
