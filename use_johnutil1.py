#!/usr/bin/env python
import sys
# from folder/folder import file

# from package.package import module
from barfco.it import johnutil
import barfco

print(barfco.ice_cream)
# look for modules in
#  current folder + PYTHONPATH folders + builtin folders

# set PYTHONPATH="c:\foo\bar;D:\python\stuff"

# import  mystuff.johnutil

johnutil.spam()
johnutil.ham()

print(johnutil.ACTOR)
print()

for path in sys.path:
    print(path)

