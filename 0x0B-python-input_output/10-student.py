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
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance."""
        if attrs:
            return {attr: getattr(self, attr) for attr in attrs}
        else:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age,
            }
