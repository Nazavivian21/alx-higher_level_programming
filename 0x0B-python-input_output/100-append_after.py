#!/usr/bin/python3
"""The append_after method module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a specific string"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        modified_lines.append(line)
        if search_string in line:
            modified_lines.append(new_string + '\n')

    with open(filename, 'w') as file:
        file.writelines(modified_lines)
