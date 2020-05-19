"""Tests the bst."""

import unittest
import bst


class BSTTest(unittest.TestCase):

    def test_add(self):
        head = bst.Node(10)
        head.add(11)
        head.add(9)
        self.assertEqual(head.value, 10)
        self.assertEqual(head._left.value, 9)
        self.assertEqual(head._right.value, 11)

    def test_in(self):
        head = bst.Node(10)
        head.add(11)
        head.add(9)

        self.assertTrue(10 in head)
        self.assertFalse(13 in head)

    def test_traverse_inorder(self):
        head = bst.Node(10)
        head.add(11)
        head.add(9)
        head.add(13)
        head.add(14)
        head.add(18)

        out = []
        head.traverse_inorder(out.append)
        self.assertEqual(out, [9, 10, 11, 13, 14, 18])

    def test_traverse_preorder(self):
        head = bst.Node(10)
        head.add(11)
        head.add(9)
        head.add(13)
        head.add(14)
        head.add(18)

        out = []
        head.traverse_preorder(out.append)
        self.assertEqual(out, [10, 9, 11, 13, 14, 18])

    def test_traverse_postorder(self):
        head = bst.Node(10)
        head.add(11)
        head.add(9)
        head.add(13)
        head.add(14)
        head.add(18)

        out = []
        head.traverse_postorder(out.append)
        self.assertEqual(out, [9, 18, 14, 13, 11, 10])

    def test_height(self):
        head = bst.Node(10)
        head.add(11)
        head.add(9)
        head.add(13)
        head.add(14)
        head.add(18)

        self.assertEqual(head.get_height(), 5)

    def test_is_balanced(self):
        head = bst.Node(10)
        head.add(11)
        head.add(9)
        head.add(13)
        head.add(14)
        head.add(18)
        self.assertFalse(head.is_balanced)

    def test_rebalanced(self):
        head = bst.Node(10)
        head.add(11)
        head.add(9)
        head.add(13)
        head.add(14)
        head.add(18)
        self.assertFalse(head.is_balanced)
        print(head.get_height())
        head = head.rebalance()
        self.assertTrue(head.is_balanced)
        print(head.get_height())


if __name__ == '__main__':
    unittest.main()
