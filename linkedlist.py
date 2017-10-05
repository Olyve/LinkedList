#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return len(self.items()) == 0

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        return len(self.items())

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        node = Node(item)

        if self.is_empty():
            self.head = node
            node.next = None
        else:
            self.tail.next = node

        self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        node = Node(item)
        if self.is_empty():
            self.tail = node
        else:
            node.next = self.head
        self.head = node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        current_node = self._find_node(item)
        if current_node is None:
            raise ValueError('{0} does not contain {1}'.format(self.__class__.__name__, item))

        if current_node == self.head and current_node == self.tail:
            self.head = None
            self.tail = None
        elif current_node == self.head:
            print(current_node.next)
            self.head = current_node.next
        elif current_node == self.tail:
            previous_node = self._find_previous_node(current_node)
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node = self._find_previous_node(current_node)
            previous_node.next = current_node.next

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        for item in self.items():
            if quality(item):
                return item

    def replace(self, item, new_item):
        node = self._find_node(item)
        node.data = new_item

    def _find_node(self, item):
        """Returns the first node it encounters where data is equal to item"""
        current_node = self.head
        while current_node is not None:
            if current_node.data == item:
                return current_node
            current_node = current_node.next

    def _find_previous_node(self, node):
        """Returns the node that is before node"""
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node != node:
                previous_node = current_node
                current_node = current_node.next
            else:
                return previous_node


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    ll.replace('B', 'S')
    print(ll)


if __name__ == '__main__':
    test_linked_list()
