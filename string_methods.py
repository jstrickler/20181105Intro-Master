#!/usr/bin/env python

actor = "Brad Pitt"

print(actor)

print(len(actor), type(actor))

a1 = actor.upper()
print(a1)

print(actor.upper())

print(actor.lower(), actor.title(), actor.capitalize())

print("this is a test".title())
print("this is a test".capitalize())

print(actor.split())

print(actor.count('t'))

cave_man = 'Barney Rubble'

print(cave_man.count('B'), cave_man.count('b'))

# print(actor.capitalize('x'))

print(cave_man.count('Rub'))
print(actor.count('rad'))
print(actor.count('cool'))

print(actor.startswith('B'))
print(actor.startswith('Bra'))
print(actor.startswith('Sock'))

print('rad' in actor)  # "in" means "contains"
print('ubb' in cave_man)
print('ubb' in actor)

print(actor.index('rad'))
print(actor.index('it'))

# print(actor.index('Angelina'))  ERROR!

song = "    All my exes live in Texas    "
print("|" + song.lstrip() + "|")
print("|" + song.rstrip() + "|")
print("|" + song.strip() + "|")
print()

song = "xyxxyyxxxyyyAll my exes live in Texasxyxyxyyyyxxxx"
print("|" + song.lstrip('xy') + "|")
print("|" + song.rstrip('xy') + "|")
print("|" + song.strip('xy') + "|")
print()

print(actor.split(), cave_man.split())

fruits = 'lemon;lime;orange;grapefruit'

print(fruits.split(';'))

print(fruits.replace(';', '/'))
print(fruits.replace(';', ' '))
print(fruits.replace(';', ''))

fruits = 'lemon,lime;orange;kiwi,grapefruit'

import re

print(re.split(r'[;,]', fruits))








