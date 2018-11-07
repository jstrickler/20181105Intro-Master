#!/usr/bin/env python
import os

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

file_name = 'fruits.txt'

if os.path.exists(file_name):
    print("Sorry, file exists")
else:
    with open(file_name, 'w') as fruits_out:
        for fruit in fruits:
            fruits_out.write(fruit + '\n')


# with open('file1') as f1:
#     with open('file2') as f2:
#         ...
