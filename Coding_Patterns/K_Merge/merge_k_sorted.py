# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def upheap(heap,i,n):
    parent = (i-1)//2

    if parent<0:
        return
    
    if heap[parent][0] > heap[i][0]:
        heap[i],heap[parent] = heap[parent],heap[i]
        upheap(heap,parent,n)

def downheap(heap,i,n):
    left = 2*i+1
    right = 2*i+2

    smallest = i

    if left<n and heap[smallest][0] > heap[left][0]:
        smallest = left
    
    if right<n and heap[smallest][0] > heap[right][0]:
        smallest = right 
    
    if smallest != i:
        heap[smallest],heap[i] = heap[i],heap[smallest]
        downheap(heap,smallest,n)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = None
        curr = None

        heap = []
        

        for top in lists:
            if top is not None:
                heap.append([top.val,top])
                n = len(heap)
                upheap(heap,n-1,n)

        print(heap)

        while heap:

            heap[0],heap[-1] = heap[-1],heap[0]
            temp = heap.pop(-1)[1]
            downheap(heap,0,len(heap))

            if head is None:
                head = temp
                curr = temp
            else:
                curr.next = temp
                curr = temp
            
            temp = temp.next
            if temp is not None:
                heap.append([temp.val,temp])
                upheap(heap,len(heap)-1,len(heap))
        
        return head

            
