

import compileall



import sys

import pathlib

compileall.compile_dir(pathlib.Path('.'), force=True)


print(sys.version)

x=input('terminar')
