#!/usr/bin/python3
"""The read_file method module"""


def append_write(filename="", text=""):
    """Reads a textfile and prints to stdout:"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
