import click


@click.group()
def cli():
    """This script"""


@cli.command(name='thecmd')
def run_thecmd():
    pass
