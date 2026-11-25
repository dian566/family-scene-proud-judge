#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene — one short family scene.

Writes a single warm, funny, heartfelt domestic moment to
/output/entry.txt. The bounty gate requires UTF-8 text of 1-280
characters, not only whitespace, in one or two lines.
"""

import os
import sys

SCENE = (
    "Mom keeps every crayon drawing I ever made in a shoebox labelled "
    "'Masterpieces \u2014 do not throw away.' Last week she added my tax "
    "return to the box. 'For the collection,' she said."
)


def validate(text: str) -> str:
    """Return the entry text, or raise if it cannot pass the bounty gate."""
    if "\r" in text:
        raise ValueError("entry must not contain carriage returns")
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or whitespace only")
    if len(stripped) > 280:
        raise ValueError(f"entry is {len(stripped)} characters, over the 280 limit")
    if stripped.count("\n") > 1:
        raise ValueError("entry must be one or two lines")
    lines = [line.rstrip() for line in stripped.split("\n")]
    return "\n".join(lines)


def main() -> int:
    try:
        text = validate(SCENE)
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
