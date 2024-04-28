#!/usr/bin/python3
class MyList(list):
	"""Inherits from class list."""
	def print_sorted(self):
		"""
		Prints a sorted list
		
		Returns:
			None
		"""
		sorted_list = sorted(self)
		print(sorted_list)