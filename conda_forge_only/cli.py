import click
from conda_forge_only.check import check_files
import sys

@click.command()
@click.argument("files", nargs=-1)
def cli(files):
    checks_passed = check_files(files)
    sys.exit(0 if all(checks_passed) else 1)
