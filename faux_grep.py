#!/usr/bin/env python
import fileinput
import re
import argparse
from glob import glob

#  sys.argv
#     0           1      2      3
#  faux_grep.py PATTERN file1 file2 ....

# python faux_grep.py -i -n pattern files ...

arg_parser = argparse.ArgumentParser(description="Print lines matching RE")

arg_parser.add_argument('-i', dest="ignore_case", action="store_true", help="Ignore case")
arg_parser.add_argument('-n', dest="show_names", action="store_true", help="Print file names")
arg_parser.add_argument('pattern', help="Pattern to find")
arg_parser.add_argument('files', nargs='*', help="Files to search (if no files, read STDIN)")

args = arg_parser.parse_args()  # defaults to sys.argv

pattern = re.compile(args.pattern, re.I if args.ignore_case else 0)

file_list = []
for file_spec in args.files:
    file_list.extend(glob(file_spec))

for raw_line in fileinput.input(file_list):
    line = raw_line.rstrip()
    if pattern.search(line):
        if args.show_names:
            print(fileinput.filename(), end=' ')
        print(line)


