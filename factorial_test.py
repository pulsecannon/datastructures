"""Defines unittest for factorial number generation."""

import factorial
import unittest


class FactorialTest(unittest.TestCase):

    def test_factorial(self):
        actual = factorial.factorial(10)
        expected = 3628800
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
