#!/usr/bin/env python


person = 'Bill', 'Gates', 'Microsoft'

print(person[0])
print(len(person))
print(person[:2])

first_name, last_name, product = person   # unpack tuple into variables

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


