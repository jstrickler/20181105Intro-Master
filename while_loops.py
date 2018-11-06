#!/usr/bin/env python

# while COND:
#     .....
#

while True:
    name = input("What is your name? ")
    if name == 'q':
        break
    if name == '':
        continue
    print("OK, {}".format(name))

# don't do this:
i = 0
while i < 5:
    print("Oof!")
    i += 1
print()
