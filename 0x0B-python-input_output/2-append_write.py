#!/usr/bin/python3
"""The append_write method module"""


def append_write(filename="", text=""):
    """Appends to a textfile"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
