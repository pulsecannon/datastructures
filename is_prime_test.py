"""Defines unittests for prime number detection."""

import is_prime
import unittest
import time


class IsPrimeTest(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime.is_prime(17))

    def test_is_not_prime(self):
        self.assertFalse(is_prime.is_prime(9))

    def test_is_large_is_prime(self):
        st = time.time()
        self.assertTrue(is_prime.is_prime(87178291199))
        et = tiem.time()
        print(f'Took {et - st} time')


if __name__ == '__main__':
    unittest.main()
