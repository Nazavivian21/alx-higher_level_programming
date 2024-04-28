#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
            obj: The object whose attributes and methods are looked up.
    """
    return dir(obj)
