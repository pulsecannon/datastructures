"""Defines unittests for fibonacci numbers."""

import fibonacci
import unittest

class FibonacciTest(unittest.TestCase):

    def test_generate_resursive(self):
        actual = fibonacci.fibonacci_recursive(10)
        expected = 89
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
