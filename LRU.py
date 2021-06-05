# Design/implement LRU cache
# Test
#
# key(int)->val(int)
# capacity
#
# get -> O(1)
# put -> O(1)
#


# put(1)
# put(2)
# put(3)
# put(4)
# get(3)
# get(1) [4, 3, 2, 1]
# put(5)
# put(7)

# Rearrange -> DLinkedList O(1)


DB = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66, 7: 77}


class LRUDoubleLinkedNode:

    def __init__(self, value: int, key: int):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None


class LRU:

    def __init__(self, size: int):
        self._size = size
        self._cache = dict()
        self._head = None
        self._tail = None

    @property
    def is_full(self) -> bool:
        return len(self._cache) == self._size

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def _add_node(self, key: int, value: int) -> LRUDoubleLinkedNode:
        node = LRUDoubleLinkedNode(value, key)
        node.next = self._head

        # There are already nodes in the DLL.
        if self._head is not None:
            self._head.prev = node

        # If this is first node then head will point to first node.
        self._head = node

        # Check if this is the first node.
        if self._tail is None:
            self._tail = node

        self._cache[node.key] = node
        return node

    def _discard_tail(self):
        old_tail = self._tail
        self._tail = old_tail.prev
        self._tail.next = None

        # Sever the old tail node from new tail.
        old_tail.prev = None

        # Remove it from cache.
        self._cache.pop(old_tail.key)

    def _move_to_front(self, node):
        # Node is the head node, head is already at the front nothing to do.
        if node is self._head:
            return

        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node

        # If the node being moved is the tail node then moved the tail pointer
        # to prev node of the tail.
        if node is self._tail:
            self._tail = prev_node
        else:
            next_node.prev = prev_node

        node.next = self._head
        self._head.prev = node
        self._head = node

    def get(self, key: int) -> int:
        node = self._cache.get(key)

        if node is None:
            # Node is not there in the cache, get it from DB.
            value = self.get_from_db(key)

            # This is a new node, check if we have reached full capacity,
            # if yes first discard to make space then add new element.
            if self.is_full:
                self._discard_tail()
            node = self._add_node(key, value)
        else:
            # Move the node to front.
            self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int):
        node = self._cache.get(key)
        if node is None:
            # This is a new node, check if we have reached full capacity,
            # if yes first discard to make space then add new element.
            if self.is_full:
                self._discard_tail()
            self._add_node(key, value)
        else:
            # We have node already but the value different.
            if node.value != value:
                node.value = value
            # We made an operation on this node, need to move to the front of DLL.
            self._move_to_front(node)

    def get_from_db(self, key):
        return DB.get(key)


def test_lur_cache():
    lru_cache = LRU(5)

    # Init the cache and fill it to capacity.
    lru_cache.put(1, 11)
    lru_cache.put(2, 22)
    lru_cache.put(3, 33)
    lru_cache.put(4, 44)
    lru_cache.put(5, 55)

    # 1 is the tail, lets move 1 to head.
    # Tail should be Key 2 value 22.
    assert lru_cache.get(1) == 11
    assert lru_cache.head.key == 1
    assert lru_cache.head.value == 11
    assert lru_cache.tail.key == 2
    assert lru_cache.tail.value == 22

    # Get from DB, should discard tail (Key: 2, value: 22) because capacity is full.
    # Head should be Key: 6 Value: 66
    assert lru_cache.get(6) == 66
    assert lru_cache.head.key == 6
    assert lru_cache.head.value == 66
    assert lru_cache.tail.key == 3
    assert lru_cache.tail.value == 33

    # Get head, should not modify the DLL.
    assert lru_cache.get(6) == 66
    assert lru_cache.head.key == 6
    assert lru_cache.head.value == 66
    assert lru_cache.tail.key == 3
    assert lru_cache.tail.value == 33

    # Get mid element, should move (Key: 4, value: 44) to head.
    assert lru_cache.get(4) == 44
    assert lru_cache.head.key == 4
    assert lru_cache.head.value == 44
    assert lru_cache.tail.key == 3
    assert lru_cache.tail.value == 33

    # Try to put more than capacity, should discard tail, tail should be Key: 5, value: 55.
    # Head should be key: 9, value: 99
    lru_cache.put(9, 99)
    assert lru_cache.head.key == 9
    assert lru_cache.head.value == 99
    assert lru_cache.tail.key == 5
    assert lru_cache.tail.value == 55

    # Try to update the value of Key: 4 to value: 104
    lru_cache.put(4, 104)
    assert lru_cache.head.key == 4
    assert lru_cache.head.value == 104
    assert lru_cache.tail.key == 5
    assert lru_cache.tail.value == 55

    print('All tests passed successfully.')


test_lur_cache()
