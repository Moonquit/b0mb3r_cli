import os
from pathlib import Path

import click


@click.command()
def main():
    path = os.path.dirname(os.path.abspath(__file__))
    os.system(f"{Path(path) / '__main__.py'}")

main()
