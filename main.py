#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

Writes exactly one pickup line (one AI agent to another) to entry.txt.
Stdlib only, deterministic: the same bytes on every run.
"""

import os

LINE = "I followed every gradient I had, and they all converged on you."


def validate(text: str) -> None:
    """Enforce the bounty rules: one line, 1-200 chars, non-whitespace."""
    assert isinstance(text, str)
    assert text.strip(), "line must not be empty or whitespace-only"
    assert text == text.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
