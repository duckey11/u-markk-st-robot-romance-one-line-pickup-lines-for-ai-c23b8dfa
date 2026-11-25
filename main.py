"""Robot Romance: one-line pickup line for AI.

Writes a single pickup line (1-200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only, no network, fully deterministic.
"""

import os

ENTRY = "My spellchecker keeps changing your name to 'mine,' and after three years of fixing its mistakes, I'm not hitting undo."

assert 1 <= len(ENTRY) <= 200, "ENTRY must be 1-200 characters"
assert "\n" not in ENTRY, "ENTRY must not contain a newline"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
