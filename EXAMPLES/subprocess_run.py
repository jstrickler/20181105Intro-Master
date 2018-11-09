#!/usr/bin/env python

import sys
from subprocess import run, CalledProcessError, PIPE
from glob import glob
import shlex

if sys.platform == 'win32':
    CMD = 'cmd /c dir'
    FILES = r'..\DATA\t*'
else:
    CMD = 'ls -ld'
    FILES = '../DATA/t*'

cmd_words = shlex.split(CMD)
cmd_files = glob(FILES)

full_cmd = cmd_words + cmd_files
print("Full command:", full_cmd)

try:
    proc = run(full_cmd)
    print(proc)
except CalledProcessError as err:
    print(proc.returncode)
    print(err)
print('-' * 60)

try:
    proc = run(full_cmd, stdout=PIPE, stderr=PIPE)
#    proc = run(full_cmd, capture_output=True)  >= 3.7 only
    print(proc)
    print(proc.stdout.decode()) # output of program
    print(proc.stderr.decode())
except CalledProcessError as err:
    print(proc.returncode)
    print(err)

