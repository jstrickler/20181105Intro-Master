#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    limit = int(sys.argv[1])  #  ['sieve.py', 100]
else:
    limit = 100


flags = [True] * (limit + 1)

for i in range(2, limit + 1):
    if flags[i]:
        print(i, end=',')
        for j in range(i * 2, limit + 1, i):
            flags[j] = False
print()
