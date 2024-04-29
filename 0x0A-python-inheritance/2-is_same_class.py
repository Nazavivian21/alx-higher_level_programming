#!/usr/bin/python3
"""
Returns True if the object is an instance of the specified class, otherwise 
False.
"""
def is_same_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class, otherwise 
    False.

    Args:
            obj: The object to check.
            a_class: The class to be checked against.
    """
    return type(obj) is a_class
