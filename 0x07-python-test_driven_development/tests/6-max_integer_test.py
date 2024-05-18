#!/usr/bin/python3
import sys
import os

# Add the src directory to the Python search path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
    
    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2, 0]), 4)
    
    def test_one_negative_number(self):
        self.assertEqual(max_integer([1, -2, 3, 4, 5]), 5)
    
    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
    
    def test_list_of_one_element(self):
        self.assertEqual(max_integer([10]), 10)
    
    def test_list_is_empty(self):
        self.assertIsNone(max_integer([]))
