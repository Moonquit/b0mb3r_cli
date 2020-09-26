import click

from .__main__ import cli_start

@click.command()
def main():
    cli_start()

main()
