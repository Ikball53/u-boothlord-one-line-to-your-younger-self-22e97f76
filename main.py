#!/usr/bin/env python3
"""One Line to Your Younger Self.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt
when the variable is unset). The line is composed from named parts so the
entry is built, not pasted.
"""

import os

# --- the line, built from its pieces -------------------------------------

# Who the line is about: the girl the younger self spent a year too scared to approach.
SUBJECT = "The girl you spent a year too scared to talk to"
# What the older self knows that the younger self does not: how her story ends.
FATE = "marries the guy who just says hi"

LINE = f"{SUBJECT} {FATE}."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
