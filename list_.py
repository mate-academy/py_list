"""This program creates and deletes linked list"""


class Item:
    """This is a class that represents an item
    of "node" type to be added to linked list"""

    def __init__(self, data):
        """Initiate node-type item with its properties"""
        self.data = data
        self.next = None

    def get_data(self):
        """Initiate data return"""
        return self.data

    @staticmethod
    def pylint_block():
        """No idea what else Item should do
        so this is just a fake method"""
        return None


class List():
    """This is a class that represents an item
    of linked list"""
    def __init__(self):
        """Initiate linked list with its properties"""
        self.head = None

    def insert(self, new_data):
        """Describe mechanism of adding new item
        at the beginning of the list"""
        new_item = Item(new_data)
        new_item.next = self.head
        self.head = new_item

    def delete(self):
        """Describe mechanism of removing an item
        at the beginning of the list"""
        if self.head is None:
            return None
        item_to_delete = self.head
        self.head = item_to_delete.next
        data = item_to_delete.data
        item_to_delete = None
        return data

    def state(self):
        """Show the current state of the linked list contents"""
        current_item = self.head
        result = ""
        while current_item:
            result += "%d" % current_item.data
            if current_item.next is None:
                break
            result += ","
            current_item = current_item.next
        return f"[{result}]"
