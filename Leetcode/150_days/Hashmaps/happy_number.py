class Solution:
    def isHappy(self, n: int) -> bool:

        hashmap = {}

        while n != 1:

            string = str(n)

            summer = 0

            for i in string:
                summer += int(i)**2
            
            n = summer

            if hashmap.get(n,-1)!=-1:
                return False
            
            hashmap[n] = True
        
        return True