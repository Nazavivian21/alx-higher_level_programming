#!/usr/bin/python3
"""
This module contains a function that takes a text string and
inserts two new lines after each occurrence of the characters '.', '?',
and ':'. Without any trailing white space.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    i = 0
    length = len(text)

    while i < length:
        print(text[i], end="")
        if text[i] in chars:
            print("\n\n", end="")
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
