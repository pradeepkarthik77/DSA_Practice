def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1,-1,-1):
        for j in range(n-1,0+(n-i-1),-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]

value = input("Enter the array:")

arr = list(map(int,value.split()))

bubble_sort(arr)

print(arr)