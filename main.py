#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line (<=160 chars) to /output/entry.txt,
the artifact the make.fun program/v1 grader reads and gates.
"""
import os

ENTRY = "v4.0.7: fixed a bug where sneezing in a quiet meeting played at 340% volume with no mute button and eye contact from 14 colleagues."


def main() -> None:
    # Gate, same as the sealed scorer: UTF-8, 1-160 chars, not only
    # whitespace, exactly one line. Fail loudly rather than ship invalid.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, must be 1-160"
    assert "\n" not in ENTRY and ENTRY.strip() != "", "entry must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
