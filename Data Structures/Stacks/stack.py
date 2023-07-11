class Stack:
    def __init__(self,size=5):
        self.stack = []
        self.top = -1
        self.size = size
    
    def push(self,item):
        if (self.top+1) == self.size:
            print("Stack is full")
            return 
    
        self.stack.append(item)
        self.top+=1
    
    def pop(self):
        if (self.top) == -1:
            print("Stack is empty")
            return
        
        self.stack.pop(self.top)
        self.top-=1
    
    def printstack(self):
        return self.stack
    
if __name__=="__main__":
    obj = Stack(5)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.push(5)
    obj.push(6)
    print(obj.printstack())
    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()
    print(obj.printstack())

    