#!/usr/bin/python3
import sys
import os

# Add the src directory to the Python search path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function"""

    def test_empty_list(self):
        """Test case for an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test case for a list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements_list(self):
        """Test case for a list with multiple elements"""
        self.assertEqual(max_integer([3, 7, 2, 9, 1]), 9)

    def test_negative_numbers(self):
        """Test case for a list with negative numbers"""
        self.assertEqual(max_integer([-5, -10, -3]), -3)

    def test_mixed_numbers(self):
        """Test case for a list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([2, -4, 6, -1, 8]), 8)

    def test_max_at_end(self):
        """Test case for a list with max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_max_in_middle(self):
        """Test case for a list with max in the middle"""
        self.assertEqual(max_integer([1, 9, 3, 2]), 9)

    def test_one_negative_number(self):
        """Test case for a list with one negative number"""
        self.assertEqual(max_integer([5, -10]), 5)

    def test_only_negative_numbers(self):
        """Test case for a list with only negative numbers"""
        self.assertEqual(max_integer([-5, -10, -3]), -3)