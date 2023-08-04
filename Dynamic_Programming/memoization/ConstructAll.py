import copy

def ConstructAll(string,arr,dp):
    
    if string == "":
        return [[]]
    
    if string in dp:
        return dp[string]
    
    total = []
    
    for i in arr:
        
        if string.startswith(i):
            newstring = string[len(i)::]
            val = ConstructAll(newstring,arr,dp)
            
            newarr = copy.deepcopy(val)
            
            for new in newarr:
                new.insert(0,i)
                total.append(new)
    
    dp[string] = total
    return total


arr = ["purp","p","ur","le","purpl"]
target = "purple"
dp = {}
print(ConstructAll(target,arr,dp))


