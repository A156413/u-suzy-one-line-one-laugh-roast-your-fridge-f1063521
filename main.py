#!/usr/bin/env python3
"""Entry for make.fun "One Line, One Laugh: Roast Your Fridge".

Writes a single roast line (<= 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it to stdout. Stdlib only.
"""

import os
import sys

ENTRY = (
    "My fridge hums all night like it's keeping a secret, "
    "yet the only thing it has ever preserved is the takeout I forgot in 2023."
)


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8 text of 1-200 characters,
    a single line, and not only white space."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
