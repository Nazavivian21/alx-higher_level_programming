#!/usr/bin/python3
"""The Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class that is inheriting from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square class instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width 

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
