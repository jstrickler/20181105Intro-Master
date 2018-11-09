#!/usr/bin/env python

import sys
import os

if len(sys.argv) < 2:
    sys.stderr.write('Please specify a starting directory\n')
    sys.exit(1)

start_dir = sys.argv[1]

for base_name in os.listdir(start_dir): # <1>
    file_name = os.path.join(start_dir,base_name)
    print(file_name, end=' ')
    if os.access(file_name, os.R_OK | os.W_OK):  # <2>
        print("is writable", end=' ')
    else:
        print("is NOT writable", end = ' ')
    print(bin(os.stat(file_name).st_mode))



