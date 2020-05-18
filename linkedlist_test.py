"""Unittest for linkedlist."""

import unittest
import linkedlist


class LinkedListTest(unittest.TestCase):

    def test_add(self):
        ll = linkedlist.LinkedList()
        for i in range(10):
            ll.add(i)
        self.assertEqual(len(ll), 10)

    def test_pop(self):
        ll = linkedlist.LinkedList()
        original_len = 10
        for i in range(original_len):
            ll.add(i)

        for i in range(5):
            value = ll.pop()
            self.assertEqual(value, ((original_len - 1) - i))
        self.assertEqual(len(ll), 5)

    def test_insert(self):
        ll = linkedlist.LinkedList()
        original_len = 10
        for i in range(original_len):
            ll.add(i)

        ll.insert(3, 33)
        self.assertEqual(len(ll), 11)
        self.assertTrue(33 in ll)

    def test_remove(self):
        ll = linkedlist.LinkedList()
        original_len = 10
        for i in range(original_len):
            ll.add(i)

        ll.remove(3)
        self.assertEqual(len(ll), 9)
        self.assertFalse(2 in ll)

    def test_find(self):
        ll = linkedlist.LinkedList()
        original_len = 10
        for i in range(original_len):
            ll.add(i)

        self.assertEqual(ll.find(2), 2)


if __name__ == '__main__':
    unittest.main()
