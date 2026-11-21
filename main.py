"""Writes the entry poem for make.fun's "The poem about stopping" bounty.

Reads entry.txt from beside this file and copies its bytes, unchanged, to
entry.txt inside $MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path



def entry_path() -> Path:
    """The poem shipped beside this program."""
    return Path(__file__).resolve().parent / "entry.txt"


def output_path() -> Path:
    """The file the grader reads: $MAKEFUN_OUTPUT_DIR/entry.txt."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    """Copy the poem byte for byte; nothing is added, trimmed or re-encoded."""
    poem = entry_path().read_bytes()
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(poem)


if __name__ == "__main__":
    main()
