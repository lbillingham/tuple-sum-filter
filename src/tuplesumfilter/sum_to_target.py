import itertools
import math

import tuplesumfilter.types as t
from tuplesumfilter.app_logging import get_logger

FLOAT_COMPARISON_REL_TOL = 1e-8

logger = get_logger()


def pairs_that_sum_to(numbers: t.Sequence[t.Num], sum_target: t.Num) -> t.PairsOfNums:
    logger.bind(
        sum_kind="pairs",
        sum_target=sum_target,
        len_input=len(numbers),
        algo="itertools",
    )
    pairs = itertools.combinations(numbers, 2)
    filtered = [pair for pair in pairs if sum(pair) == sum_target]
    logger.debug(f"found {len(filtered)} pair sequences that sum to {sum_target}")
    return filtered


def triplets_that_sum_to(
    numbers: t.Sequence[t.Num], sum_target: t.Num
) -> t.TripletsOfNums:
    logger.bind(
        sum_kind="triplets",
        sum_target=sum_target,
        len_input=len(numbers),
        algo="itertools",
    )
    triplets = itertools.combinations(numbers, 3)
    filtered = [
        triplet
        for triplet in triplets
        if math.isclose(sum(triplet), sum_target, rel_tol=FLOAT_COMPARISON_REL_TOL)
    ]
    logger.debug(f"found {len(filtered)} triplet sequences that sum to {sum_target}")
    return filtered
