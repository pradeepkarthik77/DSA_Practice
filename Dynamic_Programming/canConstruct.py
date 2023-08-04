def canConstruct(string,arr,dp):
    if string == "":
        return True
    elif string in dp:
        return dp[string]
    for s in arr:
        if string.startswith(s):
            newstring = string[len(s)::]
            if canConstruct(newstring,arr,dp):
                dp[string] = True
                return True
            else:
                continue
    
    dp[string] = False
    return False

arr = ["ab","abc","cd","def","abcd"]
target = "abcdef"
dp = {}
print(canConstruct(target,arr,dp))