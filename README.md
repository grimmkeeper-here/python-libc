# python-libc
This is app template for install libc

## Prerequisites
- OS: Ubuntu v21.04 or later
- Runtime environment: Python version 3.9.x
- Package manager: APT (Ubuntu)

## Setup project
``` bash
sudo apt-get install build-essential

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt --trusted-host pypi.python.org
```

## Setup dev enviroment
- Make _env_ folder
- Add secrets key to _env/dev.env_
- Secrets key can find at _app/core/config.py_

## Format before git
- Auto autoflake,isort then black all .py file in git status
``` bash
./scripts/format.sh
```

## Add new libc for implement to Python
- Add new C file to _app/libc/source/_
``` C
    // square.c
    
    #include <stdio.h>
    int square(int i) {
        return i * i;
    }
```
- Add Lib info to _app/libc/lib.json_
``` json
[
  {
     "name":"square libc",
     "_file":"square",
     "description":"This is test libc with square function"
  }
]
```
- Install libc(or build .so file from .c file), run command:
``` bash
./scripts/install_libc.sh
```
- List all libc is installed
``` bash
python manage.py libc list
```
```
#######################################################
name: square libc
_file: square
install: from libc import square
description: This is test libc with square function
#######################################################
```
- Use libc with _install_
``` python
from libc import square as square_lib
square_lib.square(10) #100
```

