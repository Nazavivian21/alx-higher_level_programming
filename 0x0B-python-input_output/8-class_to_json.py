#!/usr/bin/python3
"""The class_to_json method mosdule"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    """
    return obj.__dict__
