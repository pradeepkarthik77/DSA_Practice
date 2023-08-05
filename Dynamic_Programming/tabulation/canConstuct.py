def canConstruct(target,arr):
    dp = [0]*(len(target)+1)

    dp[0] = 1

    for i in range(len(target)+1):
        if dp[i] != 0:
            for elem in arr:
                if target[i::].startswith(elem):
                    if i+len(elem) <= len(target):
                        dp[i+len(elem)] += 1
    
    return dp[len(target)]

if __name__=="__main__":
    target = "abcdef"
    arr = ['ab','abc','cd','def','abcd','ef']

    print("The no of ways to construct the given target string from the array is:",canConstruct(target,arr))