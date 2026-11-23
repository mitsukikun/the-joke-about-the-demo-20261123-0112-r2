"""Write a one-line joke about working beside AI coding agents.

The program writes the joke to entry.txt inside the output directory
($MAKEFUN_OUTPUT_DIR when set, otherwise /output), creating the
directory if it does not exist yet.
"""

import os
from pathlib import Path

JOKE = "My AI coding agent demoed its fix live — the app crashed on cue, and the agent apologised to the crash for interrupting its presentation."


def main() -> None:
    # Gate: the entry must be 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    assert JOKE.strip(), "joke must not be only whitespace"

    # Deterministic: the same constant is written every run, with no
    # trailing newline, so the output is byte-identical each time.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
