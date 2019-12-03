"""
module linked list implementation
"""


class Item:
    """
    Node representation
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """
        Return present item from linked list.
        :return: Any
        """
        return self.data

    def get_next_item(self):
        """
        Return next item from linked list.
        :return: Any
        """
        return self.next


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
            new_node.next = self.head
            self.head = new_node

    def delete(self):
        """
        Remove top element from the linked list and return this element.
        :return:
        """
        if self.head is None:
            return None
        node_item = self.head.data
        self.head = self.head.next
        return node_item

    def state(self):
        """
        Return the current state of the linked list.
        :return:
        """
        res = ''
        if self.head is not None:
            node_item = self.head
            while node_item is not None:
                res += str(node_item.data)
                node_item = node_item.next
            return '[' + ','.join(res) + ']'
        return '[]'

    def size(self):
        """
        Return size of list.
        :return:
        """
        node_item = self.head
        count = 0
        while node_item is not None:
            count = count + 1
            node_item = node_item.next
        return count

    def is_empty(self):
        """
        Check if the stack is empty.
        :return:
        """
        return self.head is None

    def top(self):
        """
        Return top element in the stack.
        :return:
        """
        return self.head.data
