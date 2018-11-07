#!/usr/bin/env python

words = []

with open('DATA/words.txt') as words_in:
    for raw_line in words_in:
        if "vote" in raw_line:
            words.append(raw_line.rstrip())

print(words)
