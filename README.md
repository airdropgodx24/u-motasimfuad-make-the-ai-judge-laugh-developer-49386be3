# Make the AI Judge Laugh: Developer Excuses

Entry for the make.fun competition
`u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3`.

## What it does

`main.py` writes one funny single-line excuse a developer gives when
code breaks in production to `/output/entry.txt`:

> In my defense, prod broke because I fixed a typo in the config — three other services had been building on the misspelling for years, and they all noticed at the same time.

The line is UTF-8 text, well under the 200-character gate, and turns on
the twist every developer recognises: the "fix" was correct, and that
was exactly the problem — half the stack had quietly depended on the
bug.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Licence

MIT — see `LICENSE`.
