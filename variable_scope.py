#!/usr/bin/env python

x = 100  # global variable

if x:
    y = 10

def spam():
    actor = 'Brad Pitt' # local variable
    print("In spam(): x is", x)
    return actor


result = spam()
print("In main: actor is", result)
print("In main: x is", x)



