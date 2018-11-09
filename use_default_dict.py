#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fruit_lists = defaultdict(list)

for fruit in fruits:
    fruit_lists[fruit[0]].append(fruit)

pprint(fruit_lists)

def not_found():
    return "NOT FOUND"

capitals_by_state = defaultdict(not_found)
capitals_by_state['FL'] = 'Tallahassee'
capitals_by_state['VA'] = 'Richmond'
capitals_by_state['MA'] = 'Boston'
capitals_by_state['CO'] = 'Denver'


states = ['FL', 'MA', 'CO', 'NC', 'VA', 'IL', 'CA']


for state in states:
    print(capitals_by_state[state])


#  lambda P1, P2, ...: VALUE
#  lambda: VALUE

magic = defaultdict(lambda: 0)


print(magic['hello'])
print(magic[5])
print(magic["this is weird"])






