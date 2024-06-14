#!/usr/bin/python3
"""The read_file method module"""


def read_file(filename=""):
    """Reads a textfile and prints to stdout:"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
