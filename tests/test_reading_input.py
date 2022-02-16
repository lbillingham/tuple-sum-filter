from pathlib import Path
from this import d

import pytest

from tuplesumfilter import numbers_in_file
from tuplesumfilter.read_input import UnknownFileFormat

DATA_DIR = Path(__file__).absolute().parent / "__test_data__"


def test_reading_non_existant_file_raises():
    non_existant_filename = "rfijweafiojsad"
    with pytest.raises(FileNotFoundError):
        numbers_in_file(DATA_DIR / non_existant_filename)


def test_reading_non_numeric_file_content_raises():
    with pytest.raises(UnknownFileFormat):
        numbers_in_file(DATA_DIR / "non_numeric_input.txt")


def test_reading_numeric_but_not_newline_seperated_raises():
    with pytest.raises(UnknownFileFormat):
        numbers_in_file(DATA_DIR / "comma_and_newline_seperated.txt")


def test_reading_worked_example():
    expected = [1721, 979, 366, 299, 675, 1456]
    assert numbers_in_file(DATA_DIR / "worked_example.txt") == expected


def test_reading_mixed_floats_and_ints_gives_floats():
    got_from_file = numbers_in_file(DATA_DIR / "mixed_ints_and_floats.txt")
    expected = [pytest.approx(n) for n in [1721.0, 979.0, 366.0, 29.9, 675.0, 14.56]]
    assert got_from_file == expected
    assert all(isinstance(n, float) for n in got_from_file)
