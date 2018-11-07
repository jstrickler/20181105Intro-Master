#!/usr/bin/env python
from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)

print(knight_data['Robin'])
print(knight_data['Arthur'])
print(knight_data['Robin'][0])
print()

for knight, info in knight_data.items():
    print(info[0], knight, info[-1])


