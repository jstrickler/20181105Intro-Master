#!/usr/bin/env python

from zipfile import ZipFile

zip = ZipFile('DATA/textfiles.zip')

print(zip.namelist())

tyger = zip.read('tyger.txt').decode()
print(tyger, '\n')

zip.extract('parrot.txt')

