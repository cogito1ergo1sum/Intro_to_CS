class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def get_head(self):
        return self.head
    def get_tail(self):
        return self.tail
    def insert_tail(self):
        pass

######################mid_val_method####################    
    def mid_val(self):
        start = self.get_head()
        end = self.get_tail()
        while start != end:
            if start.get_next() == end.get_prev():
                return start.get_next().get_data()
            start = start.get_next()
            end = end.get_prev()
        return start.get_data(), end.get_data()

################end_of_method###########################

class Node:
    def __init__(self, val=None):
        self._val=val
        self._next=None
        self._prev=None
    def get_data(self):
        return self._val
    def get_next(self):
        return self._next
    def set_next(self, node):
        self._next = node
    def get_prev(self):
        return self._prev
    def set_prev(self, node):
        self._prev = node

