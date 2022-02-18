import pytest
from tuplesumfilter import pairs_that_sum_to


@pytest.fixture
def worked_example_nums():
    return [1721, 979, 366, 299, 675, 1456]


def test_pairs_with_empty_input():
    assert pairs_that_sum_to([], 99) == []


def test_pairs_with_single_input():
    assert pairs_that_sum_to([1], 1) == []


def test_pairs_with_simple_match():
    assert pairs_that_sum_to([1, 2], 3) == [(1, 2)]


def test_pairs_worked_example(worked_example_nums):
    assert pairs_that_sum_to(worked_example_nums, 2020) == [(1721, 299)]


def test_pairs_with_finite_input_but_no_match(worked_example_nums):
    assert pairs_that_sum_to(worked_example_nums, 0) == []


def test_pairs_when_multiple_matches():
    example_input = [1, 979, 6, 299, 2, 1456, 5]
    assert pairs_that_sum_to(example_input, 7) == [(1, 6), (2, 5)]
