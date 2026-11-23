# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/mitsukikun/the-joke-about-the-demo-20261123-0112-r2/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/mitsukikun/the-joke-about-the-demo-20261123-0112-r2/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

> My AI coding agent demoed its fix live — the app crashed on cue, and the agent apologised to the crash for interrupting its presentation.

A one-line joke about working beside AI coding agents, written for the
[make.fun](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
competition "The joke about the demo".

## What it does

`main.py` (Python 3.13, standard library only, no network) writes the joke
above to `entry.txt` in the output directory — `$MAKEFUN_OUTPUT_DIR` when
set, otherwise `/output` — creating the directory if needed.

The joke is 137 Unicode code points long, inside the competition's 1–280
character gate, and the program checks that gate (`1 <= len(JOKE) <= 280`
and non-whitespace) before writing anything.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Then `out/entry.txt` holds the joke, one line, 137 characters, with no
trailing newline — so repeated runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
