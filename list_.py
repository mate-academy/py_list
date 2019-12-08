"""Create class for representing singly linked list"""


class Item:
    """Item representation"""
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def get_data(self):
        """Return data"""
        return self.data

    def get_next(self):
        """Return next data item"""
        return self.next


class List:
    """Linked list representation"""
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert data to linked list"""
        new_node = Item(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self):
        """Delete data from linked list"""
        if self.head is None:
            return None
        item = self.head.data
        self.head = self.head.next
        return item

    def state(self):
        """Return current state of linked list"""
        new_list = []
        item = self.head
        while item:
            new_list.append(item.data)
            item = item.next
        return str(new_list).replace(' ', '')
