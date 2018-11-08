#!/usr/bin/env python
import subprocess
import os

result = os.system("netstat -an")
print(result)
print('-' * 60)

with os.popen("netstat -an") as netstat_in:
    for line in netstat_in:
        if 'ESTAB' in line:
            print(line.rstrip())

with os.popen("netstat -an") as netstat_in:
    all_output = netstat_in.read()
