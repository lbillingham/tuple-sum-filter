import tuplesumfilter.types as t
from tuplesumfilter.app_logging import get_logger

FLOAT_COMPARISON_REL_TOL = 1e-8

logger = get_logger()


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
        already_seen = set()
        still_need = sum_target - left
        for right in numbers[ileft + 1 :]:
            if still_need - right in already_seen:
                summed.append((left, (sum_target - left - right), right))
            already_seen.add(right)
    logger.debug(f"found {len(summed)} triplet sequences that sum to {sum_target}")
    return summed
