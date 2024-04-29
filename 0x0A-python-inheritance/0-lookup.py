#!/usr/bin/python3
"""
Contains a function that returns a list of available attributes and methods of 
an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
            obj: The object whose attributes and methods are looked up.
    """
    return dir(obj)
