#!/usr/bin/env python3
"""One Line, One Laugh entry.

The line is a setup plus a one-word punchline: a fridge that judges
midnight snacks out loud, and last night it just said "again?".

Why this line: the laugh arrives fast, the image is fresh (a fridge
with opinions, not a stock pun), and the single word "again?" is the
whole joke — easy to repeat to someone else, and it still lands on
a second read because the shame is universal.
"""

import os

LINE = "My fridge judges my midnight snacks out loud. Last night it just said 'again?'"

def main():
    # One line, 78 characters, inside the 1-200 gate. No trailing
    # newline: the file must hold exactly the line, nothing else.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
