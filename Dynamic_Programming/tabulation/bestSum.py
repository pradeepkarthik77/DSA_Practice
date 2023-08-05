def bestSum(target,arr):
    
    dp = [None]*(target+1)

    dp[0] = []

    for i in range(target+1):
        if dp[i] is not None:
            for elem in arr:
                if i+elem <= target:
                    if dp[i+elem] is None:
                        comb = dp[i].copy()
                        comb.append(elem)
                        dp[i+elem] = comb 
                    else:
                        comb = dp[i].copy()
                        comb.append(elem)

                        if len(dp[i+elem]) > len(comb):
                            dp[i+elem] = comb
    
    return dp[target]

if __name__=="__main__":
    arr = [5,3,4]
    target = 8
    print(bestSum(target,arr))