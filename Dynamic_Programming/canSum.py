def canSum(target,arr,dp):
    
    if target == 0:
        return True
        
    elif target < 0:
        return False
        
    elif target in dp:
        return dp[target]
        
    else:
        for i in arr:
            if canSum(target-i,arr,dp):
                dp[target] = True
                return dp[target]
            else:
                continue
        dp[target] = False
        return dp[target]

dp = {}

print(canSum(7,[5,3,4,7],dp))