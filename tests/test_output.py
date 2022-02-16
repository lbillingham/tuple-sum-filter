from tuplesumfilter.output import FilterResult, dimensions_for_display


def test_display_pair():
    got = FilterResult((1, 6))
    assert str(got) == "(1, 6)"
    assert got.sum == 7
    assert got.product == 6
    assert got.dims_for_display == "pair"


def test_display_triplet():
    got = FilterResult((1, 10, 100))
    assert str(got) == "(1, 10, 100)"
    assert got.sum == 111
    assert got.product == 1_000
    assert got.dims_for_display == "triplet"


def test_display_dimensions():
    assert dimensions_for_display(1) == "n-tuple"
    assert dimensions_for_display(2) == "pair"
    assert dimensions_for_display(3) == "triplet"
    assert dimensions_for_display(4) == "n-tuple"
