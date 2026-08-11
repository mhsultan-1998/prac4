import pytest

from seqtools import (
    count_kmers,
    gc_content,
    hamming_distance,
    reverse_complement,
    sliding_window_mean_quality,
    translate,
)


def test_reverse_complement_basic():
    assert reverse_complement("ATGC") == "GCAT"


def test_translate_basic():
    assert translate("ATGTTTTAA") == "MF"


def test_gc_content_uppercase():
    assert gc_content("GCGC") == 1.0


def test_gc_content_lowercase():
    assert gc_content("gcgc") == 1.0


def test_gc_content_mixedcase():
    assert gc_content("gcGc") == 1.0


def test_gc_content_mixed_gc_and_at():
    assert gc_content("ATGC") == 0.5


def test_hamming_distance_equal_length():
    assert hamming_distance("ATGC", "ATCC") == 1


def test_hamming_distance_unequal_length():
    assert hamming_distance("ATGC", "ATC") is ValueError


def test_hamming_distance_identical():
    assert hamming_distance("ATGC", "ATGC") == 0


def test_count_kmers_known_kmer_present():
    counts = count_kmers("ATGC", 2)
    assert counts["AT"] == 1
    assert counts["GC"] == 1


def test_count_kmers_known_kmer_present_bad_count():
    counts = count_kmers("ATGCC", 2)
    assert counts["AT"] == 1
    assert counts["GC"] == 1
    assert ("C" not in counts)
    # so the counts for "C" should be easy since the kmer length is less than k.


def test_sliding_window_mean_quality_exact_multiple():
    # 6 bases, window 3 -> divides evenly, bug is invisible on this input
    quality = "IIIIII"
    result = sliding_window_mean_quality(quality, 3)
    assert result == [40.0, 40.0]

def test_sliding_window_mean_quality_exact_multiple_uneven():
    # 6 bases, window 3 -> divides evenly, bug is invisible on this input
    quality = "IIIIIII"
    result = sliding_window_mean_quality(quality, 3)
    assert result == [40.0, 40.0, 40.0]
