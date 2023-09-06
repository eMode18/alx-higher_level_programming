#!/usr/bin/python3

"""Unit Tests for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unit tests for max_integer([..])."""

    def test_ordered_positive_integers(self):
        """Check an ordered list of positive integers."""
        ordered_positives = [10, 20, 30, 40]
        self.assertEqual(max_integer(ordered_positives), 40)

    def test_unordered_positive_integers(self):
        """Evaluate an unordered list of positive integers."""
        unordered_positives = [40, 20, 60, 30]
        self.assertEqual(max_integer(unordered_positives), 60)

    def test_max_at_beginning(self):
        """Test a list with the maximum value at the start."""
        max_at_beginning = [99, 88, 77, 66]
        self.assertEqual(max_integer(max_at_beginning), 99)

    def test_empty_list(self):
        """Examine an empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_single_element_list(self):
        """Assess a list with a single element."""
        single_element = [42]
        self.assertEqual(max_integer(single_element), 42)

    def test_mixed_numbers(self):
        """Inspect a list of mixed numbers (integers and floats)."""
        mixed_numbers = [1.5, 3, 2, 4.8, 2.5]
        self.assertEqual(max_integer(mixed_numbers), 4.8)

    def test_string_characters(self):
        """Find the maximum character in a string."""
        string = "example"
        self.assertEqual(max_integer(string), 'x')

    def test_strings(self):
        """Find the maximum string in a list of strings."""
        string_list = ["apple", "banana", "cherry", "date"]
        self.assertEqual(max_integer(string_list), "date")

    def test_empty_string(self):
        """Evaluate an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
