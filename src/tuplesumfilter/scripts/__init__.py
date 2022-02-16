import click


@click.command()
@click.option("--who", default="World", help="Who to greet.")
def cli(who):
    click.echo(f"Hello {who}!")
