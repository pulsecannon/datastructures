"""Unittests for find all duplicates."""

import unittest

import find_all_duplicates


class FindAllDuplicatesTest(unittest.TestCase):
    """Unittests for find all duplicates."""

    def test_success(self):
        """Tests success case."""
        numbers = [4, 3, 2, 7, 8, 2, 3, 1]
        expected = [2, 3]
        actual = find_all_duplicates.find_all_duplicates(numbers)
        self.assertEqual(actual, expected)

    def test_fail(self):
        """Fails to find duplicates."""
        numbers = [1, 2, 3, 4, 5, 6, 7]
        expected = []
        actual = find_all_duplicates.find_all_duplicates(numbers)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
