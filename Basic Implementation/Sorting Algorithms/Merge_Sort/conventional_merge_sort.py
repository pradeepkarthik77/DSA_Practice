def merge(arr,left,mid,right):

    arr1 = [arr[x] for x in range(left,mid+1)]
    arr2 = [arr[x] for x in range(mid+1,right+1)]

    n1 = mid-left+1
    n2 = right-mid

    l = 0
    r = 0
    indx = left

    print(arr1,arr2)

    while l<n1 and r<n2:
        if(arr1[l] < arr2[r]):
            arr[indx] = arr1[l]
            l+=1
            indx+=1
        else:
            arr[indx] = arr2[r]
            r+=1 
            indx+=1 
    
    if l == n1:
        while r<n2:
            arr[indx] = arr2[r]
            r+=1
            indx+=1
    
    if r == n2:
        while l<n1:
            arr[indx] = arr1[l]
            l+=1
            indx+=1

    print("arr: ",arr)

def merge_sort(arr,l,r):
    if l<r:
        mid = (l+r)//2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        merge(arr,l,mid,r)


if __name__ == "__main__":
    arr = list(map(int,input("Enter the arr: ").split()))
    merge_sort(arr,0,len(arr)-1)
    print(arr)