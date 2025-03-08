import os
import mimetypes
from pathlib import Path
from typing import List, Optional

class ProjectContextGenerator:
    """
    Scans the current directory, creates:
      1) A "project tree" listing all files (with Included/Excluded).
      2) Appends the content of included files (text-based, not ignored, 
         and total combined size stays under a given max).
    """

    def __init__(
        self,
        output_file: str = "project_context.txt",
        max_total_combined_size: int = 1_024 * 1_024,  # 1MB total combined
        ignore_files: Optional[List[str]] = None,
        ignore_dirs: Optional[List[str]] = None,
        verbose: bool = False
    ) -> None:
        """
        :param output_file: Name of the output file.
        :param max_total_combined_size: The limit for total bytes of included content.
        :param ignore_files: Specific file names to ignore (e.g. 'script.py', 'package-lock.json').
        :param ignore_dirs: Directory names to ignore (e.g. '.git', 'node_modules').
        :param verbose: Whether to print logging info to stdout.
        """
        self.output_file = output_file
        self.max_total_combined_size = max_total_combined_size
        self.verbose = verbose

        # Default ignored files & directories
        self.ignore_files = set(ignore_files or [])
        self.ignore_files.add(self.output_file)  # avoid re-including output
        self.ignore_dirs = set(ignore_dirs or [
            ".git", "node_modules", "dist", "build", ".next", ".cache", ".venv",
            "build_backup", "build_new", "dataconnect-generated", "fav", "public"
        ])

        # For storing metadata about each file: included/excluded, reason, etc.
        self.file_info = {}  # dict: Path -> {"included": bool, "reason": str, "size": int}
        self.total_included_size = 0

    def log(self, message: str) -> None:
        """Helper method for optional verbose logging."""
        if self.verbose:
            print(message)

    def is_text_file(self, file_path: Path) -> bool:
        """
        Check if a file is likely text-based:
          - Skip known binary extensions.
          - Check mimetypes.
          - Do a quick binary sniff for null bytes or high non-ASCII ratio.
        """
        # Common known binary extensions to skip
        binary_exts = {
            '.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg',
            '.woff', '.woff2', '.ttf', '.eot', '.otf',
            '.mp3', '.mp4', '.webm', '.ogg', '.pdf',
            '.zip', '.gz', '.rar', '.7z'
        }
        if file_path.suffix.lower() in binary_exts:
            return False

        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type and not mime_type.startswith("text"):
            # .js might come back as "text/javascript", which is fine.
            # But if it’s application/octet-stream or something else, check more carefully
            if mime_type == "application/octet-stream":
                # Double-check by sniffing
                return not self._binary_sniff(file_path)
            return False if not mime_type.startswith("text") else True

        # Final fallback: sniff
        return not self._binary_sniff(file_path)

    def _binary_sniff(self, file_path: Path, chunk_size: int = 1024) -> bool:
        """Return True if file appears to be binary."""
        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(chunk_size)
                if b'\x00' in chunk:
                    return True  # presence of null byte suggests binary
                # Check ratio of non-ASCII
                non_ascii = sum(b > 127 for b in chunk)
                if len(chunk) > 0 and (non_ascii / len(chunk)) > 0.3:
                    return True
            return False
        except:
            # If unreadable, treat as binary
            return True

    def should_ignore(self, file_path: Path) -> bool:
        """Check if the file should be ignored by name or by any parent directory."""
        if file_path.name in self.ignore_files:
            return True
        for part in file_path.parts:
            if part in self.ignore_dirs:
                return True
        return False

    def gather_files(self, base_path: Path) -> List[Path]:
        """
        Gather all files from base_path (recursively).
        Returns a sorted list of file paths.
        """
        all_files = list(base_path.rglob("*"))
        all_files = [f for f in all_files if f.is_file()]
        # Sort by path (so the tree print is consistent)
        all_files.sort()
        return all_files

    def decide_inclusion(self, file_path: Path) -> None:
        """
        Decide whether to include a single file. Populates self.file_info[file_path] with:
         {
           "included": bool,
           "reason": str,
           "size": int
         }
        """
        stat = file_path.stat()
        size = stat.st_size

        # Default file_info
        self.file_info[file_path] = {
            "included": False,
            "reason": "",
            "size": size
        }

        # Check ignore
        if self.should_ignore(file_path):
            self.file_info[file_path]["reason"] = "Excluded: ignored by name/dir"
            return

        # Check text
        if not self.is_text_file(file_path):
            self.file_info[file_path]["reason"] = "Excluded: binary or non-text"
            return

        # Check if we'd exceed total allowed combined size
        if self.total_included_size + size > self.max_total_combined_size:
            self.file_info[file_path]["reason"] = (
                f"Excluded: adding this would exceed {self.max_total_combined_size} bytes limit"
            )
            return

        # If we get here, we can include this file
        self.file_info[file_path]["included"] = True
        self.file_info[file_path]["reason"] = "Included"
        # update total_included_size
        self.total_included_size += size
        self.log(f"Including: {file_path} (size={size} bytes)")

    def build_project_tree(self, base_path: Path) -> str:
        """
        Build a simple text "tree" listing all files and marking them
        as [Included] or [Excluded: reason]. 
        """
        # We'll produce a dict: {directory_path: [(name, is_dir), ...], ...} to group items
        from collections import defaultdict

        dir_map = defaultdict(list)
        all_paths = sorted(self.file_info.keys(), key=lambda p: p.parts)

        for path in all_paths:
            rel = path.relative_to(base_path)
            parent = rel.parent
            dir_map[parent].append((path.name, path.is_dir(), path))

        # We'll recursively print from top-level
        lines = []
        lines.append(f"{base_path.resolve().name}/")
        self._print_tree_recursive(lines, base_path, Path("."), dir_map, level=1)
        return "\n".join(lines)

    def _print_tree_recursive(
        self,
        lines: List[str],
        base_path: Path,
        rel_dir: Path,
        dir_map,
        level: int
    ):
        """Recursively build lines for the project tree."""
        if rel_dir in dir_map:
            entries = dir_map[rel_dir]
            entries.sort(key=lambda e: e[0])  # sort by name
            for name, is_dir, full_path_obj in entries:
                indent = "   " * level
                file_info = self.file_info.get(full_path_obj, {})
                included = file_info.get("included", False)
                reason = file_info.get("reason", "")
                if is_dir:
                    # It's theoretically possible if we stored directories too, but we only store files
                    # in self.file_info. Let's skip or handle if needed.
                    # We'll just display the directory name; sub-entries are handled recursively.
                    lines.append(f"{indent}{name}/ [DIR]")
                    # Then recursively handle children
                    self._print_tree_recursive(
                        lines,
                        base_path,
                        rel_dir / name,
                        dir_map,
                        level + 1
                    )
                else:
                    status_str = f"[Included]" if included else f"[{reason}]"
                    lines.append(f"{indent}{name} {status_str}")

    def generate_context_file(self) -> None:
        """
        Main entry point:
          1) Gather all files.
          2) Decide inclusion for each.
          3) Build a text tree listing all files (included/excluded).
          4) Append the content of included files, ensuring total stays < max limit.
          5) Write to `self.output_file`.
        """
        base_path = Path(".")
        all_files = self.gather_files(base_path)

        for f in all_files:
            self.decide_inclusion(f)

        # 1) Build the "project tree" text
        tree_text = self.build_project_tree(base_path)

        # 2) Gather content for included files
        included_content_lines = []
        included_content_lines.append("\n\n---\n## Included Files Content\n\n")
        for f in all_files:
            info = self.file_info[f]
            if info["included"]:
                # Read & append
                try:
                    with f.open("r", encoding="utf-8", errors="ignore") as fp:
                        file_text = fp.read()
                    included_content_lines.append(
                        f"// File: {f}\n{'-'*40}\n{file_text}\n\n"
                    )
                except Exception as e:
                    self.log(f"Error reading {f}: {e}")

        # 3) Combine into final output
        output = tree_text + "".join(included_content_lines)

        with open(self.output_file, "w", encoding="utf-8") as out:
            out.write(output)

        print(
            f"Context file generated: {self.output_file}\n"
            f"Total included content size: {self.total_included_size} bytes\n"
        )


if __name__ == "__main__":
    generator = ProjectContextGenerator(
        output_file="project_context.txt",
        max_total_combined_size=1_024 * 1_024,  # 1 MB
        ignore_files=["script.py", ".env"],  # more if needed
        ignore_dirs=[".git", "node_modules", "dist", "build", ".next", ".cache",
                     "build_backup", "build_new", "dataconnect-generated", "fav", "public"],
        verbose=True
    )
    generator.generate_context_file()