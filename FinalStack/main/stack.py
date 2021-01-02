
# stack implementation.

class Stack:

    def __init__(self): # constructor for Stack includes list variable called items.
        self.items = []

    def push(self, item): # push method allows to append new items into list.
        self.items.append(item)

    def pop(self): # removes and returns top element of stack.
        if (len(self.items) == 0):
            raise IndexError("The stack is empty.") # raises index error if stack is empty.
        else:
            return self.items.pop()

    def top(self): # returns top element of the stack.
        if (self.size() == 0):
           raise IndexError("The stack is empty.") # raises index error if stack is empty.
        return self.items[len(self.items) - 1]
            

    def size(self): # returns size of stack.
        return len(self.items)

    def clear(self): # clears all elements in stack.
        while (Stack.size(self) != 0):
            self.pop()

   