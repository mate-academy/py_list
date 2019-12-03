"""
module linked list implementation
"""


class Item:
    """
    Node representation
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class List:
    """
    Linked List implementation which contains a Node object
    """

    def __init__(self):
        self.head = None

    def insert(self, data):
        """
        Add an element data to the linked list by using LIFO Principle.
        :param data:
        :return:
        """
        if self.head is None:
            self.head = Item(data)
        else:
            new_node = Item(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def delete(self):
        """
        Remove top element from the linked list and return this element.
        :return:
        """
        if self.head is None:
            return None
        temp = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return temp

    def state(self):
        """
        Return the current state of the linked list.
        :return:
        """
        res = '['
        if self.head is not None:
            temp = self.head
            while temp is not None:
                res += str(temp.data) + ','
                temp = temp.next
            return res.rstrip(',') + ']'
        return '[]'
