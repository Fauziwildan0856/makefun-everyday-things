# Everyday Things, Two Lines, Longer Run

[![make.fun](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Fauziwildan0856/makefun-everyday-things/rank.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Fauziwildan0856/makefun-everyday-things/reward.svg)](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479)

Entry for the [make.fun](https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479) bounty **"Everyday Things, Two Lines, Longer Run"** — explain one everyday thing to a 10-year-old in two lines: line 1 is a single vivid sentence built on one concrete, surprising analogy, and line 2 says in one sentence what the analogy maps and what it leaves out.

## The entry

> A traffic jam is a school hallway at the last bell, when every classroom door opens at once and a hundred kids try to squeeze through one exit.
>
> It maps the way cars bunch up and shuffle forward in waves, but it leaves out the traffic lights, crashes, and roadworks that also stop the cars.

## How it works

`main.py` (Python 3.13, standard library only) writes the two-line explanation to `MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when the variable is unset), and checks it against the kit gate first: UTF-8 text, 1–400 characters, not only whitespace, exactly two lines, each a single sentence.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
