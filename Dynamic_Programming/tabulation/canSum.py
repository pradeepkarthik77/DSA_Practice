def howSum(target,arr):
    
    dp = [None for i in range(target+1)]

    dp[0] = [[]]

    for i in range(target+1):
        if dp[i] is not None:
            for elem in arr:
                if i+elem <= target:
                    if dp[i+elem] is None:
                        thisarr = []
                        for A in dp[i]:
                            comb = A.copy()
                            comb.append(elem)
                            thisarr.append(comb)
                        dp[i+elem] = thisarr
                    else:
                        for A in dp[i]:
                            comb = A.copy()
                            comb.append(elem)
                            dp[i+elem].append(comb)
    
    print(dp[target])
    

if __name__=="__main__":
    arr = [5,3,4]
    target = 8
    print(howSum(target,arr))