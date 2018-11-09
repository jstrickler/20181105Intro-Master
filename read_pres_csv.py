#!/usr/bin/env python
import csv

with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    print(type(rdr))
    for row in rdr:
        print(row[1], row[2])
        # print(row)
print('-' * 60)

headings = 'term first_name last_name birth_place birth_state party'.split()

with open('DATA/presidents.csv') as pres_in:
    rdr = csv.DictReader(pres_in, fieldnames=headings)
    for row in rdr:
        print(row['first_name'], row['last_name'])
print('-' * 60)

with open('DATA/airport_boardings.csv') as ab_in:
    rdr = csv.DictReader(ab_in)
    for row in rdr:
        print(row['Code'], row['2010 Rank'])
