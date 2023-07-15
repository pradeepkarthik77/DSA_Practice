from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        n = len(nums)

        answer = []

        for i in range(n):

            if i>0 and nums[i-1] == nums[i]:
                continue

            l,r = i+1,n-1

            while l<r:

                threeSum = nums[i]+nums[l]+nums[r]

                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    answer.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        
        return answer