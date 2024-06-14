#!/usr/bin/python3
"""The load_from_json method module"""
import json


def load_from_json_file(filename):
    """Returns the Python object represented by the JSON data in a file."""
    with open(filename, 'r') as file:
        return json.load(file)
