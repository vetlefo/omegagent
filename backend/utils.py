import os
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from backend.models.shared import RelevantFiles
from typing import List, Dict, Any
import backoff
import numpy as np

# Use Agentic-Reasoning encoder if variable is set
USE_AGENTIC_ENCODER = os.environ.get("USE_AGENTIC_ENCODER", "false").lower() == "true"
if USE_AGENTIC_ENCODER:
    from agentic_research.encoder import Encoder
    print("Using Agentic Encoder for embeddings")
else:
    print("Using default embedding function")

# Cache for index
_index_cache = None
_last_index_update = 0
_INDEX_CACHE_TTL = 300  # 5 minutes

def _get_gitignore_spec(root_directory: str):
    """Build a PathSpec from all .gitignore files in the directory tree."""
    import pathspec

    gitignore_patterns = []
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename == '.gitignore':
                gitignore_path = os.path.join(dirpath, filename)
                try:
                    with open(gitignore_path, 'r') as f:
                        patterns = f.readlines()
                        gitignore_patterns.extend(p.strip() for p in patterns if p.strip() and not p.startswith('#'))
                except:
                    pass
    return pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, gitignore_patterns)


def get_file_content(file_path: str, root_directory: str = None) -> str:
    """Get the content of a file, ensuring absolute paths are used."""
    if not os.path.isabs(file_path):
        if root_directory:
            file_path = os.path.join(root_directory, file_path)
        else:
            file_path = os.path.join(os.getcwd(), file_path)  # Use getcwd()

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
    """Splits the text into chunks with specified size and overlap."""
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


def _build_search_index(root_directory: str):
    """Build or rebuild the ChromaDB search index."""
    from chromadb.utils import embedding_functions

    global _index_cache, _last_index_update
    
    client = chromadb.EphemeralClient(Settings(anonymized_telemetry=False))
    
    # Choose the appropriate embedding function
    if USE_AGENTIC_ENCODER:
        embedding_function = AgenticEncoderFunction()
    else:
        embedding_function = embedding_functions.DefaultEmbeddingFunction()
    
    collection = client.create_collection(
        name='code_documents',
        embedding_function=embedding_function
    )
    
    gitignore_spec = _get_gitignore_spec(root_directory)
    
    documents = []
    metadatas = []
    ids = []

    for root, _, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check if file should be ignored
            if gitignore_spec.match_file(file_path):
                continue
            
            if file.endswith(('.py', '.js', '.ts', '.svelte', '.html', '.css')):
                try:
                    content = get_file_content(file_path, root_directory)
                    if content:
                        chunks = chunk_text(content)
                        for i, chunk in enumerate(chunks):
                            documents.append(chunk)
                            relative_path = os.path.relpath(file_path, root_directory)
                            metadatas.append({"filename": relative_path, "chunk": i})
                            ids.append(f"{relative_path}::chunk{i}")  # Unique ID

                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

    if documents:
        collection.add(documents=documents, metadatas=metadatas, ids=ids)

    _index_cache = collection
    _last_index_update = time.time()
    return collection


def get_relevant_snippets(search_terms: str, root_directory: str, top_k: int = 5) -> List[Dict[str, str]]:
    """Get relevant code snippets using ChromaDB with semantic search."""
    global _index_cache, _last_index_update

    current_time = time.time()
    if _index_cache is None or (current_time - _last_index_update) > _INDEX_CACHE_TTL:
        _index_cache = _build_search_index(root_directory)
        _last_index_update = current_time

    # if it is "too simple", i.e., no agentic encoder
    results = _index_cache.query(query_texts=[search_terms], n_results=top_k)

    snippets = []
    for i in range(len(results["documents"][0])):
        snippets.append({
            "filename": results["metadatas"][0][i]["filename"],
            "snippet": results["documents"][0][i],
        })

    return snippets


def build_full_context(repo_map: str, files: RelevantFiles, root_directory: str = None) -> str:
    """Build the full context from the repo map and relevant files."""
    context = f"Repository Map:\n{repo_map}\n"
    for file_info in files.files:
        filename = file_info.filename
        content = get_file_content(filename, root_directory)
        context += f"\n\nFile: {filename}\n```\n{content}\n```"
    return context

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
        # Initialize the encoder - pass embedding model if using OpenAI or Azure
        self.encoder = Encoder(
            encoder_type=encoder_type,
            model_name=embedding_model if encoder_type in ["openai", "azure"] else None
        )
        logger.info(f"Initialized Agentic Encoder with {encoder_type} API and model {embedding_model}")
        
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