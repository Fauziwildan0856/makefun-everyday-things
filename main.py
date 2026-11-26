"""Everyday Things, Two Lines, Longer Run -- make.fun entry.

Writes a two-line explanation of a traffic jam to a 10-year-old
to MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the
variable is unset). Standard library only.

Judge brief, in short: line 1 explains one everyday thing in a
single vivid sentence built on ONE concrete, surprising analogy --
things a 10-year-old can see, hold or stand in, no list of
comparisons, no second metaphor. Line 2 says in one sentence why
the analogy works: what it maps AND what it leaves out, honestly
and specifically, in language a 10-year-old follows without
being talked down to.
"""

import os
from pathlib import Path

ENTRY = (
    "A traffic jam is a school hallway at the last bell, when every "
    "classroom door opens at once and a hundred kids try to squeeze "
    "through one exit.\n"
    "It maps the way cars bunch up and shuffle forward in waves, but "
    "it leaves out the traffic lights, crashes, and roadworks that "
    "also stop the cars."
)


def check_entry(text: str) -> None:
    """Enforce the kit gate locally before writing anything.

    The sealed scorer requires UTF-8 text of 1-400 characters that
    is not only whitespace; the judge brief additionally requires
    exactly two lines, each a single sentence.
    """
    if not 1 <= len(text) <= 400:
        raise SystemExit(
            f"entry fails the kit gate: {len(text)} characters "
            "(must be 1-400)"
        )
    if not text.strip():
        raise SystemExit("entry fails the kit gate: only whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise SystemExit(
            f"entry fails the judge brief: {len(lines)} lines, "
            "expected exactly 2"
        )
    for i, line in enumerate(lines, start=1):
        # One sentence means exactly one sentence terminator, and it
        # must close the line: a second terminator (or a "!" / "?")
        # would mean a second sentence crowding the line.
        terminators = sum(line.count(mark) for mark in ".!?")
        if terminators != 1 or line[-1] not in ".!?":
            raise SystemExit(
                f"entry fails the judge brief: line {i} is not "
                "exactly one sentence"
            )


def main() -> None:
    check_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {target}")


if __name__ == "__main__":
    main()
