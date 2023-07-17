from collections import defaultdict
def downheap(heap,i,n):
    left = 2*i+1
    right = 2*i+2

    smallest = i

    if left<n and (heap[left][1] < heap[smallest][1] or (heap[left][1] == heap[smallest][1] and heap[left][0] > heap[smallest][0])):
        smallest = left
    
    if right<n and (heap[right][1] < heap[smallest][1] or (heap[right][1] == heap[smallest][1] and heap[right][0] > heap[smallest][0])):
        smallest = right
    
    if smallest != i:
        heap[smallest],heap[i] = heap[i],heap[smallest]
        downheap(heap,smallest,n)

def upheap(heap,i,n):
    parent = (i-1)//2

    if parent < 0:
        return
    
    if heap[i][1] < heap[parent][1] or (heap[i][1] == heap[parent][1] and heap[i][0] > heap[parent][0]):
        heap[i],heap[parent] = heap[parent],heap[i]
        upheap(heap,parent,n)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hashmap = defaultdict(int)

        for task in tasks:
            hashmap[task] +=1

        tasker = []

        time = 1

        for value in hashmap.values():
            tasker.append([value,time])
            upheap(tasker,len(tasker)-1,len(tasker))
        
        while tasker:
            elem = tasker[0]

            if elem[1] <= time:
                #logic to pop and process
                elem = tasker.pop(0)
                elem[0]-=1
                elem[1] += (n+1)

                if elem[0]>0:
                    tasker.append(elem)
                    upheap(tasker,len(tasker)-1,len(tasker))
            
            time+=1
        return time-1

        
