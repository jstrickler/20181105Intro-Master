#!/usr/bin/env python


#  ../../foo.txt
# mary_in = open('/Users/jstrick/Desktop/py3master/DATA/mary.txt')  #   DATA/mary

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip('\r\n')
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print(contents)
    print(len(contents))
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
    print(len(all_lines))
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines = [line.rstrip() for line in mary_in]
    print(all_lines)
    print(len(all_lines))
print('-' * 60)




