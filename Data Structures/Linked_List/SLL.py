class Node:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self):
        self.head = None
    
    def addNode(self,item):
        newnode = Node(item)

        if self.head is None:
            self.head = newnode 
            return

        temp = self.head

        while temp.next:
            temp = temp.next
        
        temp.next = newnode
    
    def returnList(self):
        arr = []

        temp = self.head 

        while temp:
            arr.append(temp.data)
            temp = temp.next
        
        return arr

    def length(self):
        count = 0
        temp = self.head

        while temp:
            count+=1
            temp = temp.next 
        
        return count 

    def deleteNode(self,item):

        temp = self.head
        prev = None 

        while temp:

            if temp.data == item:
                if prev == None:
                    self.head = temp.next
                    return True
                else:
                    prev.next = temp.next
                    temp = temp.next
            else:
                prev = temp 
                temp = temp.next
        else:
            return False

if __name__ == "__main__":
    sll = SLL()

    sll.addNode(1)
    sll.addNode(2)
    sll.addNode(3)
    sll.addNode(4)

    print(sll.returnList())
    print(sll.deleteNode(1))
    print(sll.returnList())
