from math import e, pi, sqrt

import pytest
from tuplesumfilter import pairs_that_sum_to, triplets_that_sum_to

pytestmark = pytest.mark.floats


def test_triplets_works_approx_with_floats():
    root2 = sqrt(2)
    nums = [pi, root2, 17.45, 1e-10, e]
    target = pi + e + root2
    expected = [(pytest.approx(pi), pytest.approx(root2), pytest.approx(e))]
    assert triplets_that_sum_to(nums, target) == expected


def test_pairs_works_approx_with_floats():
    root2 = sqrt(2)
    nums = [pi, root2, 17.45, 1e-10, e]
    target = pi + root2
    expected = [(pytest.approx(pi), pytest.approx(root2))]
    assert pairs_that_sum_to(nums, target) == expected
