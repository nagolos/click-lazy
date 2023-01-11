import click


@click.group()
def cli():
    """This script"""


@cli.command(name='easy_cmd')
def run_easy_cmd():
    print('Running command from easy group file')
