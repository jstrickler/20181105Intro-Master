#!/usr/bin/env python
from pprint import pprint
from collections import namedtuple

Person = namedtuple('Person', 'first_name last_name product')

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

person_list = []

for first_name, last_name, product in people:
    p = Person(first_name, last_name, product)
    person_list.append(p)


for person in person_list:
    print(person.first_name, person.last_name)
print()

pprint(person_list)
