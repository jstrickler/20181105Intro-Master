#!/usr/bin/env python

john_countries = """Canada Mexico Barbados China UK Austria Spain Bulgaria Israel""".split()

clare_countries = """BVI Denmark UK Spain Kenya Mexico Barbados Norway Sweden Canada""".split()


print(john_countries)
print(clare_countries)
print()

john = set(john_countries)
clare = set(clare_countries)

print('Both:', john & clare)  # intersection
print('Just one:', john ^ clare)  # XOR

print("Either:", john | clare) # union

print("Just Clare:", clare - john)
print("Just John:", john - clare)

food = ['spam', 'spam', 'spam', 'spam', 'toast', 'toast', 'toast', 'spam', 'spam', 'spam', 'ham',
            'eggs', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs']

unique_food = set(food) - {'spam'}
print(unique_food)
