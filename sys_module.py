#!/usr/bin/env python
import sys

print(sys.prefix)
print(sys.executable)

print(sys.version, '\n')
print(sys.version_info, '\n')
print(sys.version_info.major, '\n')

for path in sys.path:  # current + PYTHONPATH + std locations
    print(path)
print('-' * 60)

print(sys.platform)  # where am I?

print(sys.modules.keys(), '\n')


