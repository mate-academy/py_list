"""
Module that define singly linked list data structure
Classes
-------
Node
List
"""


class Node:
    """
    A class, representing a node of the linked list
    Attributes
    ----------
    data : Any  --  information stored in the node
    next : Node --  pointer to the next node

    Methods
    -------
    get_data
    get_next
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """Return information stored in the node"""
        return self.data

    def get_next(self):
        """Return pointer to the next node"""
        return self.next


class List:
    """
    A class, representing linked list
    Attributes
    ----------
    head : Node  --  first node of the linked list

    Methods
    -------
    state() -- return all elements of the list
    insert(value) -- insert new element in the beginning of the list
    delete() -- delete first element of the list
    """
    def __init__(self):
        self.head = None

    def state(self):
        """Return all elements of the linked list (str)"""
        volume = []
        list_element = self.head
        while list_element:
            volume.append(list_element.data)
            list_element = list_element.next
        return '[' + ','.join(map(str, volume)) + ']'

    def insert(self, value):
        """Insert new element in the beginning of the list"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self):
        """Delete first element of the linked list"""
        if self.head is None:
            return 'List is empty!!!'
        deleted = self.head.data
        self.head = self.head.next
        return deleted
