# Written by Eric Martin for COMP9021


'''
A Stack abstract data type
'''


class EmptyStackError(Exception):
    def __init__(self, message):
        self.message = message


class Stack:
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def peek(self):
        '''
        >>> stack = Stack()
        >>> stack.peek()
        Traceback (most recent call last):
        ...
        EmptyStackError: Cannot peek at top of empty stack
        '''
        if self.is_empty():
            raise EmptyStackError('Cannot peek at top of empty stack')
        return self._data[-1]

    def push(self, datum):
        self._data.append(datum)

    def pop(self):
        '''
        >>> stack = Stack()
        >>> stack.peek()
        Traceback (most recent call last):
        ...
        EmptyStackError: Cannot pop from top of empty stack
        '''
        if self.is_empty():
            raise EmptyStackError('Cannot pop from top of empty stack')
        return self._data.pop()
        
