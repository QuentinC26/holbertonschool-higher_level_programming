#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_max_integer_at_the_beginning(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
    def test_max_integer_in_the_middle(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
    def test_one_value_negative(self):
        list = [4, 2, 3, 4, -5]
    def test_only_value_negative(self):
        list = [-4, -2, -3, -4, -5]
    def test_list_one_element(self):
        list = [4]
    def test_list_empty(self):
        list = []

if __name__ == '__main__':
    unittest.main()
