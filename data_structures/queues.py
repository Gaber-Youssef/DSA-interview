class Queue:
    def __init__(self, limit=10):
        self.items = []
        self.size = 0
        self.front = None # front is the index of the first element
        self.rear = None # rear is the index of the last element
        self.limit = limit
        
    def __str__(self):
        return " ".join([str(i) for i in self.items])
    
    def isEmpty(self):
        return self.items == []
    
    def isFull(self):
        return self.size == self.limit
    
    def getSize(self):
        return self.size
    
    def enqueue(self, data):
        if self.isFull():
            print("Queue is full")
        else:
            self.items.append(data)
            if self.front is None:
                self.front = self.rear = 0
            else:
                self.rear = self.size
            self.size += 1
            
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.items.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
                

if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    print(q)
    
    for i in range(5):
        q.dequeue()
    print(q)
