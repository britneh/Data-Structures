"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self, size, storage):
        self.size = size
        self.storage =  []

    def push(self, size, storage, value):
        self.storage.append(value)
        self.size += 1
        return self.size

    def pop(self,value):
        self.storage.pop(value)
        self.size -= 1
        return self.storage

    def __len__(self):
        return self.size