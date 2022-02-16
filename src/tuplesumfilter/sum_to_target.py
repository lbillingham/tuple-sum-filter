import itertools
import tuplesumfilter.types as t


def pairs_that_sum_to(numbers: t.Sequence[t.Num], sum_target: t.Num) -> t.PairsOfNums:
    pairs = itertools.combinations(numbers, 2)
    filtered = [pair for pair in pairs if sum(pair) == sum_target]
    return filtered
