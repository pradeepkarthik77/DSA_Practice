def merge(arr,beg,mid,end):

    n1 = mid-beg+1 
    n2 = end-mid
    
    arr1 = [0]*n1 
    arr2 = [0]*n2 
    
    indx = beg 
    
    for i in range(n1):
        arr1[i] = arr[indx]
        indx+=1 
    
    indx = mid+1 
    
    for i in range(n2):
        arr2[i] = arr[indx]
        indx+=1 
    
    print(arr1,arr2)

def mergesort(arr,beg,end):
    
    if beg < end:
        mid = (beg+end)//2
        mergesort(arr,beg,mid)
        mergesort(arr,mid+1,end)
        merge(arr,beg,mid,end)

if __name__=="__main__":
    arr = [1,2,3,4,5]
    mergesort(arr,0,len(arr)-1)