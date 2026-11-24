"""Funniest Time Machine Warning Label — make.fun entry.

Writes the warning label to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic, stdlib only, no network, no randomness.
"""

import os

ENTRY = "WARNING: If you see yourself boarding, do not board. Two of you voids the warranty, and only one of you gets home."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
