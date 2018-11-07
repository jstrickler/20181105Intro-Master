#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

#   [EXPR for VAR in ITERABLE]
#   [EXPR for VAR in ITERABLE if CONDITION]

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2 = [f for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f.upper() for f in fruits if len(f) > 6]
print("f3:", f3, '\n')

raw_food = ['spam', 'spam', 'spam', 'spam', 'toast', 'spam', 'spam', 'spam', 'ham',
            'eggs', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs']

food = [f for f in raw_food if f != 'spam']
print("food:", food, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')




#

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [n * 100 for n in nums]
print("n1:", n1, '\n')

n2 = [float(n) for n in nums if n > 300]
print("n2:", n2, '\n')

n3 = [(i, i**2, i**3) for i in range(10)]
print("n3:", n3, '\n')

last_names_gen = (p[1] for p in people)
print(last_names_gen)

for last_name in last_names_gen:
    print(last_name)
print()
