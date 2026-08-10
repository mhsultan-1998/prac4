COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}

CODON_TABLE = {
    "ATG": "M",
    "TTT": "F",
    "TTC": "F",
    "TAA": "*",
    "TAG": "*",
    "TGA": "*",
    "GGG": "G",
    "AAA": "K",
    "CCC": "P",
    "TGG": "W",
}


def reverse_complement(seq: str) -> str:
    """Return the reverse complement of a DNA sequence.

    Each base is complemented (A<->T, G<->C) and the resulting string is
    then reversed, matching the standard 5'->3' reverse-strand
    convention. Input is assumed to already be uppercase.
    """
    complemented = "".join(COMPLEMENT[base] for base in seq)
    return complemented[::-1]
# Can do the string reversal earlier but this works too. Very minimal fix.


def translate(seq: str) -> str:
    """Translate a DNA sequence into a protein string.

    Reads the sequence in consecutive, non-overlapping codons starting
    at index 0 (the first three bases are the first codon). Translation
    stops at the first stop codon, and the stop codon itself is not
    included in the returned protein string.
    """
    protein = []
    for i in range(0, len(seq), 3):
        codon = seq[i:i + 3]
        amino = CODON_TABLE.get(codon)
        if amino is None or amino == "*":
            break
        protein.append(amino)
    return "".join(protein)


def gc_content(seq: str) -> float:
    """Fraction of bases that are G or C.

    Must be case-insensitive: lowercase and uppercase bases are counted
    identically. An empty sequence has a GC content of 0.0.
    """
    if not seq:
        return 0.0
    seq = seq.upper()
    gc = sum(1 for base in seq if base in "GC")
    return gc / len(seq)


def count_kmers(seq: str, k: int) -> dict[str, int]:
    """Count all overlapping k-mers of length k in seq.

    A k-mer is only valid if it is exactly k bases long. The sliding
    window must never be allowed to run past the end of the sequence
    and produce a shorter, invalid k-mer.
    """
    counts: dict[str, int] = {}
    check = 0
    for i in range(len(seq) - k + 1):
        if check > len(seq):
            break
        check = i + k
        # print("i:", i)
        # print("check:", check)
        kmer = seq[i:check]
        counts[kmer] = counts.get(kmer, 0) + 1
        # print(counts)
        check += 1
    return counts


    # counts: dict[str, int] = {}
    #     for i in range(len(seq) - k + 2):
    #         kmer = seq[i:i + k]
    #         counts[kmer] = counts.get(kmer, 0) + 1
    #     return counts
# I hate how this function is written, and why is there no indexing error being raised?

# Why isn't there an indexing error?!


def hamming_distance(seq1: str, seq2: str) -> int:
    """Count the number of differing positions between two sequences.

    seq1 and seq2 must be the same length for the comparison to be
    meaningful. If they are different lengths, this must raise a
    ValueError rather than silently comparing only the overlapping
    portion.
    """
    if len(seq1) != len(seq2):
        return ValueError
    return sum(1 for a, b in zip(seq1, seq2) if a != b)


def sliding_window_mean_quality(quality: str, window: int) -> list[float]:
    """Mean Phred+33 quality score for each consecutive window.

    The quality string is split into consecutive, non-overlapping
    windows of size `window`, in order, starting at position 0. Every
    base in the input must appear in exactly one window, including a
    final shorter window when len(quality) is not an exact multiple of
    `window` — no base may be silently dropped.
    """
    scores = [ord(ch) - 33 for ch in quality]
    result = []

    # for i in range(0, len(scores) - window + 1, window):
    #     chunk = scores[i:i + window]
    #     result.append(sum(chunk) / len(chunk))

    check = 0
    # chunk = 0
    while check < len(scores):
        if (check+window) > (len(scores)-1):
            chunk = scores[check:]
            # print("check:", check)
            result.append(sum(chunk) / len(chunk))
            # print(result)
            check = len(scores)
        elif (check+window) <= (len(scores)-1):
            chunk = scores[check:check+window]
            # print("check:", check)
            result.append(sum(chunk) / len(chunk))
            # print(result)
            check += window
            # print(check)

    return result

quality = "IIIIII"
result = sliding_window_mean_quality(quality, 3)
print(result)

print("\n")
quality = "IIIIIII"
result = sliding_window_mean_quality(quality, 3)
print(result)






