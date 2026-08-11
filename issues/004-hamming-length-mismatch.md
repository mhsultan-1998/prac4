# Issue #4 (medium) — `hamming_distance` silently ignores length mismatches

**Labels:** `bug`, `needs-tests`

Per spec, `hamming_distance` should raise a `ValueError` when given two
sequences of different lengths, since comparing sequences of unequal
length position-by-position isn't a meaningful operation.

Right now it doesn't check lengths at all — it uses `zip`, which
silently stops at the shorter sequence. So
`hamming_distance("ATGC", "ATG")` doesn't raise anything; it just quietly
compares the first 3 characters and returns a number that looks like a
valid answer but isn't one.

The existing tests only use equal-length inputs, so none of them catch
this. Add a test with mismatched lengths that expects a `ValueError`,
then add the missing validation.

# Did exactly as this bug requested adding a mismatched length test case. Fixed this bug by adding an if statement comparing sequence lengths.