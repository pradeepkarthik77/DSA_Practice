# program to return one possible combination in a array that has the given target
def howSum(target,arr,dp,stack):
    
    if target == 0:
        print(stack)
        return True
    elif target < 0:
        return False
    
    elif target in dp:
        return target[dp]
    
    else:
        for i in arr:
            remainder = target-i
            
            stack.append(i)
            
            if howSum(remainder,arr,dp,stack):
                dp[target] = True
                return True
            else:
                stack.pop(-1)
                continue
        
        dp[target] = False
        return False

dp = {}
print(howSum(8,[2,3,4,5],dp,[]))