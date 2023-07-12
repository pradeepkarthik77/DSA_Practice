class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:

#         value = float('inf')

#         count = 0

#         n = len(nums)

#         for i in range(n):
#             if nums[i] == val:
#                 count+=1
#                 nums[i] = value
        
#         nums.sort()
#         return (n-count)