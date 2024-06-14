#!/usr/bin/python3
"""The read_file method module"""


def write_file(filename="", text=""):
    """Reads a textfile and prints to stdout:"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)