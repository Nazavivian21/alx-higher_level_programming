#!/usr/bin/python3
"""The write_file method module"""


def write_file(filename="", text=""):
    """Writes a textfile and prints to stdout:"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
