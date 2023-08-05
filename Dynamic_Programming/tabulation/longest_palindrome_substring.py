class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        dp = [[""]*(n) for i in range(n)]

        maxstr = ""

        for i in range(n):
            dp[i][i] = s[i]
            maxstr = dp[i][i]

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if (dp[i+1][j-1] !="") or (dp[i+1][j-1] == "" and abs(i-j) == 1):
                            dp[i][j] = s[i]+dp[i+1][j-1]+s[j]
                    if len(dp[i][j]) > len(maxstr):
                        maxstr = dp[i][j]
                else:
                    dp[i][j] = ""
        return maxstr