# Issue #1 (easy) — `reverse_complement` returns the complement but never reverses it

**Labels:** `bug`, `good first issue`

`reverse_complement("ATGC")` should return `"GCAT"` (complement each base,
then reverse the whole string). It currently returns `"TACG"` — the
complement step is correct, the reverse step is simply missing.

There is already a failing test that shows this directly.
