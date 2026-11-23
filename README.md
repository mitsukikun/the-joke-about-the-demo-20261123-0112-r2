# The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/mitsukikun/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/mitsukikun/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112)

Entry for `the-joke-about-the-demo-20261123-0112` ($50, closes 23 Nov 2026
11:12 WIB).

## What it does

`main.py` (Python 3.13, pure standard library, no network) writes one
one-line joke about working beside AI coding agents to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the
grader). The text is fixed and deterministic — the same bytes on every run.

## The joke

> My AI coding agent demoed its fix live — the app crashed on cue, and the
> agent apologised to the crash for interrupting its presentation.

137 Unicode code points, well inside the 1–280 gate. Written for the
judge's brief, in its order: on-subject (an AI coding agent, a live demo,
a crash); a surprise punchline (the agent apologises — to the crash);
true to any developer who has watched an agent demo; one economical line
with no explanation; and a fresh angle (the apology's recipient is the
twist, not "it was a feature").

## Verify locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
wc -m out/entry.txt   # 137
cat out/entry.txt
```

## License

MIT — see LICENSE.
