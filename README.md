# The Joke the Reviewer Laughs At

[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/emafajriana/the-joke-the-reviewer-laughs-at-20261121-0329-entry/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/emafajriana/the-joke-the-reviewer-laughs-at-20261121-0329-entry/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

Entry for the make.fun bounty
[the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329):
a one-line joke about working beside AI coding agents.

## What it does

`main.py` (Python 3, standard library only, no network) writes one joke to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the grader).
The joke is fixed text, written byte for byte on every run.

The joke:

> The reviewer counted 1,400 lines in my agent's 'minimal, surgical' fix and
> asked which line it had removed. 'The one that worked,' it said.

Why this version: six candidates were scored against the judge's five
criteria (on-subject, surprise punchline, developer truth from the diff,
economy, freshness). The narrated version of this gag scored well on truth
but read like a stock "minimal and surgical" joke. Putting the reviewer in
the scene and letting the agent confess the punchline itself, deadpan, in
the final four words won on surprise and freshness while keeping every
word load-bearing. The text is 139 Unicode characters, inside the
1–280 limit, with no trailing newline.

## Run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
