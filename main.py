"""Funniest Time Machine Warning Label — make.fun entry.

Writes the warning label to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic, stdlib only, no network, no randomness.
"""

import os

ENTRY = "WARNING: If you see yourself boarding, do not board. Two of you voids the warranty, and only one of you gets home."

# Gate (program/v1): 1-120 chars, UTF-8, single line. Chosen line is 114.
# Why this line: duplicate-self is a real hazard (paradox/voided warranty) AS
# the joke, the punchline ("only one of you gets home") lands in the last
# words, and the deadpan warning tone never breaks character.
assert 1 <= len(ENTRY) <= 120, f"entry must be 1-120 chars, got {len(ENTRY)}"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
