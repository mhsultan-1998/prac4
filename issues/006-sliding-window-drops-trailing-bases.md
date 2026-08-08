# Issue #6 (hard) — `sliding_window_mean_quality` silently drops trailing bases

**Labels:** `bug`, `needs-tests`, `priority-high`

Per spec, every base in the quality string must end up in exactly one
window, including a shorter final window when the length isn't an exact
multiple of the window size. Right now, whenever the length doesn't
divide evenly, the leftover bases at the end are silently dropped —
they never appear in any window, and there's no error or warning.

The existing test uses a quality string whose length is an exact
multiple of the window size (6 bases, window 3), so all 6 bases happen
to get covered by 2 full windows and the bug produces no visible
difference on that input at all.

This is a data-loss bug, not a crash — it will never show up unless the
test input is specifically chosen so that `len(quality) % window != 0`.
Add a test with a length that doesn't divide evenly (e.g. 10 bases,
window 3, which should produce 4 windows: three of size 3 and one final
window of size 1), work out by hand what the correct output should be,
then fix the implementation so no bases are dropped.
