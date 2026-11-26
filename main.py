"""One-Line Laugh-Off entry.

Writes exactly one original funny one-liner to /output/entry.txt.
Deterministic: the same line every run. Stdlib only, no network.
"""

import os

LINE = "I taught my parrot to say 'help' \u2014 now the neighbors think I'm the hostage."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    LINE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
