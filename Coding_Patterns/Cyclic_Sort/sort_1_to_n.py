def sortn(arr):
    n = len(arr)

    for i in range(n):
        if arr[i] != i+1:
            arr[arr[i]-1],arr[i] = arr[i],arr[arr[i]-1]

if __name__=="__main__":
    arr = [3,1,5,4,2]

    sortn(arr)

    print(arr)