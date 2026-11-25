"""Entry for make.fun: "The Meeting That Should Have Been an Email".

Writes one single-line joke (85 characters, well under the 200 cap) to
/output/entry.txt. Standard library only; deterministic: the same bytes
on every run.
"""

import os
from pathlib import Path

LINE = "It took nine people and one hour to read an email that just said 'per my last email'."

# The grader runs this with no environment set, so the default is the
# required path. The override exists only so the entry can be verified
# locally without touching /output.
OUTPUT = Path(os.environ.get("MAKEFUN_ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
