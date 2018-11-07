#!/usr/bin/env python

for i in range(10):
    print("Hello, Python world")
print()

# range(STOP)   range(START, STOP)    range(START, STOP, STEP)

for i in range(1, 11):
    print(i)
print()

r = range(1000000)

print(r)

colors = ['red', 'purple', 'pink']
numbers = [5, 10, 15]

e = enumerate(colors)

print(e)

z = zip(colors, numbers)

print(z)

# enumerate, zip, and range are GENERATORS!!!!

