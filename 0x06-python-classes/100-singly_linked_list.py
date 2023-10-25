#!/usr/bin/python3
"""Defines a class Node and SinglyLinkedList."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node.

        Args:
            data (int): The data of the new node.
            next_node (Node): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value (int): The new data of the node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node.

        Returns:
            Node: The next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node.

        Args:
            value (Node): The new next node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The value of the new Node to insert.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Prints the entire list in stdout.

        Returns:
            str: The entire list, one node number by line.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
