class Node:
    def __init__(self,data=0,next=None,prev=None):
        self.data = data
        self.prev = prev
        self.next = next 

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self,val):

        node = Node(val)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node 
        node.prev = self.tail 

        self.tail = node
    
    def printDLL(self):
        temp = self.head 

        arr = []

        while temp:
            arr.append(temp.data)
            temp = temp.next 
        
        return arr 

obj = DLL()
obj.addNode(1)
obj.addNode(2)
obj.addNode(3)
obj.addNode(4)
print(obj.printDLL())
obj.removeNode(2)
print(obj.printDLL())




