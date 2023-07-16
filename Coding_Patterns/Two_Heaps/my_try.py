class MaxHeap:
    def __init__(self,maxheap=[],maxN=0):
        self.maxheap = maxheap
        self.maxN = maxN
    
    def addNode(self,item):
        self.maxheap.append(item)
        self.maxN+=1
        self.upheap(self.maxN-1)
    
    def removetop(self):
        self.maxheap[0],self.maxheap[-1] = self.maxheap[-1],self.maxheap[0]
        elem = self.maxheap.pop(-1)
        self.maxN-=1
        self.downheap(0)
    
    def returntop(self):
        if self.maxN == 0:
            return 0
        else:
            return self.maxheap[0]
    
    def downheapify(self,i):

        left = 2*i+1
        right = 2*i+2
        largest = i

        if left<self.maxN and self.maxheap[left] > self.maxheap[largest]:
            largest = left
        
        if right<self.maxN and self.maxheap[right] > self.maxheap[largest]:
            largest = right
        
        if largest != i:
            self.maxheap[i],self.maxheap[largest] = self.maxheap[largest],self.maxheap[i]
            self.downheapify(largest)
    
    def upheap(self,i):
        parent = (i//2)-1

        if parent < 0:
            return
        
        if self.maxheap[i] > self.maxheap[parent]:
            self.maxheap[i],self.maxheap[parent] = self.maxheap[parent],self.maxheap[i]
            self.upheap(parent)

class MinHeap:
    def __init__(self,minheap=[],minN=0):
        self.minheap = minheap
        self.minN = minN
    
    def addNode(self,num):
        self.minheap.append(num)
        self.minN+=1
        self.upheap(self.minN-1)
    
    def removetop(self):
        self.minheap[0],self.minheap[-1] = self.minheap[-1],self.minheap[0]
        elem = self.minheap.pop(-1)
        self.minN-=1
        self.downheap(0)

    def returntop(self):
        if self.minN == 0:
            return 0
        else:
            return self.minheap[0]
    
    def downheapify(self,i):

        left = 2*i+1
        right = 2*i+2
        largest = i

        if left<self.minN and self.minheap[left] < self.minheap[largest]:
            largest = left
        
        if right<self.minN and self.minheap[right] < self.minheap[largest]:
            largest = right
        
        if largest != i:
            self.minheap[i],self.minheap[largest] = self.minheap[largest],self.minheap[i]
            self.downheapify(largest)
    
    def upheap(self,i):
        parent = (i//2)-1

        if parent < 0:
            return
        
        if self.minheap[i] < self.minheap[parent]:
            self.minheap[i],self.minheap[parent] = self.minheap[parent],self.minheap[i]
            self.upheap(parent)

class MedianFinder:

    def __init__(self):
        self.min = MinHeap()
        self.max = MaxHeap()
    
    def balance(self,obj1,obj2):
        elem = obj1.removetop()
        obj2.addNode(elem)

    def addNum(self, num: int) -> None:

        if self.max.maxN == 0:
            self.max.addNode(num)
        
        elif num <= self.max.maxheap[0]:
            self.max.addNode(num)
        
        else:
            self.min.addNode(num)
        
        if self.max.maxN != self.min.minN:

            if (self.max.maxN+self.min.minN)%2!=0 and (self.max.maxN - self.min.minN) == 1:
                return
            
            else:
                print(self.max.maxN,self.min.minN)
                while self.max.maxN == self.min.minN:
                    if self.max.maxN > self.min.minN:
                        self.balance(self.max,self.min)
                    else:
                        self.balance(self.min,self.min)
        

    def findMedian(self) -> float:
        print(self.min.minheap,self.max.maxheap)
        if (self.max.maxN+self.min.minN) %2 == 0:
            avg = (self.max.returntop()+self.min.returntop())/2
            return avg
        else:
            return self.max.returntop()


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()