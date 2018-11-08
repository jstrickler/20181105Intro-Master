#!/usr/bin/env python
from datetime import datetime
import os  # includes os.path

FOLDER = 'DATA'
FILE = 'mary.txt'

file_path = os.path.join(FOLDER, FILE)
print("file path:", file_path)

file_size = os.path.getsize(file_path)
print("file size:", file_size)

print(os.path.exists(file_path))
print(os.path.exists('rutabaga.txt'))

print(os.path.dirname(file_path))
print(os.path.basename(file_path))
print(os.path.abspath(file_path))

raw_timestamp = os.path.getmtime(file_path)
print(raw_timestamp)
timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)
print()

for entry in os.scandir("."):
        print("{:22s} {:40s} {}".format(entry.name, entry.path, entry.is_dir()))


