"""Unittest for permutations."""

import unittest

import permutations


class PermutationsTest(unittest.TestCase):

    def test_example(self):
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        actual = permutations.permutation([1, 2, 3])
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
