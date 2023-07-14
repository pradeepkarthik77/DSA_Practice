# given a sorted array
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        i = 0
        j = n-1

        while i<j:
            sum = nums[i]+nums[j]
            if sum == target:
                return [i,j]
            elif sum > target:
                j-=1
            else:
                i+=1
        
        return [-1,-1]