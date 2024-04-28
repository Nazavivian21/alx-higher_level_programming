#!/usr/bin/python3
class BaseGeometry:
	def area(self):
		raise Exception('area() is not implemented')
	def integer_validator(self, name, value):
		if not isinstance(value, int):
			raise TypeError('name must be an integer')
		if value <= 0:
			raise ValueError('name must be greater than 0')
class Rectangle(BaseGeometry):
	def __init__(self, width, height):
		self.__width = super().integer_validator('width', width)
		self.__height = super().integer_validator('height', height)