#!/usr/bin/python3
"""The Base class module"""
import json
import csv
import os


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

        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation `json_string`."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.m"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a file containing a JSON string \
            representation.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            json_string = file.read()

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

    classmethod

    def save_to_file_csv(cls, list_objs):
        """
        Serialize and save a list of objects to a CSV file.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                writer.writerow(["id", "width", "height", "x", "y"])
                for obj in list_objs:
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y]
                    )
            elif cls.__name__ == "Square":
                writer.writerow(["id", "size", "x", "y"])
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize and return a list of objects from a CSV file.
        """
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            list_of_dicts = []
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dict_row = {
                        "id": int(row["id"]),
                        "width": int(row["width"]),
                        "height": int(row["height"]),
                        "x": int(row["x"]),
                        "y": int(row["y"]),
                    }
                elif cls.__name__ == "Square":
                    dict_row = {
                        "id": int(row["id"]),
                        "size": int(row["size"]),
                        "x": int(row["x"]),
                        "y": int(row["y"]),
                    }
                list_of_dicts.append(dict_row)
            return [cls.create(**d) for d in list_of_dicts]
