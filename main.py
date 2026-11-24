#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt (UTF-8, 1-200 characters).
"""

import os

ENTRY = (
    "In my defense, prod broke because I fixed a typo in the config "
    "\u2014 three other services had been building on the misspelling "
    "for years, and they all noticed at the same time."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
