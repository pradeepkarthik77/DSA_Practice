def get_next(num):

    n = str(num)

    sum =0 

    for i in n:
        sum+=int(i)**2
    
    return sum

def findcycle(n):

    slow = get_next(n)
    fast = get_next(get_next(n))

    while fast!=1 and fast!=slow:
        fast = get_next(get_next(fast))
        slow = get_next(slow)
    
    return fast == 1

if __name__=="__main__":
    n = 116
    print(findcycle(n))