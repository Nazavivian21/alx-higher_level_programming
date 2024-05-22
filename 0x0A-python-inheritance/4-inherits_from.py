#!/usr/bin/python3
"""This module returns True if an object is a sub class"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited \
    (directly or indirectly) from the specified class.

    Args:
    obj: The object to check.
    a_class: The class to check against.

    Returns:
    True if the object is an instance of a subclass \
          of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
