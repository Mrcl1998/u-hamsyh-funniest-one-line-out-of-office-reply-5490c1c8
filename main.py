"""Funniest One-Line Out-of-Office Reply.

Writes a single out-of-office auto-reply line to /output/entry.txt.
Pure standard library, deterministic, no network.
"""

import os

ENTRY = "Your email arrived safely and will be ignored in the order it was received."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
