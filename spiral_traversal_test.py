"""Unittest for spiral traversal."""

import unittest
import spiral_traverse

class SpiralTraversalTest(unittest.TestCase):

    def test_square_matrix(self):
        matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(spiral_traverse.spiral_traversal(matrix), expected)

    def test_square_regtangular(self):
        matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(spiral_traverse.spiral_traversal(matrix), expected)

    def test_large(self):
        matrix = [[1,2,3,4,5,6,7],
                  [8,9,10,11,12,13,14],
                  [15,16,17,18,19,20,21],
                  [22,23,24,25,26,27,28],
                  [29,30,31,32,33,34,35]]
        expected = [1,2,3,4,5,6,7,14,21,28,35,34,33,32,31,30,
                    29,22,15,8,9,10,11,12,13,20,27,26,25,24,23,16,17,18,19]
        self.assertEqual(spiral_traverse.spiral_traversal(matrix), expected)


if __name__ == '__main__':
    unittest.main()
