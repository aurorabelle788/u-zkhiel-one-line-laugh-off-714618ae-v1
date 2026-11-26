# One-Line Laugh-Off

[![One-Line Laugh-Off](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/aurorabelle788/u-zkhiel-one-line-laugh-off-714618ae-v1/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/aurorabelle788/u-zkhiel-one-line-laugh-off-714618ae-v1/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

Entry for the [One-Line Laugh-Off](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae) bounty on make.fun.

## What it does

`main.py` (Python 3.13, standard library only, no network, fully deterministic)
writes exactly one original funny one-liner to `/output/entry.txt`:

> I taught my parrot to say 'help' — now the neighbors think I'm the hostage.

## Run

```sh
python3 main.py
```

The program asserts the line is 1–200 characters, a single line, non-blank,
valid UTF-8, creates `/output` if needed, and writes the line to
`/output/entry.txt`.
