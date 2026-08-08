# seqtools

Toy bioinformatics repository — small DNA sequence utilities
(reverse complement, translation, GC content, k-mer counting, Hamming
distance, quality-score windowing).

## Setup

```bash
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

python -m pip install -r requirements.txt
python -m pip install -e .
python -m pytest
```

## Interview simulation

This repository has **six open issues**, described in `issues/`, spread
across three difficulty tiers — two of each:

- **Easy (#1, #2):** already caught by a failing test. Read the
  failure, find the line, fix it.
- **Medium (#3, #4):** the current test suite is green for these, but
  only because the given tests happen not to exercise the input that
  breaks. You're told exactly what's wrong in the issue — the skill
  being practiced is recognizing that "tests pass" isn't the same
  claim as "code is correct," writing the missing test yourself, and
  then fixing it.
- **Hard (#5, #6):** also green right now, and also fully described in
  their issue files — nothing here is a mystery. What makes these hard
  is that the correct output requires you to reason precisely about
  the specified behavior (or work out expected values by hand) before
  you can tell right from wrong, and the existing tests were built in
  a way that structurally cannot detect the bug regardless of luck.

No time limit on this one. Work through all six at whatever pace lets
you actually reason carefully, especially #5 and #6. `ANSWER_KEY.md` has
the exact fix and regression test for each — don't open it until you've
attempted the issue yourself.

Once you can get through all six cleanly untimed, try a second full pass
with a 45–60 minute cap for a closer simulation of the real thing (which
will only have a couple of issues, not six — this repo is intentionally
denser for practice volume).

Do not rewrite unrelated code. Keep each fix scoped to the issue it
addresses, and use a real branch → commit → push → PR cycle per issue.
