'''
Module for representing singly linked list
'''


class Item:
    '''
    class for representing singly linked list
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data

    def get_next(self):
        '''

        :return:
        '''
        return self.next

    def get_data(self):
        '''

        :return:
        '''
        return self.data


class List:
    '''
    class for representing singly linked list
    '''
    def __init__(self):
        self.head = None

    def get_list(self):
        '''
        :return singly linked list
        '''
        linked_list = []
        if self.head is not None:
            current = self.head
            linked_list = [str(current.data)]
            while current.next:
                current = current.next
                linked_list.append(str(current.data))
            return f"[{','.join(linked_list)}]"
        return str(linked_list)

    def insert(self, value):
        '''Insert item'''
        if self.head:
            new = Item(value)
            new.next = self.head
            self.head = new
        else:
            self.head = Item(value)

    def delete(self):
        '''Delete item'''
        if self.head is None:
            raise ValueError
        value = self.head.data
        self.head = self.head.next
        return value
