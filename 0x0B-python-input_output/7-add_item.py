#!/usr/bin/python3
"""This module loads, adds and saves arguments into  a file"""

import sys
import os
from pathlib import Path


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to be serialized and written to the file.
        filename (str): The name of the file to which the JSON representation
                        of the object should be written.

    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file to read the JSON data from.

    Returns:
        The Python object represented by the JSON data in the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)


if __name__ == "__main__":
    import json

    filename = "add_item.json"
    items = []

    # Load existing items if the file exists
    if Path(filename).exists():
        items = load_from_json_file(filename)

    # Add new arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, filename)
