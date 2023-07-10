class Array:
    def __init__(self):
        self.arr = []
        self.length = 0
    
    def add(self,item):
        self.arr.append(item)
        self.length+=1
    
    def pop(self,index):
        element = self.arr[index-1]
        j = index-1
        
        while j != self.length-1:
            self.arr[j] = self.arr[j+1]
            j+=1
            
        del self.arr[self.length-1]
        self.length = self.length - 1
    
    def printarr(self):
        for i in range(self.length):
            print(self.arr[i],end=" ")
        print()

arr = Array()

arr.add(1)
arr.add(2)
arr.add(3)
arr.add(4)

arr.pop(4)

arr.printarr()