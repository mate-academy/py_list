"""module docstring"""


class Item:
    """Node in linked list"""
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def get_value(self):
        """return value stored in node"""
        return self.value

    def get_next(self):
        """return pointer to next node"""
        return self.next_item


class List:
    """linked list"""
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        """place value at the head of the list"""
        new_item = Item(value)
        new_item.next_item = self.head
        self.head = new_item

    def state(self):
        """print current state of list"""
        if self.head is None:
            return "[]"
        state_str = "["
        crawler = self.head
        while crawler is not None:
            state_str += str(crawler.value) + ","
            crawler = crawler.next_item
        return state_str.rstrip(",") + "]"

    def delete(self):
        """delete first node from list return value stored in this node"""
        if self.head is None:
            return "[]"
        value = self.head.value
        self.head = self.head.next_item
        return value
