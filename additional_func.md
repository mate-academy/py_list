 def size(self):
        """
        Return size of list.
        :return:
        """
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
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