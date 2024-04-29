#!/usr/bin/python3
"""
Checks if the object is an instance of the class being inherited from.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of the class being inherited from.

    Args:
            obj: The object to be checked.
            a_class: The class to checked against.
    """
    return isinstance(obj, a_class)
