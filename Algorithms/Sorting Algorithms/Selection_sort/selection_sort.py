def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        smallest = i
        for j in range(i+1,n):
            if arr[j] < arr[smallest]:
                smallest = j 
        arr[i],arr[smallest] = arr[smallest],arr[i]      

arr = list(map(int,input("Enter the array: ").split()))
selection_sort(arr)
print(arr)