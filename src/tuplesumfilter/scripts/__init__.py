import click

from tuplesumfilter import numbers_in_file, pairs_that_sum_to
from tuplesumfilter.output import FilterResult, dimensions_for_display
from tuplesumfilter import types as t


@click.command()
@click.option(
    "--input_file",
    help="A file of newline-delimited numbers.",
    type=str,  # we don't use click.File here because we deal with Path | str vs IOWrapper internally
    prompt=True,
    required=True,
)
@click.option(
    "--sum_target", default=2020, show_default=True, help="A positive number."
)
@click.option(
    "--dimension",
    type=click.Choice(["2", "3"]),
    default="2",
    show_default=True,
    help="2 for sums between pairs, 3 for sums between triplets",
)
def cli(input_file: t.Pathlike, sum_target: t.Num, dimension: t.Str):
    numbers = numbers_in_file(input_file)
    numeric_dimension = int(dimension)
    dims_disp = dimensions_for_display(numeric_dimension)
    click.echo(
        f"checking for {dims_disp}s of numbers that sum to {sum_target} in {input_file}"
    )
    results = pairs_that_sum_to(numbers, sum_target)
    if not results:
        click.echo(
            f"No matches found for {dims_disp} in {input_file} that sum to {sum_target}"
        )

    for result in results:
        disp_result = FilterResult(result)
        click.echo(
            f"Results {disp_result.dims_for_display} {disp_result} match: sum to {disp_result.sum} and multiply to {disp_result.product}"
        )
