from heapq import heappush,heappop

class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:
        if not self.maxheap or -self.maxheap[0] > num:
            heappush(self.maxheap,-num)
        else:
            heappush(self.minheap,num)
        
        if len(self.maxheap) > len(self.minheap)+1:
            heappush(self.minheap,-heappop(self.maxheap))
        
        elif len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap,-heappop(self.minheap))
        
    def findMedian(self) -> float:

        if (len(self.minheap)+len(self.maxheap)) %2 == 0:
            return (self.minheap[0]+(-self.maxheap[0]))/2
        
        else:
            return -self.maxheap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()