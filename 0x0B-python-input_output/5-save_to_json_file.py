#!/usr/bin/python3
"""The save_to_json_file method module """
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using its JSON representation."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
