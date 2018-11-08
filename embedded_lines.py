#!/usr/bin/env python
import re

with open("DATA/mary.txt") as mary_in:
    for line in mary_in:
        line = line.rstrip()
        print(line)
print()


with open("DATA/mary.txt") as mary_in:
    contents = mary_in.read()
    print(repr(contents))
print()

m = re.search('l..b', contents)
if m:
    print(m.group())
