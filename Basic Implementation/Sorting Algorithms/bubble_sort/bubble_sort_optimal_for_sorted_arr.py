def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                swapped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        
        if not swapped:
            print("Array already sorted")
            break

value = input("Enter the array:")

arr = list(map(int,value.split()))

bubble_sort(arr)

print(arr)