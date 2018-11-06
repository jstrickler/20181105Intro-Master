#!/usr/bin/env python

list1 = list()   # new, empty, list
list2 = ['red', 'blue', 'green']  # literal list
list3 = []  # empty literal list

#  a list is an *iterable*
list4 = 'red blue green'.split()  # another way to get a list

colors = ['red', 'blue', 'purple']

colors.append('pink')

print(colors)

colors.append('green')

print(colors)

colors.insert(0, 'brown')
print(colors)
colors.insert(3, 'white')
print(colors)

print(sorted(colors))
sorted_colors = sorted(colors)
print(sorted_colors)

print(colors[3])

del colors[3]  # remove variable or element

print(colors)

colors.remove('red')

print(colors)

c = colors.pop()
print(c)
print(colors)

c = colors.pop(2)
print(c)
print(colors)

more_colors = ['taupe', 'navy', 'chartreuse']

colors.extend(more_colors)

print(colors, '\n')

# colors.append(more_colors)

# print(colors)

for color in colors:
    # color = get next item from colors
    print(color)
print()

actor = 'Brad Pitt'

for character in actor:
    print(character)
print()

