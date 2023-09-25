class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)

        dp = [float('inf')]*(amount+1)

        dp[0] = 0

        for i in range(amount+1):
            if dp[i] != float('inf'):
                for coin in coins:
                    sum = i+coin
                    if sum <= amount:
                        dp[sum] = min(dp[sum],1+dp[i])

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
