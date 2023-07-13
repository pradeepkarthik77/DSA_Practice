class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i in range(len(nums)):
            if map.get(nums[i],0.1)==0.1:
                map[target-nums[i]] = i
            else:
                return [i,map[nums[i]]]
        
        return []
            
        