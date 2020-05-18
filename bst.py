"""Defines a binary search tree."""


class Node(object):

    def __init__(self, value):
        self._left = self._right = None
        self.value = value

    def add(self, value):
        if value <= self.value:
            if self._left is None:
                self._left = Node(value)
            else:
                self._left.add(value)
        else:
            if self._right is None:
                self._right = Node(value)
            else:
                self._right.add(value)

    def __contains__(self, value):
        if self.value == value:
            return True
        elif self.value < value:
            if self._left is not None:
                return value in self._left
            else:
                return False
        else:
            if self._right is not None:
                return value in self._right
            else:
                return False

    def traverse_inorder(self, callback_fn):
        if self._left is not None:
            self._left.traverse_inorder(callback_fn)
        callback_fn(self.value)
        if self._right is not None:
            self._right.traverse_inorder(callback_fn)

    def traverse_preorder(self, callback_fn):
        callback_fn(self.value)
        if self._left is not None:
            self._left.traverse_preorder(callback_fn)
        if self._right is not None:
            self._right.traverse_preorder(callback_fn)

    def traverse_postorder(self, callback_fn):
        if self._left is not None:
            self._left.traverse_postorder(callback_fn)
        if self._right is not None:
            self._right.traverse_postorder(callback_fn)
        callback_fn(self.value)

    def height(self):
        if self._right is None or self._right is None:
            return 1
        elif self._right is not None:
            return 1 + self._right.height()
        elif self._left is not None:
            return 1 + self._left.height()
        else:
            return 1 + max(self._left.height(), self._right.height())

    def is_balanced(self):
        return abs(self._left.height() - self._right.height()) <= 1
