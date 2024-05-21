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
        """Test with max integer at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Test with max integer in the middle"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_all_equal_numbers(self):
        """Test with all numbers being equal"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats_and_integers(self):
        """Test with a mix of floats and integers"""
        self.assertEqual(max_integer([1.5, 2.5, 3, 4.5]), 4.5)

    def test_unsorted_list(self):
        """Test with an unsorted list"""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max integer at the beginning"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
