"""linked list realisation"""


class Item:
    """Item realisation"""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return self.value

    def next_prev(self):
        """
        :return: (previous item, next item)
        """
        return (self.previous, self.next)


class List:
    """item list realisation"""
    def __init__(self):
        self.head = None

    def state(self):
        """
        :return: items list in str format
        """
        result = []
        if self.head is not None:
            current = self.head
            result = [str(current.value)]
            while current.previous is not None:
                current = current.previous
                result.append(str(current.value))
            return "[" + ",".join(result) + "]"
        return str(result)

    def insert(self, value):
        """
        Insert item in list
        :param value: item value
        :return: None
        """
        if self.head is None:
            self.head = Item(value)
        else:
            new = Item(value)
            new.previous = self.head
            self.head.next = self.head = new


    def delete(self):
        """
        Delete item from list
        :return: deleted item
        """
        if self.head is not None:
            for_del = self.head
            self.head = self.head.previous
            self.head.next = None
            return for_del.value
        raise IndexError
