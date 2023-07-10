def merge(arr,left,mid,right):

    n1 = mid-left+1
    n2 = right-mid

    arr1 = [0] * (n1+1)
    arr2 = [0] * (n2+1)

    indx = 0
    for i in range(left,mid+1):
        arr1[indx] = arr[i]
        indx+=1
    
    indx = 0
    for i in range(mid+1,right+1):
        arr2[indx] = arr[i]
        indx+=1
    
    arr1[-1] = float('inf')
    arr2[-1] = float('inf')

    print(arr1,arr2)

    l = 0
    r = 0

    for indx in range(left,right+1):

        if(arr1[l] < arr2[r]):
            arr[indx] = arr1[l]
            l+=1
        else:
            arr[indx] = arr2[r]
            r+=1

    print("arr:",arr)
    

def merge_sort(arr,l,r): 
    if l<r:
        mid = (l+r)//2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        merge(arr,l,mid,r)

if __name__ == "__main__":
    arr = list(map(int,input("Enter the arr: ").split()))
    merge_sort(arr,0,len(arr)-1)