#!/usr/bin/env python3
"""Write the competition entry letter to entry.txt.

The entry is exactly one letter, A for coffee, and nothing else:
no word, no explanation, no punctuation, no trailing newline.
A is the first cup of the day, black, before anything else gets done.
"""

import os
from pathlib import Path

LETTER = "A"
OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def gate_problems(text):
    problems = []
    if len(text) != 1:
        problems.append("must be exactly one character")
    if text != text.strip():
        problems.append("must not be whitespace")
    if not text.isalpha():
        problems.append("must be a letter")
    return problems


def main():
    problems = gate_problems(LETTER)
    if problems:
        raise SystemExit("entry letter fails the gate: " + "; ".join(problems))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LETTER, encoding="utf-8")
    # The read-back is the proof: whatever lands in entry.txt must be
    # byte for byte the letter, with no trailing newline added.
    if OUTPUT_PATH.read_text(encoding="utf-8") != LETTER:
        raise SystemExit("entry.txt does not match the letter")


if __name__ == "__main__":
    main()
