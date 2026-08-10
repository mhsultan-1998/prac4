# Issue #2 (easy) — `translate` reads codons in the wrong frame

**Labels:** `bug`, `good first issue`

`translate("ATGTTTTAA")` should read three codons — `ATG` (M), `TTT`
(F), `TAA` (stop) — and return `"MF"`. It currently starts reading one
base too late (frame shifted by 1), so it never lines up with real
codons and returns an empty string.

There is already a failing test that shows this directly.

# Fascinating case. Because does this function work with sequences where the first 3 bases aren't ATG (start codon)?
# Fixing this bug was simple because the range of numbers being iterated through starts at 1 instead of 0, classic python indexing flaw.
