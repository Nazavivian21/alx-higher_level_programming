#!/usr/bin/python3
"""Square class definition module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from the Rectangle class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation of the square class"""
        return f"[Square] {self.__size}/{self.__size}"
