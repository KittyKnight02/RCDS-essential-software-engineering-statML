import unittest
from add import add_fn

class test_add(unittest.TestCase):
    def test_negative_numbers(self):
        self.assertEqual(add_fn(-1, -1), -2)

    def test_positive_numbers(self):
        self.assertEqual(add_fn(1, 3), 4)

