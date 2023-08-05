def gridTraveller(n,m):
    
    dp = [[0]*(n+1) for i in range(m+1)]
    
    dp[1][1] = 1

    for i in range(1,m+1):
        for j in range(1,n+1):
            if i+1 <= m:
                dp[i+1][j] += dp[i][j]
            if j+1 <= n:
                dp[i][j+1] += dp[i][j]
    
    return dp[m][n]

if __name__=="__main__":
    # m is the no of rows
    # n is the no of columns
    n,m = [3,3]
    print("The no of ways to travel the grid of n*m is: ",gridTraveller(n,m)) 