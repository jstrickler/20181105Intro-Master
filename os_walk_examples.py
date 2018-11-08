#!/usr/bin/env python

import os


# os.walk() -> [(...), (...), (...), ...]

TARGET_DIR = "."

for curr_dir, folder_list, file_list in os.walk(TARGET_DIR):
    if 'git' in curr_dir:
        continue  # skip git folders
    print(curr_dir)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print("{:12d} {}".format(file_size, file_name))


