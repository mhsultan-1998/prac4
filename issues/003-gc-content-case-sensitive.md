# Issue #3 (medium) — `gc_content` is case-sensitive

**Labels:** `bug`, `needs-tests`

`gc_content` is documented to be case-insensitive — lowercase and
uppercase bases should count the same way. It currently only matches
uppercase `G`/`C`, so a lowercase sequence like `"gcgc"` incorrectly
comes back as `0.0` instead of `1.0`.

The existing tests only use uppercase input, so they all pass right now
even though the bug is real. Add a test using a lowercase sequence to
expose it, then fix the implementation.

# After verifying the input is legit, just run a simple .upper() function on the string. But add another test case just to show even a mix of upper and lower cased sequences won't cause an issue.