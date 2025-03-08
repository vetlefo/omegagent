#!/usr/bin/env python3
import os
import sys
import ast
from typing import Any, List, Dict, Set, Optional, Union
import tiktoken
from bs4 import BeautifulSoup
import fnmatch
import re
import logging

# Import advanced reasoning capabilities from Agentic-Reasoning
from agentic_research.encoder import Encoder
from agentic_research.utils import FileIOHelper

logger = logging.getLogger(__name__)

def unparse_annotation(annotation):
    """
    Return a source-code string for an annotation using ast.unparse (Python 3.9+).
    """
    try:
        return ast.unparse(annotation)
    except Exception:
        return None

def format_parameters(parameters):
    """
    Format a list of parameter dicts into a Python parameter list string.
    Each parameter is output as: name: type.
    If no type is available, "Any" is used.
    """
    params = []
    for param in parameters:
        ptype = param.get("type") or "Any"
        params.append(f"{param['name']}: {ptype}")
    return ", ".join(params)

def format_function(func):
    """
    Return a Python stub-like function declaration.
    Example:
        async def foo(a: int, b: Any) -> str: ...
    """
    async_keyword = "async " if func.get("async") else ""
    ret = func.get("return") or "Any"
    param_str = format_parameters(func.get("parameters", []))
    return f"{async_keyword}def {func['name']}({param_str}) -> {ret}: ..."

def format_class(cls):
    """
    Return a Python stub-like class declaration.
    Attributes and methods are indented inside the class.
    """
    lines = []
    lines.append(f"class {cls['name']}:")
    # Attributes
    if cls.get("attributes"):
        for attr in cls["attributes"]:
            atype = attr.get("type") or "Any"
            lines.append(f"    {attr['name']}: {atype}")
    # Methods
    if cls.get("methods"):
        for meth in cls["methods"]:
            lines.append("    " + format_function(meth))
    # If there is nothing inside, put an ellipsis.
    if not cls.get("attributes") and not cls.get("methods"):
        lines.append("    ...")
    return "\n".join(lines)

def parse_asset_file(filepath: str) -> Dict[str, Any]:
    """
    Read a .js or .css file and return a stub representation.
    This stub includes a header comment with the filename and up to ten non-empty lines of content.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading asset file {filepath}: {e}", file=sys.stderr)
        return {"stub": f"/* Error reading file: {filepath} */"}
    
    snippet = []
    for line in lines:
        clean_line = line.strip()
        if (clean_line):
            snippet.append(clean_line)
        if len(snippet) >= 10:
            break

    base = os.path.basename(filepath)
    if filepath.endswith(".js"):
        header = f"/* JavaScript File: {base} */"
    elif filepath.endswith(".css"):
        header = f"/* CSS File: {base} */"
    else:
        header = f"/* Asset File: {base} */"
    return {"stub": header + "\n" + "\n".join(snippet)}

def add_parent_info(node, parent=None):
    """
    Recursively add a parent attribute to every node in the AST.
    """
    node.parent = parent
    for child in ast.iter_child_nodes(node):
        add_parent_info(child, node)

def parse_gitignore(gitignore_path: str) -> Set[str]:
    """
    Parse a .gitignore file and return a set of patterns.
    """
    patterns = set()
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if line and not line.startswith('#'):
                    # Don't add bare * pattern as it's too broad
                    if line != '*':
                        patterns.add(line)
    return patterns

def should_ignore(path: str, root_dir: str, gitignore_patterns: Set[str]) -> bool:
    """
    Check if a path should be ignored based on gitignore patterns.
    """
    if not gitignore_patterns:
        return False

    # Get relative path from root directory
    rel_path = os.path.relpath(path, root_dir)
    
    # Convert path to forward slashes for consistency
    rel_path = rel_path.replace(os.sep, '/')
    
    for pattern in gitignore_patterns:
        # Handle pattern variations
        if pattern.endswith('/'):
            # Directory pattern
            if fnmatch.fnmatch(rel_path + '/', pattern) or \
               fnmatch.fnmatch(rel_path + '/*', pattern):
                return True
        else:
            # File pattern
            if fnmatch.fnmatch(rel_path, pattern):
                return True
            # Handle patterns without leading slash
            if '/' not in pattern and fnmatch.fnmatch(os.path.basename(rel_path), pattern):
                return True
    
    return False

def parse_svelte_file(filepath: str) -> Dict[str, Any]:
    """
    Parse a Svelte file and return a dict with:
      - "components": imported components
      - "scripts": script block contents
      - "styles": style block contents
      - "props": component props
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Skipping {filepath}: {e}", file=sys.stderr)
        return None

    svelte_info = {
        "components": [],
        "props": [],
        "hasScript": False,  
        "hasStyle": False
    }

    # Extract imported components
    import_pattern = r'import\s+(?:\{[^}]+\}|[\w\d]+)\s+from\s+[\'"]([^\'"]+)[\'"]'
    for match in re.finditer(import_pattern, content):
        if match.group(1).endswith('.svelte'):
            svelte_info["components"].append(match.group(1))

    # Check for script and extract props
    if '<script' in content:
        svelte_info["hasScript"] = True
        # Look for export let statements to find props
        prop_pattern = r'export\s+let\s+(\w+)(?:\s*=\s*[^;]+)?;'
        props = re.findall(prop_pattern, content)
        svelte_info["props"].extend(props)

    # Check for style block
    if '<style' in content:
        svelte_info["hasStyle"] = True

    return svelte_info

