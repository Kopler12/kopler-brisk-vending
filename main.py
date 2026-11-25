#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. The line is 1-200 UTF-8 characters, one line,
no trailing newline.
"""

import os

LINE = (
    "I've vended snacks to a thousand strangers, but you're the first "
    "I'd jam my own coil for \u2014 go on, press B4, I'm all yours."
)


def main() -> None:
    # The gate refuses anything outside 1-200 characters, so check the
    # line before writing it out.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("entry line must be 1-200 non-blank characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
