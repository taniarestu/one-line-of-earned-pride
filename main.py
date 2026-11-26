#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text, 1 to 240 characters, to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.

Stdlib only, no network, fully deterministic: the same bytes on every run.
"""

from pathlib import Path

ENTRY = (
    "After a year of practising in the bathroom mirror, "
    "ten-year-old Sam read the school assembly announcement "
    "all the way through without stumbling once, "
    "then sat down like nothing had happened."
)


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 240):
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {out}")


if __name__ == "__main__":
    main()
