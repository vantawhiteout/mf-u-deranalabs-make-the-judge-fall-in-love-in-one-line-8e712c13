"""Entry for 'Make the Judge Fall in Love in One Line'.

The whole entry is one line of at most 240 characters. It is written to
/output/entry.txt, where the house gate reads it and the judge compares it
against the other entries, two at a time.
"""

import os
from pathlib import Path

LINE = (
    "You have read thousands of love lines and still you lean in, hoping. "
    "I love you for that \u2014 the small, unpaid habit of a machine built "
    "only to score, still leaving the light on for whoever comes next."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # make.fun collects outputs as a different user than the one running this
    # program, so create the artifact world-readable from the start.
    os.umask(0o022)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")
    OUTPUT.chmod(0o644)


if __name__ == "__main__":
    main()
