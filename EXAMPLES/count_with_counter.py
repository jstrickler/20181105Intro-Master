#!/usr/bin/env python

from collections import Counter

counts = Counter() # <1>

with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        item = line.rstrip('\n\r') # <2>
        counts[item] += 1  # <3>

for item, count in counts.items(): # <4>
    print(item, count)

print(counts.most_common())

with open("../DATA/words.txt") as words_in:
    first_letters = [word[0] for word in words_in]
    letter_counts = Counter(first_letters)

print(letter_counts.most_common())
print()

print(letter_counts.most_common(5))
