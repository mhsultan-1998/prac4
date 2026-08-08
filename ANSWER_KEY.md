# Answer Key — attempt all six issues before opening this

## Issue #1 (easy) — reverse_complement

**Fix:**
```python
def reverse_complement(seq: str) -> str:
    complemented = "".join(COMPLEMENT[base] for base in seq)
    return complemented[::-1]
```

---

## Issue #2 (easy) — translate frameshift

**Fix:**
```python
for i in range(0, len(seq), 3):   # was range(1, len(seq), 3)
```

---

## Issue #3 (medium) — gc_content case sensitivity

**Fix:**
```python
def gc_content(seq: str) -> float:
    if not seq:
        return 0.0
    seq = seq.upper()
    gc = sum(1 for base in seq if base in "GC")
    return gc / len(seq)
```

**Test to add:**
```python
def test_gc_content_lowercase():
    assert gc_content("gcgc") == 1.0
```

---

## Issue #4 (medium) — hamming_distance length validation

**Fix:**
```python
def hamming_distance(seq1: str, seq2: str) -> int:
    if len(seq1) != len(seq2):
        raise ValueError("sequences must be the same length")
    return sum(1 for a, b in zip(seq1, seq2) if a != b)
```

**Test to add:**
```python
def test_hamming_distance_length_mismatch_raises():
    with pytest.raises(ValueError):
        hamming_distance("ATGC", "ATG")
```

---

## Issue #5 (hard) — count_kmers off-by-one

**Fix:**
```python
for i in range(len(seq) - k + 1):   # was range(len(seq) - k + 2)
```

**Test to add** (checks the thing the original test didn't):
```python
def test_count_kmers_no_short_kmers():
    counts = count_kmers("ATGC", 2)
    assert counts == {"AT": 1, "TG": 1, "GC": 1}
    assert all(len(kmer) == 2 for kmer in counts)
```

**Why the original test missed it:** it only asserted specific keys'
values (`counts["AT"] == 1`), never the full key set or key lengths — so
an extra spurious short key could exist undetected forever.

---

## Issue #6 (hard) — sliding_window_mean_quality drops trailing bases

**Fix:**
```python
for i in range(0, len(scores), window):   # was range(0, len(scores) - window + 1, window)
```

**Test to add**, worked by hand (quality string `"IIIIIIIIII"`, 10
characters, `I` = Phred+33 score 40 for every character, window = 3):

```python
def test_sliding_window_mean_quality_nonexact_multiple():
    quality = "IIIIIIIIII"  # 10 bases, all score 40
    result = sliding_window_mean_quality(quality, 3)
    # 10 bases / window 3 -> windows of size 3, 3, 3, 1 = 4 windows total
    assert result == [40.0, 40.0, 40.0, 40.0]
    assert len(result) == 4
```

**Why the original test missed it:** 6 bases with window 3 divides
evenly into exactly 2 full windows with nothing left over, so the
"drop the trailing partial window" bug has literally nothing to drop on
that input — it behaves identically to correct code. The bug is only
observable when `len(quality) % window != 0`.
