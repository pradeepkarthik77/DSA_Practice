class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        from collections import defaultdict
        
        map = defaultdict(list)

        n = len(nums)

        for i in range(n):
            if map[nums[i]] == []:
                map[nums[i]].append(i)

            else:
                temp = map[nums[i]].copy()
                for j in map[nums[i]]:
                    if abs(i-j) <= k:
                        return True
                    else:
                        temp.append(i)
                else:
                    map[nums[i]] = temp
        # print(map
        return False