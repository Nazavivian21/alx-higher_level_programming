#!/usr/bin/python3
"""The Base class module"""
import json


class Base:
    """The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.
        """

        filename = f"{cls.__name__}.json"
        list_dicts = (
            [obj.to_dictionary() for obj in list_objs] if list_objs else []
        )
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_string)
