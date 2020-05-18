"""Defines the linked list datastructure."""


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self):
        self._head = None
        self._length = 0

    def insert(self, index, value):
        if self._head is None:
            raise IndexError
        curr = self._head
        curr_idx = 1
        while (curr.next is not None and curr_idx < index):
            curr = curr.next
            curr_idx += 1
        if curr_idx == index:
            new_node = Node(value)
            new_node.next = curr.next
            curr.next = new_node
            self._length += 1
        else:
            raise IndexError

    def remove(self, index):
        if self._head is None:
            raise IndexError
        curr = self._head
        curr_idx = 1
        while (curr.next is not None and curr_idx < index - 1):
            curr = curr.next
            curr_idx += 1
        if curr_idx == index - 1:
            remove_node = curr.next
            curr.next = remove_node.next
            value = remove_node.value
            remove_node.next = remove_node = None
            self._length -= 1
            return value
        else:
            raise IndexError

    def add(self, value):
        if self._head is None:
            new_node = Node(value)
            self._head = new_node
            self._length = 1
            return
        curr = self._head
        while (curr.next is not None):
            curr = curr.next
        new_node = Node(value)
        curr.next = new_node
        self._length += 1

    def pop(self):
        if self._head is None:
            raise IndexError
        prev = None
        curr = self._head
        while (curr.next is not None):
            prev = curr
            curr = curr.next
        value = curr.value
        if prev is not None:
            prev.next = curr = None
        else:
            self._head = None
        self._length -= 1
        return value

    def print_state(self):
        curr = self._head
        out = 'h'
        while (curr is not None):
            out += ' -> ' + str(curr.value)
            curr = curr.next
        print(out)

    def find(self, value):
        found = -1
        curr = self._head
        idx = 0
        while (curr is not None):
            if curr.value == value:
                found = idx
                break
            curr = curr.next
            idx += 1
        return found

    def __contains__(self, value):
        return self.find(value) != -1
        

    def __len__(self):
        return self._length


