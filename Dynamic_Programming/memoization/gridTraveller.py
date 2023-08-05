def gridTraveller(i,j,n,m,dp):
    if i == m and j == n:
        return 1
    elif i > m or j > n:
        return 0
    elif dp[i-1][j-1] != -1:
        return dp[i-1][j-1]
    else:
        dp[i-1][j-1] = gridTraveller(i+1,j,n,m,dp) + gridTraveller(i,j+1,n,m,dp)
        return dp[i-1][j-1]

if __name__=="__main__":

    # M is rows and N is columns

    N,M = [3,3]

    dp = [[-1]*N for i in range(M)]

    print("The no of ways to reach the end is: ",gridTraveller(1,1,N,M,dp))