#!/usr/bin/python3
"""
Define classes Node and SinglyLinkedList for a singly linked list.
"""


class Node:
    """Represent a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new node.

        Parameters:
        - data: Integer value for the node.
        - next_node: The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Parameters:
        - value: Integer value for the new Node.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (
                    current.next_node is not None and
                    current.next_node.data < value
                    ):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
        - str: String representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
