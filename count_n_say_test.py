"""Unittests for count n say."""

import unittest
import count_n_say


class CountNSayTest(unittest.TestCase):

    def test_base(self):
        expected = '11'
        actual = count_n_say.count_n_say(2)
        self.assertEqual(actual, expected)

    def test_number(self):
        expected = '1211'
        actual = count_n_say.count_n_say(4)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
