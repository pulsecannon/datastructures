"""Unittest for reverse linked list."""

import unittest

import reverse_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReverseLinkedListTest(unittest.TestCase):

    def to_list(self, head):
        output = []
        while head is not None:
            output.append(head.val)
            head = head.next
        return output

    def test_one_element(self):
        head = ListNode(1)
        expected = [1]
        self.assertEqual(self.to_list(reverse_linked_list(head)), expected)

    def test_one_element(self):
        head = ListNode(1)
        node = head
        expected = [1]
        for i in range(2, 10):
            node.next = ListNode(i)
            node = node.next
            expected.insert(0, i)
        self.assertEqual(self.to_list(reverse_linked_list.reverse_linked_list(
            head)), expected)


if __name__ == '__main__':
    unittest.main()
