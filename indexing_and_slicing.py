#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0], fruits[5])
print(len(fruits))
print(fruits[21])
print(fruits[len(fruits) - 1])
print(fruits[-1])
print(fruits[-2], fruits[-3])

#   I[START:STOP]   I[:STOP]   I[START:]
#   I[START:STOP:STEP]

print(fruits[0:3])  # first 3 fruits (fruits[0] through fruits[2])
print(fruits[9:13], '\n')

print(fruits, '\n')

fruits[9:13] = []

print(fruits, '\n')

fruits[4:6] = ['grapefruit', 'durian', 'marionberry']

print(fruits, '\n')

print(fruits[0:10:2], '\n')

actor = 'Brad Pitt'

print(actor[1:4], actor[5:8])



