# Written by Eric Martin for COMP9021


'''
A Doubly Linked List abstract data type
'''


from copy import deepcopy


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    def __init__(self, L = None, key = lambda x: x):
        '''Creates an empty list or a list built from a subscriptable object,
        the key of each value being by default the value itself.

        >>> DoublyLinkedList().print_from_head_to_tail()
        >>> DoublyLinkedList().print_from_tail_to_head()
        >>> DoublyLinkedList([]).print_from_head_to_tail()
        >>> DoublyLinkedList([]).print_from_tail_to_head()
        >>> DoublyLinkedList((0,)).print_from_head_to_tail()
        0
        >>> DoublyLinkedList((0,)).print_from_tail_to_head()
        0
        >>> DoublyLinkedList(range(4)).print_from_head_to_tail()
        0, 1, 2, 3
        >>> DoublyLinkedList(range(4)).print_from_tail_to_head()
        3, 2, 1, 0
        '''
        self.key = key
        if L is None:
            self.head = None
            self.tail = None
            return
        # If L is not subscriptable, then will generate an exception that reads:
        # TypeError: 'type_of_L' object is not subscriptable
        if not len(L[: 1]):
            self.head = None
            self.tail = None
            return
        node = Node(L[0])
        self.head = node
        for e in L[1: ]:
            node.next_node = Node(e)
            node.next_node.previous_node = node
            node = node.next_node
        self.tail = node

    def print_from_head_to_tail(self, separator = ', '):
        '''
        >>> DoublyLinkedList().print_from_head_to_tail(':')
        >>> DoublyLinkedList(range(1)).print_from_head_to_tail(':')
        0
        >>> DoublyLinkedList(range(2)).print_from_head_to_tail(':')
        0:1
        >>> DoublyLinkedList(range(3)).print_from_head_to_tail('--')
        0--1--2
        '''
        if not self.head:
            return
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.value))
            node = node.next_node
        print(separator.join(nodes))

    def print_from_tail_to_head(self, separator = ', '):
        '''
        >>> DoublyLinkedList().print_from_tail_to_head(':')
        >>> DoublyLinkedList(range(1)).print_from_tail_to_head(':')
        0
        >>> DoublyLinkedList(range(2)).print_from_tail_to_head(':')
        1:0
        >>> DoublyLinkedList(range(3)).print_from_tail_to_head('--')
        2--1--0
        '''
        if not self.tail:
            return
        nodes = []
        node = self.tail
        while node:
            nodes.append(str(node.value))
            node = node.previous_node
        print(separator.join(nodes))

    def duplicate(self):
        '''
        >>> L = DoublyLinkedList(L = [[[1]], [[2]]])
        >>> L1 = L.duplicate()
        >>> L1.head.value[0][0] = 0
        >>> L1.print_from_head_to_tail()
        [[0]], [[2]]
        >>> L1.print_from_tail_to_head()
        [[2]], [[0]]
        >>> L.print_from_head_to_tail()
        [[1]], [[2]]
        '''
        if not self.head:
            return
        node = self.head
        node_copy = Node(deepcopy(node.value))
        L = DoublyLinkedList(key = self.key)
        L.head = node_copy
        L.tail = node_copy
        node = node.next_node
        while node:
            node_copy.next_node = Node(deepcopy(node.value))
            node_copy.next_node.previous_node = node_copy
            node_copy = node_copy.next_node
            L.tail = node_copy
            node = node.next_node
        return L

    def __len__(self):
        '''
        >>> len(DoublyLinkedList())
        0
        >>> len(DoublyLinkedList([0]))
        1
        >>> len(DoublyLinkedList((0, 1)))
        2
        '''
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next_node
        return length

    def apply_function(self, function):
        '''
        >>> L = DoublyLinkedList(range(3))
        >>> L.apply_function(lambda x: 2 * x)
        >>> L.print_from_head_to_tail()
        0, 2, 4
        '''
        node = self.head
        while node:
            node.value = function(node.value)
            node = node.next_node

    def is_sorted(self):
        '''
        >>> DoublyLinkedList().is_sorted()
        True
        >>> DoublyLinkedList([0]).is_sorted()
        True
        >>> DoublyLinkedList([0, 0]).is_sorted()
        True
        >>> DoublyLinkedList([0, 1]).is_sorted()
        True
        >>> DoublyLinkedList([1, 0]).is_sorted()
        False
        >>> DoublyLinkedList([0, 1, 2, 3]).is_sorted()
        True
        >>> DoublyLinkedList([0, 2, 1, 3]).is_sorted()
        False
        >>> DoublyLinkedList([0, 1, 2, 3], lambda x: -x).is_sorted()
        False
        >>> DoublyLinkedList([3, 2, 1, 0], lambda x: -x).is_sorted()
        True
        '''
        node = self.head
        while node and node.next_node:
            if self.key(node.value) > self.key(node.next_node.value):
                return False
            node = node.next_node
        return True

    def extend(self, L):
        '''
        >>> L = DoublyLinkedList()
        >>> L.extend(DoublyLinkedList(range(2)))
        >>> L.print_from_head_to_tail()
        0, 1
        >>> L.print_from_tail_to_head()
        1, 0
        >>> L = DoublyLinkedList(range(2))
        >>> L.extend(DoublyLinkedList())
        >>> L.print_from_head_to_tail()
        0, 1
        >>> L.print_from_tail_to_head()
        1, 0
        >>> L = DoublyLinkedList((0,))
        >>> L.extend(DoublyLinkedList((1,)))
        >>> L.print_from_head_to_tail()
        0, 1
        >>> L.print_from_tail_to_head()
        1, 0
        >>> L = DoublyLinkedList(range(2))
        >>> L.extend(DoublyLinkedList(range(2, 4)))
        >>> L.print_from_head_to_tail()
        0, 1, 2, 3
        >>> L.print_from_tail_to_head()
        3, 2, 1, 0
        '''
        if not L.head:
            return
        if not self.head:
            self.head = L.head
            self.tail = L.tail
            return
        self.tail.next_node = L.head
        L.head.previous_node = self.tail
        self.tail = L.tail

    def reverse(self):
        '''
        >>> L = DoublyLinkedList()
        >>> L.reverse()
        >>> L.print_from_head_to_tail()
        >>> L = DoublyLinkedList([0])
        >>> L.reverse()
        >>> L.print_from_head_to_tail()
        0
        >>> L.print_from_tail_to_head()
        0
        >>> L = DoublyLinkedList([0, 1])
        >>> L.reverse()
        >>> L.print_from_head_to_tail()
        1, 0
        >>> L.print_from_tail_to_head()
        0, 1
        >>> L = DoublyLinkedList(range(4))
        >>> L.reverse()
        >>> L.print_from_head_to_tail()
        3, 2, 1, 0
        >>> L.print_from_tail_to_head()
        0, 1, 2, 3
        '''
        if not self.head:
            return
        self.tail = self.head
        node = self.head.next_node
        self.head.next_node = None
        while node:
            next_node = node.next_node
            node.previous_node = None
            node.next_node = self.head
            self.head.previous_node = node
            self.head = node
            node = next_node

    def recursive_reverse(self):
        '''
        >>> L = DoublyLinkedList()
        >>> L.recursive_reverse()
        >>> L.print_from_head_to_tail()
        >>> L = DoublyLinkedList([0])
        >>> L.recursive_reverse()
        >>> L.print_from_head_to_tail()
        0
        >>> L.print_from_tail_to_head()
        0
        >>> L = DoublyLinkedList([0, 1])
        >>> L.recursive_reverse()
        >>> L.print_from_head_to_tail()
        1, 0
        >>> L.print_from_tail_to_head()
        0, 1
        >>> L = DoublyLinkedList(range(4))
        >>> L.recursive_reverse()
        >>> L.print_from_head_to_tail()
        3, 2, 1, 0
        >>> L.print_from_tail_to_head()
        0, 1, 2, 3
        '''
        if not self.head or not self.head.next_node:
            return
        self.tail = self.head
        node = self.head
        while node.next_node.next_node:
            node = node.next_node
        last_node = node.next_node
        last_node.previous_node = None
        node.next_node = None
        self.recursive_reverse()
        last_node.next_node = self.head
        self.head.previous_node = last_node
        self.head = last_node

    def index_of_value(self, value):
        '''
        >>> L = DoublyLinkedList()
        >>> L.index_of_value(0)
        -1
        >>> L = DoublyLinkedList(range(10, 15))
        >>> L.index_of_value(10)
        0
        >>> L.index_of_value(14)
        4
        >>> L.index_of_value(12)
        2
        >>> L.index_of_value(16)
        -1
        '''
        index = 0
        node = self.head
        while node:
            if node.value == value:
                return index
            index += 1
            node = node.next_node
        return -1

    def value_at(self, index):
        '''
        >>> L = DoublyLinkedList()
        >>> L.value_at(0)
        >>> L = DoublyLinkedList([0])
        >>> L.value_at(0)
        0
        >>> L.value_at(1)
        >>> L = DoublyLinkedList(range(10, 15))
        >>> L = DoublyLinkedList(range(10, 15))
        >>> L.value_at(0)
        10
        >>> L.value_at(2)
        12
        >>> L.value_at(4)
        14
        >>> L.value_at(6)
        '''
        if index < 0:
            return
        node = self.head
        while node and index:
            node = node.next_node
            index -= 1
        if node:
            return node.value
        return

    def prepend(self, value):
        '''
        >>> L = DoublyLinkedList()
        >>> L.prepend(0)
        >>> L.print_from_head_to_tail()
        0
        >>> L.print_from_tail_to_head()
        0
        >>> L = DoublyLinkedList([1])
        >>> L.prepend(0)
        >>> L.print_from_head_to_tail()
        0, 1
        >>> L.print_from_tail_to_head()
        1, 0
        '''
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            return
        head = self.head
        self.head = Node(value)
        self.head.next_node = head
        head.previous_node = self.head

    def append(self, value):
        '''
        >>> L = DoublyLinkedList()
        >>> L.append(0)
        >>> L.print_from_head_to_tail()
        0
        >>> L.print_from_tail_to_head()
        0
        >>> L = DoublyLinkedList([0])
        >>> L.append(1)
        >>> L.print_from_head_to_tail()
        0, 1
        >>> L.print_from_tail_to_head()
        1, 0
        >>> L = DoublyLinkedList(range(2))
        >>> L.append(2)
        >>> L.print_from_head_to_tail()
        0, 1, 2
        >>> L.print_from_tail_to_head()
        2, 1, 0
        '''
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            return
        self.tail.next_node = Node(value)
        self.tail.next_node.previous_node = self.tail
        self.tail = self.tail.next_node

    def insert_value_at(self, value, index):
        '''
        >>> L = DoublyLinkedList()
        >>> L.insert_value_at(0, 3)
        >>> L.print_from_head_to_tail()
        0
        >>> L.print_from_tail_to_head()
        0
        >>> L = DoublyLinkedList([1])
        >>> L.insert_value_at(0, -1)
        >>> L.print_from_head_to_tail()
        0, 1
        >>> L.print_from_tail_to_head()
        1, 0
        >>> L = DoublyLinkedList([1])
        >>> L.insert_value_at(0, 0)
        >>> L.print_from_head_to_tail()
        0, 1
        >>> L.print_from_tail_to_head()
        1, 0
        >>> L = DoublyLinkedList([0])
        >>> L.insert_value_at(1, 1)
        >>> L.print_from_head_to_tail()
        0, 1
        >>> L.print_from_tail_to_head()
        1, 0
        >>> L = DoublyLinkedList([0])
        >>> L.insert_value_at(1, 2)
        >>> L.print_from_head_to_tail()
        0, 1
        >>> L.print_from_tail_to_head()
        1, 0
        >>> L = DoublyLinkedList([0, 2])
        >>> L.insert_value_at(1, 1)
        >>> L.print_from_head_to_tail()
        0, 1, 2
        >>> L.print_from_tail_to_head()
        2, 1, 0
        '''
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        if index <= 0:
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node
            return
        node = self.head
        while node.next_node and index > 1:
            node = node.next_node
            index -= 1
        next_node = node.next_node
        node.next_node= new_node
        new_node.previous_node = node
        if next_node:
            new_node.next_node = next_node
            next_node.previous_node = new_node
        else:
            self.tail = new_node

    def insert_value_before(self, value_1, value_2):
        '''
        >>> L = DoublyLinkedList([1, 2])
        >>> L.insert_value_before(0, 1)
        True
        >>> L.print_from_head_to_tail()
        0, 1, 2
        >>> L.print_from_tail_to_head()
        2, 1, 0
        >>> L = DoublyLinkedList([0, 2])
        >>> L.insert_value_before(1, 2)
        True
        >>> L.print_from_head_to_tail()
        0, 1, 2
        >>> L.print_from_tail_to_head()
        2, 1, 0
        >>> L = DoublyLinkedList([0, 1])
        >>> L.insert_value_before(2, 3)
        False
        '''
        if not self.head:
            return False
        if self.head.value == value_2:
            self.insert_value_at(value_1, 0)
            return True
        node = self.head
        while node.next_node and node.next_node.value != value_2:
            node = node.next_node
        if not node.next_node:
            return False
        new_node = Node(value_1)
        new_node.next_node = node.next_node
        node.next_node.previous_node = new_node
        node.next_node = new_node
        new_node.previous_node = node
        return True

    def insert_value_after(self, value_1, value_2):
        '''
        >>> L = DoublyLinkedList([0, 1])
        >>> L.insert_value_after(2, 1)
        True
        >>> L.print_from_head_to_tail()
        0, 1, 2
        >>> L.print_from_tail_to_head()
        2, 1, 0
        >>> L = DoublyLinkedList([0, 2])
        >>> L.insert_value_after(1, 0)
        True
        >>> L.print_from_head_to_tail()
        0, 1, 2
        >>> L.print_from_tail_to_head()
        2, 1, 0
        >>> L = DoublyLinkedList([0, 1])
        >>> L.insert_value_after(3, 2)
        False
        '''
        if not self.head:
            return False
        node = self.head
        while node and node.value != value_2:
            node = node.next_node
        if not node:
            return False
        next_node = node.next_node
        new_node = Node(value_1)
        node.next_node = new_node
        new_node.previous_node = node
        if next_node:
            new_node.next_node = next_node
            next_node.previous_node = new_node
        else:
            self.tail = new_node
        return True

    def insert_sorted_value(self, value):
        '''
        >>> L = DoublyLinkedList()
        >>> L.insert_sorted_value(1)
        >>> L.print_from_head_to_tail()
        1
        >>> L.print_from_tail_to_head()
        1
        >>> L.insert_sorted_value(0)
        >>> L.print_from_head_to_tail()
        0, 1
        >>> L.print_from_tail_to_head()
        1, 0
        >>> L.insert_sorted_value(2)
        >>> L.print_from_head_to_tail()
        0, 1, 2
        >>> L.print_from_tail_to_head()
        2, 1, 0
        >>> L.insert_sorted_value(1)
        >>> L.print_from_head_to_tail()
        0, 1, 1, 2
        >>> L.print_from_tail_to_head()
        2, 1, 1, 0
        '''
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        if value <= self.key(self.head.value):
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node
            return
        node = self.head
        while node.next_node and value > self.key(node.next_node.value):
            node = node.next_node
        next_node = node.next_node
        node.next_node = new_node
        new_node.previous_node = node
        if next_node:
            new_node.next_node = next_node
            next_node.previous_node = new_node
        else:
            self.tail = new_node

    def delete_value(self, value):
        '''
        >>> L = DoublyLinkedList([0, 1, 1, 2])
        >>> L.delete_value(3)
        False
        >>> L.delete_value(1)
        True
        >>> L.print_from_head_to_tail()
        0, 1, 2
        >>> L.print_from_tail_to_head()
        2, 1, 0
        >>> L.delete_value(0)
        True
        >>> L.print_from_head_to_tail()
        1, 2
        >>> L.print_from_tail_to_head()
        2, 1
        >>> L.delete_value(2)
        True
        >>> L.print_from_head_to_tail()
        1
        >>> L.print_from_tail_to_head()
        1
        >>> L.delete_value(1)
        True
        >>> L.print_from_head_to_tail()
        >>> L.print_from_tail_to_head()
        >>> L.delete_value(0)
        False
        '''
        if not self.head:
            return False
        if self.head.value == value:
            if self.tail == self.head:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next_node
                self.head.previous_node = None                
            return True
        node = self.head
        while node.next_node and node.next_node.value != value:
            node = node.next_node
        if node.next_node:
            node.next_node = node.next_node.next_node
            if node.next_node:
                node.next_node.previous_node = node
            else:
                self.tail = node
            return True
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
