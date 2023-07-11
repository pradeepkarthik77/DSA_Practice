class Heap:
    def __init__(self,arr):
        self.heap = arr.copy()
        self.length = len(self.heap)
    
    def heapify(self,i):
        left = 2*i+1
        right = 2*i+2
        largest = i 

        if left < self.length and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < self.length and self.heap[right] > self.heap[largest]:
            largest = right 
        
        if largest!=i:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            self.heapify(largest)
    
    def upheap(self,i):
        parent = (i-1)//2

        if parent < 0:
            return

        if self.heap[i] > self.heap[parent]:
            self.heap[parent],self.heap[i] = self.heap[i],self.heap[parent]
            self.upheap(parent)
    
    def addtoHeap(self,item):
        self.heap.append(item)
        self.length+=1
        self.upheap(self.length-1)
    
    def heapit(self):
        for i in range((self.length//2)-1,-1,-1):
            self.heapify(i)
    
    def removeTop(self):
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]

        self.heapify(0)
    
    def printHeap(self):
        return self.heap

    
if __name__=="__main__":
    heap = Heap([1,2,3,6,7,9,10])
    heap.heapit()
    print(heap.printHeap())
    heap.addtoHeap(11)
    print(heap.printHeap())
    heap.removeTop()
    print(heap.printHeap())