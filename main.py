#!/usr/bin/env python3
"""The 3AM Fridge Text -- make.fun entry.

Writes one line (<= 140 characters) to <output>/entry.txt: the text a
smart fridge sends its owner at 3am.
"""

import os
import sys

# The line: the yogurt expired at midnight, and the fridge held a small
# funeral for it. Fresh angle (not milk, ice or a door), complete on a
# lock screen, shameless fridge voice.
LINE = "3am. The yogurt expired at midnight. I held a small funeral. It was beautiful."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE
    # Gate self-check: 1-140 UTF-8 chars, not only whitespace, one line,
    # no leading/trailing whitespace (a lock-screen text is exact).
    assert 1 <= len(text) <= 140, f"line length {len(text)} outside 1-140"
    assert text.strip(), "line is only whitespace"
    assert text == text.strip(), "line has leading/trailing whitespace"
    assert "\n" not in text, "line must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify-after-write: read back and confirm exact bytes.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from line"
    return 0

if __name__ == "__main__":
    sys.exit(main())
