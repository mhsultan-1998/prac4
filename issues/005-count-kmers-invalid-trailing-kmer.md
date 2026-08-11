# Issue #5 (hard) — `count_kmers` occasionally returns an invalid, too-short k-mer

**Labels:** `bug`, `needs-tests`, `priority-high`

`count_kmers(seq, k)` should only ever return keys that are exactly `k`
bases long. Right now, for certain sequence lengths, the sliding window
runs one step past where it should, and the last "k-mer" it records is
shorter than `k` — for example `count_kmers("ATGC", 2)` includes a
spurious `"C"` entry (length 1) alongside the three real 2-mers.

The existing test for this function only checks that specific expected
k-mers (like `"AT"` and `"GC"`) have the right count — it never checks
whether *extra*, invalid keys snuck into the result. That's exactly why
it currently passes despite the bug.

To catch this, you'll need to check something the current test doesn't:
either the full set of keys returned, or that every key has length `k`.
Add that test, then fix the off-by-one in the loop bound.

# Thankfully I have an understanding of how k-mers work but I was being really stupid not realizing I accidentally made an infinite loop. But for this one, a kmer is a sequential variation of the sequence as long as it matches the k length. So k = 2 for ATGCC would have AT, TG, GC, and CC. So I rewrote the function a little bit adding an index check where if it exceeded the sequence length, it'd break the for loop adding kmers. Why there wasn't an indexing error being raised is beyond me. I also adjusted the iterator range since it should go up to the sequence index with 1 less than k because the index slicing keeps one ahead of the second index slice value.