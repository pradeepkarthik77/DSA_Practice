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
            val.append(i)
            if shortest is None or len(val) < len(shortest):
                shortest = val.copy()
    
    dp[target] = shortest
    return shortest

arr = [5,3,4,2]
target = 7

dp = {}

print(bestSum(target,arr,dp))