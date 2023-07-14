class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        start = 0
        end = 0

        currsum = 0
        maxavg = float('-inf')
        currlength = 0
        n = len(nums)
        for end in range(n):
            currsum+=nums[end]
            currlength+=1

            if currlength == k:
                avg = (currsum/k)

                if avg > maxavg:
                    maxavg = avg
                
                currsum-=nums[start]
                start+=1
                currlength-=1
        
        return maxavg