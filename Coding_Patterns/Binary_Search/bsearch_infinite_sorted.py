def findelement(arr,elem):
    beg = 0
    end = 0

    while not(arr[end]>=elem and arr[beg]<=elem):
        end = end+2
        beg = beg+1
    
    while beg<=end:
        mid = (beg+end)//2

        if arr[mid] == elem:
            return mid 
        elif arr[mid] > elem:
            end = mid-1
        else:
            beg = mid+1
    
    return -1

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    print("The index of the element is: ",findelement(arr,8))