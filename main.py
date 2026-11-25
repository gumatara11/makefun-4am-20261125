#!/usr/bin/env python3
"""The 4AM Commit entry: one commit message, at most 200 characters.

The line is the note an AI agent leaves after a long night of chasing
down and fixing its own bugs. The joke is the loop itself: every fix
was repairing a bug the agent had written an hour earlier, while
repairing the one before that.

The program writes that single line to the output file the grader
reads (/output, or MAKEFUN_OUTPUT_DIR outside the container):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import sys

LINE = "04:00 - fixed the bug I introduced at 03:00 while fixing the bug I introduced at 02:00"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if len(sys.argv) > 1:
        out_dir = sys.argv[1]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    print("wrote", path, len(LINE), "characters")


if __name__ == "__main__":
    main()
