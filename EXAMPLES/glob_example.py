#!/usr/bin/env python

from glob import glob

files = glob('../DATA/*.txt') # <1>
print(files)

print(glob('../DATA/alice.txt'))


print(glob('../DATA/wombat.*'))

cmd_line = 'ls -l foo bar "old stuff"'

cmd_words = cmd_line.split()
print(cmd_words)
