class Solution:
    def jump(self, nums: List[int]) -> int:

        def jumpUtil(indx,arr,dp):
            if indx == len(arr)-1:
                return 1
            elif indx >= len(arr):
                return float('inf')
            elif dp[indx] != -1:
                return dp[indx]
            else:
                mincount = float('inf')
                for i in range(1,nums[indx]+1):
                    count = jumpUtil(indx+i,arr,dp)+1
                    if count < mincount:
                        mincount = count
                dp[indx] = mincount
                return mincount
        
        dp = [-1]*len(nums)
        dp[len(nums)-1] = 1
        return jumpUtil(0,nums,dp)-1

