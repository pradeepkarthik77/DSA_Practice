def bestSum(target,arr,dp):
    
    if target == 0:
        return []
    elif target < 0:
        return None
    elif target in dp:
        return dp[target]
    
    shortest = None
    
    for i in arr:
        rem = target-i
        
        val = bestSum(rem,arr,dp)
        
        if val is not None:
            combination = val.copy()
            combination.append(i)
            if shortest is None or len(combination) < len(shortest):
                shortest = combination
    
    dp[target] = shortest
    return shortest

arr = [1,2,5,25]
target = 100

dp = {}

print(bestSum(target,arr,dp))