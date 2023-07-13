class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        for i in s:
            map[i] = map.get(i,0)+1
        
        for i in t:
            if map.get(i,0.1)==0.1:
                return False
            else:
                map[i]-=1
        
        for key in map:
            if map[key] !=0:
                return False
        
        return True