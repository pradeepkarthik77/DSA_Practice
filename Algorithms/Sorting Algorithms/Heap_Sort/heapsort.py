def downheap(arr,i,n):
    left = 2*i+1
    right = 2*i+2
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left 
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        downheap(arr,largest,n)

def heapify(arr):
    n = len(arr)
    
    for i in range((n//2)-1,-1,-1):
        downheap(arr,i,n)

def heapsort(arr,n):

    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        downheap(arr,0,i)
    
    return arr

if __name__=="__main__":

    arr = list(map(int,input().split()))

    heapify(arr)
    print("constructed heap:",arr)
    newarr = heapsort(arr,len(arr))
    print("Sorted arr: ",newarr)