def ConstructCount(string,arr,dp):
    if string  == "":
        return 1
    elif string in dp:
        return dp[string]
        
    count = 0
    
    for sub in arr:
        
        if string.startswith(sub):
            newstring = string[len(sub)::]
            count+= ConstructCount(newstring,arr,dp)
    dp[string] = count
    return count

arr = ["purp","p","ur","le","purpl"]
target = "purple"
dp = {}
print(ConstructCount(target,arr,dp))