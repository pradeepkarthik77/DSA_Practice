class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = 0
        k = 0

        n = len(nums)

        while j<n:

            if nums[j]!=nums[i]:
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
                k+=1

            j+=1
        return i+1