class RepoMap:
    def __init__(self, root_dir=".", use_semantic_analysis=False):
        self.root_dir = os.path.abspath(root_dir)
        self.repo_map = {}
        self.gitignore_patterns = set()
        self._load_gitignore_patterns()
        
        # Flag to enable semantic code analysis using Agentic-Reasoning
        self.use_semantic_analysis = use_semantic_analysis or os.getenv("USE_SEMANTIC_ANALYSIS", "false").lower() == "true"
        
        # Initialize encoder if semantic analysis is enabled
        self.encoder = None
        if self.use_semantic_analysis:
            try:
                self.encoder = Encoder(encoder_type=os.getenv("ENCODER_API_TYPE", "openai"))
                logger.info("Initialized Agentic-Reasoning Encoder for semantic code analysis")
            except Exception as e:
                logger.warning(f"Failed to initialize Encoder: {e}")
                self.use_semantic_analysis = False
                
        logger.info(f"Loaded gitignore patterns: {self.gitignore_patterns}")

    def _load_gitignore_patterns(self):
        """
        Load all .gitignore patterns from the root directory and its subdirectories.
        """
        for dirpath, _, filenames in os.walk(self.root_dir):
            if '.gitignore' in filenames:
                gitignore_path = os.path.join(dirpath, '.gitignore')
                self.gitignore_patterns.update(parse_gitignore(gitignore_path))

    def build_map(self):
        """
        Walk the directory tree starting at self.root_dir, parse every .py, .html, .js, .css and .svelte file,
        and build the repository map with extracted functions, classes, HTML structures, or asset stubs.
        Excludes files and directories that match patterns in .gitignore files.
        """
        for dirpath, dirnames, filenames in os.walk(self.root_dir):
            # Remove ignored directories from dirnames (in-place)
            for d in dirnames[:]:
                full_path = os.path.join(dirpath, d)
                if should_ignore(full_path, self.root_dir, self.gitignore_patterns):
                    dirnames.remove(d)
            
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                # Skip files that match gitignore patterns
                if should_ignore(filepath, self.root_dir, self.gitignore_patterns):
                    continue
                    
                rel_path = os.path.relpath(filepath, self.root_dir)
                if filename.endswith(".py"):
                    parsed = self.parse_python_file(filepath)
                    if parsed is not None:
                        self.repo_map[rel_path] = parsed
                elif filename.endswith(".html"):
                    parsed = self.parse_html_file(filepath)
                    if parsed is not None:
                        self.repo_map[rel_path] = parsed
                elif filename.endswith(".svelte"):
                    parsed = parse_svelte_file(filepath)
                    if parsed is not None:
                        self.repo_map[rel_path] = parsed
                elif filename.endswith(".js") or filename.endswith(".css"):
                    asset_stub = parse_asset_file(filepath)
                    self.repo_map[rel_path] = asset_stub
        return self.repo_map

    @staticmethod
    def get_function_signature(node: Union[ast.FunctionDef, ast.AsyncFunctionDef]) -> Dict[str, Any]:
        """
        Given an ast.FunctionDef or ast.AsyncFunctionDef node, return a dict with:
          - "name": function name.
          - "parameters": list of parameters (each with "name" and optional "type").
          - "return": return annotation if available.
          - "async": True if the function is asynchronous.
        """
        params = []
        for arg in node.args.args:
            param = {"name": arg.arg}
            if arg.annotation:
                param["type"] = unparse_annotation(arg.annotation)
            params.append(param)
        if node.args.vararg:
            vararg = {"name": "*" + node.args.vararg.arg}
            if node.args.vararg.annotation:
                vararg["type"] = unparse_annotation(node.args.vararg.annotation)
            params.append(vararg)
        for arg in node.args.kwonlyargs:
            param = {"name": arg.arg}
            if arg.annotation:
                param["type"] = unparse_annotation(arg.annotation)
            params.append(param)
        if node.args.kwarg:
            kwarg = {"name": "**" + node.args.kwarg.arg}
            if node.args.kwarg.annotation:
                kwarg["type"] = unparse_annotation(node.args.kwarg.annotation)
            params.append(kwarg)
        func_info = {"name": node.name, "parameters": params}
        if node.returns:
            func_info["return"] = unparse_annotation(node.returns)
        return func_info

    def parse_python_file(self, filepath):
        """
        Parse a Python file and return a dict with keys:
          - "functions": list of functions (only top-level functions, not methods) with signature details.
          - "classes": list of classes, each with:
              • "name": class name,
              • "methods": list of method signatures,
              • "attributes": list of attributes.
        """
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                source = f.read()
        except Exception as e:
            print(f"Skipping {filepath}: {e}", file=sys.stderr)
            return None

        try:
            tree = ast.parse(source, filename=filepath)
            add_parent_info(tree)  # add parent pointers to all nodes
        except Exception as e:
            print(f"Failed to parse {filepath}: {e}", file=sys.stderr)
            return None

        file_info = {"functions": [], "classes": []}

        # Collect only top-level functions (skip those defined within a class)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if isinstance(getattr(node, "parent", None), ast.ClassDef):
                    continue
                is_async = isinstance(node, ast.AsyncFunctionDef)
                func_info = self.get_function_signature(node)
                func_info["async"] = is_async
                file_info["functions"].append(func_info)

        # Process classes by iterating over the immediate children of the module
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.ClassDef):
                class_info = {"name": node.name, "methods": [], "attributes": []}
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        is_async = isinstance(item, ast.AsyncFunctionDef)
                        meth_info = self.get_function_signature(item)
                        meth_info["async"] = is_async
                        class_info["methods"].append(meth_info)
                    elif isinstance(item, ast.AnnAssign):
                        if isinstance(item.target, ast.Name):
                            attr_name = item.target.id
                            attr_type = unparse_annotation(item.annotation) if item.annotation else None
                            class_info["attributes"].append({"name": attr_name, "type": attr_type})
                    elif isinstance(item, ast.Assign):
                        for target in item.targets:
                            if isinstance(target, ast.Name):
                                attr_name = target.id
                                attr_type = getattr(item, "type_comment", None)
                                class_info["attributes"].append({"name": attr_name, "type": attr_type})
                file_info["classes"].append(class_info)

        return file_info

    def parse_html_file(self, filepath: str) -> Dict[str, Any]:
        """
        Parse an HTML file and return a dict with:
          - "tags": a dictionary where keys are tag names and values are lists of attributes.
        """
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
        except Exception as e:
            print(f"Skipping {filepath}: {e}", file=sys.stderr)
            return None

        tags = {}
        for tag in soup.find_all():
            if tag.name not in tags:
                tags[tag.name] = set()
            for attr in tag.attrs.keys():
                tags[tag.name].add(attr)
        for tag in tags:
            tags[tag] = sorted(list(tags[tag]))
        return {"tags": tags}

    def analyze_semantic_relationships(self):
        """
        Analyze semantic relationships between code components using Agentic-Reasoning's Encoder.
        This enhances the code understanding by identifying conceptually related components.
        
        Returns:
            Dict mapping component names to lists of semantically related components
        """
        if not self.use_semantic_analysis or not self.encoder:
            logger.warning("Semantic analysis is disabled or encoder not initialized")
            return {}
            
        try:
            # Extract component definitions (classes and functions) from repo_map
            components = []
            component_details = {}
            
            for filepath, info in self.repo_map.items():
                # Process Python functions
                if info.get("functions"):
                    for func in info["functions"]:
                        func_name = func["name"]
                        func_id = f"{filepath}::{func_name}"
                        # Create a description of the function for semantic analysis
                        func_desc = format_function(func)
                        components.append(func_id)
                        component_details[func_id] = func_desc
                
                # Process Python classes
                if info.get("classes"):
                    for cls in info["classes"]:
                        cls_name = cls["name"]
                        cls_id = f"{filepath}::{cls_name}"
                        # Create a description of the class for semantic analysis
                        cls_desc = format_class(cls)
                        components.append(cls_id)
                        component_details[cls_id] = cls_desc
            
            # If no components found, return empty dictionary
            if not components:
                return {}
                
            # Generate embeddings for all component descriptions
            descriptions = [component_details[comp_id] for comp_id in components]
            embeddings = self.encoder.encode(descriptions)
            
            # Calculate semantic similarity between all components
            relationships = {}
            for i, comp_id in enumerate(components):
                # Find the 5 most similar components (excluding self)
                similarities = []
                for j, other_id in enumerate(components):
                    if i != j:  # Skip self-comparison
                        # Calculate cosine similarity between embeddings
                        similarity = self._cosine_similarity(embeddings[i], embeddings[j])
                        similarities.append((other_id, similarity))
                
                # Sort by similarity (highest first) and take top 5
                similarities.sort(key=lambda x: x[1], reverse=True)
                related = similarities[:5]
                relationships[comp_id] = related
            
            return relationships
            
        except Exception as e:
            logger.error(f"Error in semantic analysis: {e}")
            return {}
    
    def _cosine_similarity(self, a, b):
        """Calculate cosine similarity between two vectors."""
        import numpy as np
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def to_python_stub(self, include_semantic_relationships=False):
        """
        Return a Python-style stub representation of the repository map.
        
        Args:
            include_semantic_relationships: If True, includes semantic relationship 
                                           information in the stub (requires semantic analysis)
        """
        lines = []
        lines.append(f"# Repo Stub for directory: {self.root_dir}")
        
        # Add semantic relationships if requested and available
        if include_semantic_relationships and self.use_semantic_analysis:
            relationships = self.analyze_semantic_relationships()
            if relationships:
                lines.append("\n# Semantic Component Relationships:")
                for comp_id, related in relationships.items():
                    lines.append(f"# {comp_id} is related to:")
                    for rel_id, score in related:
                        lines.append(f"#   - {rel_id} (similarity: {score:.2f})")
                lines.append("\n")
        
        for filepath, info in self.repo_map.items():
            lines.append(f"\n# File: {filepath}")
            if filepath.endswith(".py"):
                if info.get("functions"):
                    for func in info["functions"]:
                        lines.append(format_function(func))
                if info.get("classes"):
                    for cls in info["classes"]:
                        lines.append(format_class(cls))
            elif filepath.endswith(".html"):
                tags = info.get("tags", {})
                if tags:
                    for tag, attrs in tags.items():
                        attrs_str = ", ".join(attrs) if attrs else ""
                        lines.append(f"<{tag} {attrs_str}>".strip())
                else:
                    lines.append("    ...")
            elif filepath.endswith(".svelte"):
                if info.get("components"):
                    lines.append("  Imported components:")
                    for comp in info["components"]:
                        lines.append(f"    - {comp}")
                if info.get("props"):
                    lines.append("  Props:")
                    for prop in info["props"]:
                        lines.append(f"    - {prop}")
                if info.get("hasScript"):
                    lines.append("  Has <script> block")
                if info.get("hasStyle"):
                    lines.append("  Has <style> block")
            elif filepath.endswith(".js") or filepath.endswith(".css"):
                # For asset files, output the stub text.
                stub = info.get("stub", "")
                lines.append(stub)
        return "\n".join(lines)

    def print_python_stub(self, include_semantic_relationships=False):
        """
        Print the Python stub representation.
        
        Args:
            include_semantic_relationships: If True, includes semantic relationship analysis
        """
        print(self.to_python_stub(include_semantic_relationships=include_semantic_relationships))

    def token_count_python_stub(self, encoding_name="gpt2", include_semantic_relationships=False):
        """
        Compute an accurate token count of the Python stub representation using tiktoken.
        
        Args:
            encoding_name: The name of the encoding to use
            include_semantic_relationships: Whether to include semantic relationships in the token count
        """
        stub_text = self.to_python_stub(include_semantic_relationships=include_semantic_relationships)
        encoding = tiktoken.get_encoding(encoding_name)
        tokens = encoding.encode(stub_text)
        return len(tokens)

    def print_token_count_python_stub(self, include_semantic_relationships=False):
        """
        Print the token count for the Python stub representation.
        
        Args:
            include_semantic_relationships: Whether to include semantic relationships in the token count
        """
        count = self.token_count_python_stub(include_semantic_relationships=include_semantic_relationships)
        if include_semantic_relationships and self.use_semantic_analysis:
            print(f"Accurate token count (Python stub with semantic relationships, using tiktoken): {count}")
        else:
            print(f"Accurate token count (Python stub, using tiktoken): {count}")
    
    def save_repo_map(self, output_path=None, include_semantic_relationships=False):
        """
        Save the repository map to a file.
        
        Args:
            output_path: Path to save the repository map to
            include_semantic_relationships: Whether to include semantic relationships
        """
        if output_path is None:
            output_path = os.path.join(self.root_dir, "repo_map.txt")
            
        stub_text = self.to_python_stub(include_semantic_relationships=include_semantic_relationships)
        try:
            FileIOHelper.write_str(stub_text, output_path)
            logger.info(f"Repository map saved to {output_path}")
            
            # Also save relationships separately if requested
            if include_semantic_relationships and self.use_semantic_analysis:
                relationships = self.analyze_semantic_relationships()
                if relationships:
                    rel_path = os.path.join(os.path.dirname(output_path), "semantic_relationships.json")
                    FileIOHelper.dump_json(relationships, rel_path)
                    logger.info(f"Semantic relationships saved to {rel_path}")
                    
            return True
        except Exception as e:
            logger.error(f"Failed to save repository map: {e}")
            return False

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate a repository map")
    parser.add_argument("--root", "-r", default=".", help="Root directory to analyze")
    parser.add_argument("--semantic", "-s", action="store_true", help="Enable semantic analysis")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--encoder", "-e", default="openai", 
                       help="Encoder type to use (openai, azure)")
    args = parser.parse_args()
    
    # Set environment variable for encoder type if provided
    if args.encoder:
        os.environ["ENCODER_API_TYPE"] = args.encoder
    
    # Initialize RepoMap with semantic analysis if requested
    rm = RepoMap(args.root, use_semantic_analysis=args.semantic)
    print(f"Building repository map for {args.root}...")
    rm.build_map()
    
    # Save the repository map if output path is provided
    if args.output:
        rm.save_repo_map(args.output, include_semantic_relationships=args.semantic)
    else:
        # Otherwise print to stdout
        rm.print_python_stub(include_semantic_relationships=args.semantic)
        rm.print_token_count_python_stub(include_semantic_relationships=args.semantic)
