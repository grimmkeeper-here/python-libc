import click

from app.cli.libc import cli as libc_cli


@click.group()
def cli() -> None:
    pass


def init_cli() -> None:
    cli.add_command(libc_cli)
