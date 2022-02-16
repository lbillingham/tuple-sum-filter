from click.testing import CliRunner

from tuplesumfilter.scripts import cli


def test_cli_when_no_args_supplied():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0


def test_cli_when_supply_who_arg():
    runner = CliRunner()
    result = runner.invoke(cli, args=f"--who=there")
    assert result.exit_code == 0
