import os

from pydantic import BaseSettings

# Define
app_dir = os.path.dirname(os.path.dirname(__file__))
root_dir = app_dir + "/.."


class Secrets(BaseSettings):
    pass


class Constants:
    LIBC_PATH = "./libc"
    LIBC_NAME = "lib.json"
    LIBC_LIB = "lib"
    LIBC_SOURCE = "source"


secrets = (
    Secrets(_env_file=f"{root_dir}/env/dev.env")
    if os.path.isfile(f"{root_dir}/env/dev.env")
    else Secrets()
)
constants = Constants()
