#!/usr/bin/env python3
"""make.fun entry: "The Long Roast: Lawmakers and the File They Cannot Convert".

The whole entry is a single sentence, so the program has a single job:
put that sentence into entry.txt in the output folder, byte for byte,
with nothing after it -- not even a newline.
"""

import os
from pathlib import Path

# One sentence, as the brief demands: the authority is set up first,
# then undercut by the file the senator cannot convert himself.
ROAST = (
    "The senator regulating artificial intelligence opened the hearing "
    "by asking the witness to please print the internet, then adjourned "
    "to have an aide convert his own amendment from .pages to PDF."
)


def output_file() -> Path:
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def main() -> None:
    output_file().write_text(ROAST, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
