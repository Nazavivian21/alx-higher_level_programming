#!/usr/bin/python3
"""The append_after method module"""


def append_after(filename, search_string, new_string):
    """Inserts a line of text to a file, after each line containing a specific string"""
    with open(filename, "r") as file_read:
        lines = file_read.readlines()

    with open(filename, "w") as file_write:
        for line in lines:
            if search_string in line:
                file_write.write(line.strip() + "\n" + new_string + "\n")
            else:
                file_write.write(line)
