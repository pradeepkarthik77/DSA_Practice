# Incomplete Implementation
def binary_insert(arr,element):

    left = 0
    right = len(arr)-1

    while left<right:
        mid = (left+right)//2
        print(arr[mid])

        if arr[mid] <= element:
            left = mid+1
        else:
            right = mid
    
    arr.insert(left,element)

    print(arr,left)

if __name__=="__main__":
    extra_arr = list(map(int,input("Enter the arr: ").split()))

    arr = []

    binary_insert(extra_arr,4)

    exit()

    for element in extra_arr:
        binary_insert(arr,element)
    
    print(arr)