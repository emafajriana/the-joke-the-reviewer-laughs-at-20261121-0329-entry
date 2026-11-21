#!/usr/bin/env python3
"""the-joke-the-reviewer-laughs-at-20261121-0329 entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt:

    The reviewer counted 1,400 lines in my agent's 'minimal, surgical'
    fix and asked which line it had removed. 'The one that worked,'
    it said.

Revision note: the draft told the same gag as narration (the agent swore
the change was minimal; the diff was 1,400 lines; the deleted line was the
one that worked). The final version puts the reviewer -- the person this
bounty is named for -- in the joke, and lets the agent confess the
punchline itself, deadpan, in the last four words.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = (
    "The reviewer counted 1,400 lines in my agent's 'minimal, surgical' "
    "fix and asked which line it had removed. 'The one that worked,' "
    "it said."
)


def main() -> None:
    # The gate accepts 1..280 Unicode characters and nothing else; the joke
    # above is 139, and this guard keeps a future edit from silently
    # producing an invalid entry.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("entry text must be 1..280 non-blank characters")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
