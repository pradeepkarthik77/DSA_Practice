def insert_sort(arr):
    n = len(arr)

    for i in range(1,n):

        key = arr[i]
        j = i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        
        arr[j+1] = key


if __name__=="__main__":
    arr = list(map(int,input("Enter the arr: ").split()))
    insert_sort(arr)
    print(arr)