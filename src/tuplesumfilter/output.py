from dataclasses import dataclass
import math

from tuplesumfilter import types as t


def dimensions_for_display(n_dims: t.Int) -> t.Str:
    if n_dims == 2:
        return "pair"
    if n_dims == 3:
        return "triplet"
    return "n-tuple"


@dataclass
class FilterResult:
    """Helper to keep track of the n-tuples that make it through the summation filter
    and to display them
    """

    passed_filter: t.TuplePassedFilter

    def __str__(self) -> t.Str:
        return f"{self.passed_filter}"

    @property
    def dims_for_display(self) -> t.Str:
        return dimensions_for_display(len(self.passed_filter))

    @property
    def sum(self):
        return sum(self.passed_filter)

    @property
    def product(self):
        return math.prod(self.passed_filter)
