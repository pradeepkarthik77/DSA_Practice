class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        dp = [[""]*(n) for i in range(n)]

        for i in range(n):
            dp[i][i] = s[i]

        for i in range(n-1,-1,-1)
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = s[i]+dp[i+1][j-1]+s[j]
                else:
                    if len(dp[i][j-1]) > len(dp[i+1][j]):
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = dp[i+1][j]

        return dp[0][n-1]