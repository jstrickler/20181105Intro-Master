#!/usr/bin/env python

import re
pattern=r'\b\d{1,3}\b'
pattern2=r'\bNote: their interbank*.*'
f=open('DATA/custinfo.dat')
#for items in f:
##    t=re.search(pattern,items)
#    print(t)
for items in f:
    items = items.rstrip()
    print("items:", items)
    m = re.search(pattern2,items)
    if m:
        print('FOUND:', m.group())
    else:
        m = re.match(r'\d\d\d',items)
        if m:
            print("Matched 3 digits:", m.group())
