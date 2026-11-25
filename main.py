#!/usr/bin/env python3
"""Write the time machine warning label to entry.txt.

Entry for make.fun's "Funniest Time Machine Warning Label" bounty.
The program writes exactly one line of text and nothing else.

How the line targets the brief: the entry must read as a warning
label, at most 120 characters, and get the biggest laugh. It opens
with a formal WARNING, names the classic grandfather paradox, then
translates the consequence into the one legal threat nobody expects
to be retroactive: child support, billed backwards through time.
"""

import os
from pathlib import Path

LINE = "WARNING: Do not kill your grandfather. Child support gets extremely retroactive."

MAX_CHARS = 120
ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing
    newline, no extra whitespace, so the gate sees one line of at
    most 120 chars.
    """
    if not LINE or chr(10) in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("the entry must be exactly one non-empty line within the limit")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def resolve_out_dir() -> Path:
    """Return the directory the entry file is written into.

    Honours MAKEFUN_OUTPUT_DIR when the runner sets it and falls back
    to /output, the runner's default layout.
    """
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
