from pathlib import Path

from tuplesumfilter import numbers_in_file, pairs_that_sum_to, triplets_that_sum_to

INPUT1_FILE = Path("./tests/__test_data__") / "input1.txt"


def test_input1_pairs(benchmark):
    expected = [(1093, 927)]
    file_contents = numbers_in_file(INPUT1_FILE)
    got = benchmark(pairs_that_sum_to, file_contents, 2020)
    assert got == expected


def test_input1_triplets(benchmark):
    expected = [(481, 19, 1520)]
    file_contents = numbers_in_file(INPUT1_FILE)
    got = benchmark(triplets_that_sum_to, file_contents, 2020)
    assert got == expected
