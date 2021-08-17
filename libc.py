import json
import os.path
from ctypes import CDLL

from app.core.config import constants

installed_libs = []
with open(f"{constants.LIBC_PATH}/{constants.LIBC_NAME}") as fi:
    libs = json.loads(fi.read())
    for lib in libs:
        if (
            os.path.isfile(
                f"{constants.LIBC_PATH}/{constants.LIBC_LIB}/%(_file)s.so" % lib
            )
            and "_file" in lib
        ):
            globals()[lib["_file"]] = CDLL(
                f"{constants.LIBC_PATH}/{constants.LIBC_LIB}/%(_file)s.so" % lib
            )
            installed_libs.append(lib)

if __name__ == "__main__":
    if installed_libs:
        print(f"#######################################################")
    for lib in installed_libs:
        print(
            f"name: %(name)s\n_file: %(_file)s\ninstall: from libc import %(_file)s\ndescription: %(description)s"
            % lib
        )
        print(f"#######################################################")
