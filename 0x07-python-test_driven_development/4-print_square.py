#!/usr/bin/python3
"""This module prints a square with a specified size"""


def print_square(size):
    """This function prints a square with the character'#'"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
