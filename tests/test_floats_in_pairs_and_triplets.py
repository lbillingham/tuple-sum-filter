from math import e, pi, sqrt

import pytest
from tuplesumfilter import pairs_that_sum_to, triplets_that_sum_to


def test_triplets_works_approx_with_floats():
    nums = [pi, sqrt(2), 17.45, 1e-10, e]
    target = pi + e + sqrt(2)
    expected = [(pytest.approx(pi), pytest.approx(sqrt(2)), pytest.approx(e))]
    assert triplets_that_sum_to(nums, target) == expected


def test_pairs_works_approx_with_floats():
    nums = [pi, sqrt(2), 17.45, 1e-10, e]
    target = pi + e
    expected = [(pytest.approx(pi), pytest.approx(e))]
    assert pairs_that_sum_to(nums, target) == expected
