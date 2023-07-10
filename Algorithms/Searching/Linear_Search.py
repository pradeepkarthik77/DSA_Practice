def lsearch(arr,x):

    for indx,element in enumerate(arr):
        if element == x:
            return indx
    return -1


if __name__=="__main__":
    arr = list(map(int,input("Enter the arr: ").split()))
    element = int(input("Enter the element to be searched: "))
    boole = lsearch(arr,element)
    print(boole)