class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        i = 0
        j = n-1

        arr = []

        while i<=j:
            val1 = nums[i]**2
            val2 = nums[j]**2

            if val1>val2:
                arr.append(val1)
                i+=1
            else:
                arr.append(val2)
                j-=1
        
        return arr[::-1]
