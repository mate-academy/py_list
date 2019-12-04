"""
docstring
"""


class Node:
    """
    Node class docstring
    """
    def __init__(self, data):
        """

        :param data:
        """
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        """

        :return:
        """
        return self.data

    def get_next_data(self):
        """

        :return:
        """
        return self.next if not None else None


class List:
    """
    List class docstring
    """
    def __init__(self):
        """

        """
        self.head = None

    def state(self):
        """

        :return:
        """
        result = ''
        lst = []
        if self.head is not None:
            var = self.head
            while var is not None:
                result += str(var.data) + ','
                var = var.next
            return '[' + result.rstrip(',') + ']'
        return str(lst)

    def insert(self, new_data):
        """

        :param new_data:
        :return:
        """
        if self.head is not None:
            new_node = Node(new_data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
        elif self.head is None:
            self.head = Node(new_data)

    def delete(self):
        """

        :return:
        """
        if self.head is not None:
            delete = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return delete
        return None
