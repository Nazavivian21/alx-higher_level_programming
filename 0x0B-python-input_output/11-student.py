#!/usr/bin/python3
"""The student class method"""


class Student:
    """
    A class that defines a student by:

    Public instance attributes:
        - first_name
        - last_name
        - age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on \
              a dictionary representation.
        """
        for key, value in json.items():
            setattr(self, key, value)
