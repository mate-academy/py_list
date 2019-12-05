"""Representation of singly linked list"""


class Item:
    """Item of linked list"""
    def __init__(self, val):
        self._val = val
        self._next = None

    def get_value(self):
        """Get value of the item"""
        return self._val

    def get_next(self):
        """Get next item"""
        return self._next

    def set_next(self, val):
        """Set link to the next item"""
        self._next = val


class List:
    """Class of linked list"""
    def __init__(self):
        self.head = None

    def insert(self, val):
        """Add item to the head of linked list"""
        new_item = Item(val)
        new_item.set_next(self.head)
        self.head = new_item

    def delete(self):
        """Remove first element of linked list"""
        del_item = self.head.get_value()
        self.head = self.head.get_next()
        return del_item

    def state(self):
        """Return state of linked list as string"""
        current = self.head
        state = []
        while current:
            state.append(current.get_value())
            current = current.get_next()
        return '[{0}]'.format(','.join(str(i) for i in state))
