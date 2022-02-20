import itertools
import math

import tuplesumfilter.types as t
from tuplesumfilter.app_logging import get_logger

FLOAT_COMPARISON_REL_TOL = 1e-8

logger = get_logger()


def _comparitor(number: t.Num, sum_target: t.Num) -> t.Boolean:
    """really just a single place to switch between == and math.isclose"""
    return number == sum_target
    # return math.isclose(number, sum_target, rel_tol=1e-09)


def pairs_that_sum_to(numbers: t.Sequence[t.Num], sum_target: t.Num) -> t.PairsOfNums:
    logger.bind(
        sum_kind="pairs",
        sum_target=sum_target,
        len_input=len(numbers),
        algo="w-storage-int-only",
    )
    already_seen = set()
    summed = []
    for comparitor in numbers:
        if (sum_target - comparitor) in already_seen:
            summed.append((sum_target - comparitor, comparitor))
        already_seen.add(comparitor)
    logger.debug(f"found {len(summed)} pair sequences that sum to {sum_target}")
    return summed


def triplets_that_sum_to(
    numbers: t.Sequence[t.Num], sum_target: t.Num
) -> t.TripletsOfNums:
    logger.bind(
        sum_kind="triplets",
        sum_target=sum_target,
        len_input=len(numbers),
        algo="nested",
    )
    summed = []
    for ileft, left in enumerate(numbers):
        for jcentre, center in enumerate(numbers[ileft + 1 :]):
            for right in numbers[(ileft + jcentre + 2) :]:
                if _comparitor(left + center + right, sum_target):
                    summed.append((left, center, right))
    logger.debug(f"found {len(summed)} triplet sequences that sum to {sum_target}")
    return summed
