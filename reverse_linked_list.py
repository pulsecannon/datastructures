"""Code to reverse a linked list."""


def reverse_linked_list(head):
    prev = None
    curr = head
    next_node = None
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
