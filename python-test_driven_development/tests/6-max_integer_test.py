#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_positive_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_int(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_negandpos_int(self):
        self.assertEqual(max_integer([1, -1, 2, -2]), 2)

    def test_one_int(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_same(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

if __name__ == "__main__":
    unittest.main()
