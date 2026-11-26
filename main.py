#!/usr/bin/env python3
"""The Comment Above the Code — make.fun entry.

Writes one line of text to /output/entry.txt: the honest comment a
developer left above fragile production code. Deterministic, offline,
stdlib only.
"""

import os

LINE = "// I added this retry loop in 2021 because the gateway 'never duplicates a charge'. It does, weekly. Finance refunds them quietly. I have said nothing."

# The line is written exactly as-is, with no trailing newline, so the
# file holds exactly the comment and nothing else (151 characters).


def main() -> None:
    # Guard the kit's gate: the text must be 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, len(LINE)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
