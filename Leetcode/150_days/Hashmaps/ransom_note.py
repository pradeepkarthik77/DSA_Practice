class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
         
        maghash = {}

        for i in magazine:
            maghash[i] = maghash.get(i,0)+1
        
        ranhash = {}

        for i in ransomNote:
            ranhash[i] = ranhash.get(i,0)+1
        
        for key,val in ranhash.items():
            if val <= maghash.get(key,0):
                continue
            else:
                return False
        
        return True