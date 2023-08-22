"""
Quick summary: 
    a sequential collection where elements are added to and removed from the same end.
Important facts:
    - First-in, last-out (FILO) data structure.
    - Equivalent of a real-life pile of papers on desk.
    - In stack terms, to insert is to push, and to remove is to pop.
    - Often implemented on top of a linked list where the head is used for both insertion and removal. Can also be implemented using dynamic arrays.
Pros:
    - Fast insertions and deletions: O(1).
Cons:
    - Access and search are O(n).
Notable uses:
    - Maintaining undo history.
    - Tracking execution of program functions via a call stack.
    - Reversing order of items.
Time complexity (worst case):
    - Access: O(n)
    - Search: O(n)
    - Insertion (pushing): O(1)
    - Deletion (popping): O(1)
"""

class Stack:
    def __init__(self, limit=10):
        self.items = []
        self.limit = limit
        
    def __str__(self):
        return " ".join([str(i) for i in self.items])

    def push(self, item):
        if len(self.items) >= self.limit:
            print("Stack Overflow")
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
          return -1

    def size(self):
        return len(self.items)
    
    def peek(self):
        # getting the last element of the stack without removing it
        if self.items:
            return self.items[-1]
        else:
            return -1
    
    def isEmpty(self):
        return self.items == []
    
    
if __name__ == "__main__":
    # test stack
    myStack = Stack()
    for i in range(10):
        myStack.push(i)
    print(myStack)
    print(myStack.size())
    print(myStack.peek())
    print(myStack.pop())
    print(myStack.peek())
    print(myStack.isEmpty())
