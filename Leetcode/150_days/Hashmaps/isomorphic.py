class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        smap = {}

        scount = 0

        encodeds = ""

        for i in s:
            val = smap.get(i,0.1)

            if val == 0.1:
                scount+=1
                smap[i] = scount
            
            encodeds+=str(smap[i])
        
        smap.clear()

        scount = 0

        encodedt = ""

        for i in t:
            val = smap.get(i,0.1)

            if val == 0.1:
                scount+=1
                smap[i] = scount
            
            encodedt+=str(smap[i])
        
        if encodeds == encodedt:
            return True
        else:
            return False