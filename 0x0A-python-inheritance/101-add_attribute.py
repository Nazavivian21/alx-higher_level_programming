#!/usr/bin/python3
"""add_attribute method module"""


def add_attribute(obj, attr_name, attr_value):
    """Adds attribute to an object"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
