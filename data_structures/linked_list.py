class Node:
    # each node has its data and a pointer to the next node
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            
    def insertAtStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        
    def insertAtPosition(self, data, position):
        newNode = Node(data)
        temp = self.head
        for i in range(position-1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
        
    def insertAfterNode(self, prevNode, data):
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
        
    def deleteNode(self, data):
        temp = self.head
        if temp.data == data: # if the node to be deleted is the head node
            self.head = temp.next
            temp = None
            return
        while temp: # if the node to be deleted is not the head node
            if temp.data == data:
                break # temp will be the node to be deleted
            prev = temp
            temp = temp.next
        if not temp: # if the node to be deleted is not present in the linked list
            return
        prev.next = temp.next # unlink the node from the linked list
        temp = None
            
    def deleteNodeAtPosition(self, position):
        pass
    
    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False
    
if __name__ == "__main__":
    List = LinkedList()
    List.head = Node(1)  # create the head node
    node2 = Node(2)
    List.head.setNext(node2)  # head node's next --> node2
    node3 = Node(3)
    node2.setNext(node3)  # node2's next --> node3
    List.insertAtStart(4)  # node4's next --> head-node --> node2 --> node3
    List.insertAfterNode(node2, 5)  # node2's next --> node5
    List.insertAtEnd(6)
    List.printLinkedList()
    print()
    List.deleteNode(3)
    List.printLinkedList()
    print()
    print(List.search(1))