def bsearch(arr,x,left,right):

    while left < right:

        mid = (left+right)//2
        
        if arr[mid] == x:
            return mid
        elif x>arr[mid]:
            left = mid+1
        else:
            right = mid-1
    else:
        return -1


if __name__=="__main__":
    arr = list(map(int,input("Enter the arr: ").split()))
    element = int(input("Enter the element to be searched: "))
    boole = bsearch(arr,element,0,len(arr)-1)
    print(boole)