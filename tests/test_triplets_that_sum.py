from math import e, pi, sqrt
import pytest
from tuplesumfilter import triplets_that_sum_to


@pytest.fixture
def worked_example_nums():
    return [1721, 979, 366, 299, 675, 1456]


def test_triplets_with_empty_input():
    assert triplets_that_sum_to([], 2020) == []


def test_triplets_with_single_input():
    assert triplets_that_sum_to([1], 1) == []


def test_triplets_with_simple_match():
    assert triplets_that_sum_to([1, 2, 3], 6) == [(1, 2, 3)]


def test_triplets_ignores_pairs_and_singles():
    assert triplets_that_sum_to([1, 2, 3], 3) == []


def test_triplets_worked_example(worked_example_nums):
    assert triplets_that_sum_to(worked_example_nums, 2020) == [(979, 366, 675)]


def test_triplets_with_finite_input_but_no_match(worked_example_nums):
    assert triplets_that_sum_to(worked_example_nums, 0) == []


def test_triplets_works_approx_with_floats():
    nums = [pi, sqrt(2), 17.45, 1e-10, e]
    target = pi + e + sqrt(2)
    expected = [(pytest.approx(pi), pytest.approx(sqrt(2)), pytest.approx(e))]
    assert triplets_that_sum_to(nums, target) == expected


def test_triplets_when_multiple_matches():
    input = [10, 979, 5, 299, 2, 1456, 6, 8, 3]
    assert triplets_that_sum_to(input, 17) == [(10, 5, 2), (6, 8, 3)]
