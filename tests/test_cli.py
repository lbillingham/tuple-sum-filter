from click.testing import CliRunner
import pytest

from tuplesumfilter.scripts import cli


@pytest.fixture
def tmp_file_of_numbers(tmp_path):
    tmp_file = tmp_path / "temp_input.txt"
    tmp_file.write_text("1721\n979\n366\n299\n675\n1456\n")
    return tmp_file


def test_cli_when_minimal_args_supplied(tmp_file_of_numbers):
    runner = CliRunner()
    filepath = tmp_file_of_numbers.absolute().as_posix()
    result = runner.invoke(cli, args=f"--input_file={filepath}")
    assert result.exit_code == 0


def test_cli_when_args_supplied_and_no_match(tmp_file_of_numbers):
    runner = CliRunner()
    filepath = tmp_file_of_numbers.absolute().as_posix()
    result = runner.invoke(
        cli, args=f"--input_file={filepath} --dimension=3 --sum_target=9999"
    )
    assert result.exit_code == 0
