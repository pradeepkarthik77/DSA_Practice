class Heap:
    def __init__(self,arr):
        self.maxheap = arr
    
    def downheap(self,i,n):

        left = 2*i+1
        right = 2*i+2

        largest = i

        if left < n and self.maxheap[left] > self.maxheap[largest]:
            largest = left
        
        if right < n and self.maxheap[right] > self.maxheap[largest]:
            largest = right
        
        if largest != i:
            self.maxheap[i],self.maxheap[largest] = self.maxheap[largest],self.maxheap[i]
            self.downheap(largest,n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)

        heap = Heap(nums.copy())

        for i in range((n//2)-1,-1,-1):
            heap.downheap(i,n)
        
        elem = 0

        for i in range(k):
            elem = heap.maxheap[0]
            heap.maxheap[0],heap.maxheap[n-i-1] = heap.maxheap[n-i-1],heap.maxheap[0]
            heap.downheap(0,n-i-1)
        
        return elem

