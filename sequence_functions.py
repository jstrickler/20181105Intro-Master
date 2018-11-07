#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(len(fruits), min(fruits), max(fruits))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(nums), min(nums), max(nums), sum(nums))

print(sorted(fruits))
print(sorted(nums))

stuff = ['a', 5, 4.6, None, True, '88']

print(list(reversed(nums)))

colors = ['red', 'purple', 'pink']
numbers = [5, 10, 15]

print(list(zip(colors, numbers)), '\n')

for color in colors:
    print(color)
print()

for i, color in enumerate(colors):
    print(i, color)
print()

print(list(enumerate(colors)), '\n')

more_colors = ['brown', 'grey', 'white']

c = colors + more_colors

print(c)

print("foo" + "bar")

print('-' * 60)

print("PYTHON " * 10)


flags = [True] * 10
print(flags)

junk = ['a', 'b', 'c'] * 5
print(junk)

data = [None] * 25
print(data)

print('red' in colors)
print('orange' in colors)

