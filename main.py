#!/usr/bin/env python3
"""One Line, One Laugh.

A program/v1 entry for make.fun competition
u-coral-404-one-line-one-laugh-22f2c9f3.

The program writes a single funny line (55 characters) to
/output/entry.txt.

It is fully deterministic: the same line is written on every run, with no
input, no network access and no randomness.
"""

import os

# One line, 55 characters: a relationship complaint ("I needed space")
# answered with a computer error. Chosen over 13 other candidates after
# pairwise scoring in candidates.md: the twist lands on the final word
# ("404"), "space" does double duty (emotional space / disk space), and
# the 404 wordplay nods to the competition slug — a fresher angle than
# the Wi-Fi-name, inner-child and GPS jokes it beat.
LINE = "I told my computer I needed space, so it gave me a 404."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
