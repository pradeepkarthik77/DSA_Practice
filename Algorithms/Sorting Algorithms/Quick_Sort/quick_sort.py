def partition(arr,left,right):
    pivot = arr[right]

    i = left-1
    
    for j in range(left,right):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[right] = arr[right],arr[i+1]
    return i+1

def quick_sort(arr,left,right):
    if left<right:

        pivot = partition(arr,left,right)
        quick_sort(arr,left,pivot-1)
        quick_sort(arr,pivot+1,right)


if __name__=="__main__":
    arr = list(map(int,input("Enter the arr: ").split()))
    quick_sort(arr,0,len(arr)-1)
    print(arr)