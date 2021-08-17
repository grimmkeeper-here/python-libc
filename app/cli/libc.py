import json
import os.path
import subprocess

import click
from click import Group

from app.core.config import constants

cli = Group("libc", help="CLI for libc install")


@cli.command("list", help="List all libc is installed")
def list_libc():
    cmd = f"python libc.py"
    cmd_exec = subprocess.Popen(cmd, shell=True)
    cmd_exec.wait()


@cli.command("install", help="Install all libc can")
def install_libc():
    with open(f"{constants.LIBC_PATH}/{constants.LIBC_NAME}") as fi:
        libs = json.loads(fi.read())
        for lib in libs:
            if os.path.isfile(
                f"{constants.LIBC_PATH}/{constants.LIBC_SOURCE}/%(_file)s.c" % lib
            ):
                cmd = (
                    f"gcc -fPIC -shared -o {constants.LIBC_PATH}/{constants.LIBC_LIB}/%(_file)s.so {constants.LIBC_PATH}/{constants.LIBC_SOURCE}/%(_file)s.c"
                    % lib
                )
                cmd_exec = subprocess.Popen(cmd, shell=True)
                cmd_exec.wait()
                click.echo(
                    f"Lib: %(name)s - Source: %(_file)s.c has been installed" % lib
                )
