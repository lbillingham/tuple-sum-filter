import itertools
import math

import tuplesumfilter.types as t
from tuplesumfilter.app_logging import get_logger

FLOAT_COMPARISON_REL_TOL = 1e-8

logger = get_logger()


def pairs_that_sum_to(numbers: t.Sequence[t.Num], sum_target: t.Num) -> t.PairsOfNums:
    logger.bind(
        sum_kind="pairs", sum_target=sum_target, len_input=len(numbers), algo="nested"
    )
    summed = []
    for ileft, left in enumerate(numbers):
        for right in numbers[ileft + 1 :]:
            if math.isclose(sum_target, left + right, rel_tol=1e-09):
                summed.append((left, right))
    logger.debug(f"found {len(summed)} pair sequences that sum to {sum_target}")
    return summed


def triplets_that_sum_to(
    numbers: t.Sequence[t.Num], sum_target: t.Num
) -> t.TripletsOfNums:
    logger.bind(
        sum_kind="triplets",
        sum_target=sum_target,
        len_input=len(numbers),
        algo="itertools",
    )
    triplets = list(ntuples_that_sum_to(numbers, sum_target, 3))
    logger.debug(f"found {len(triplets)} triplet sequences that sum to {sum_target}")
    # i promise mypy, again, that we _are_ narrowing the types here
    return t.cast(t.TripletsOfNums, triplets)


def ntuples_that_sum_to(
    numbers: t.Sequence[t.Num], sum_target: t.Num, dimensions: t.Int
) -> t.Generator[t.NTupelOfNums, None, None]:
    """
    Filters a the input `numbers` by whether their n-tuple combinations
    sum to match the `sum_target`, the n in n-tuple is controlled by `dimensions`.
    e.g. pairs of numbers for dimenions==2

    Returns
    -------
    A generator from which we can pull the matching combinations.

    >>> input = [1, 2, 3, 4]
    >>> list(ntuples_that_sum_to(input, 7, 3))
    >>> [(1, 2, 4)]
    """
    n_tuples = itertools.combinations(numbers, dimensions)
    filtered = (
        n_tuple
        for n_tuple in n_tuples
        if math.isclose(sum(n_tuple), sum_target, rel_tol=FLOAT_COMPARISON_REL_TOL)
        # if sum(n_tuple) == sum_target
    )
    return filtered
