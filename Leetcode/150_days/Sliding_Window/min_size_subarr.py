class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minlength = 10**6
        currlength = 0

        currsum = 0

        start = 0
        end = 0

        n = len(nums)

        while end<n:
            currsum += nums[end]
            currlength+=1

            if currsum >=target:
                while currsum >=target and start<=end:
                    if currlength < minlength:
                        minlength = currlength
                    currsum-=nums[start]
                    currlength-=1
                    start+=1
            
            end+=1

        if minlength == 10**6:
            return 0
        else:
            return minlength
