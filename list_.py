"""
Create class for representing singly linked list
(https://www.geeksforgeeks.org/data-structures/linked-list/).
Implement insertion to the head and deletion from the head of it.
"""


class Item:
    """Item class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        """Get data"""
        return self.data

    def get_next(self):
        """Get next"""
        return self.next


class List:
    """List class"""
    def __init__(self):
        self.head = None

    def insert(self, new_data):
        """Add item to list"""
        new_item = Item(new_data)
        new_item.next = self.head
        self.head = new_item

    def state(self):
        """Display the contents of the list"""
        lst = []
        temp = self.head
        while temp:
            lst.append(temp.data)
            temp = temp.next
        return lst

    def delete(self):
        """Delete the list item"""
        temp = self.head.data
        self.head = self.head.next
        return temp
