class Solution:

    def encode(self,arr):

        map = {}
        count = 0
        string = ""

        for i in arr:
            val = map.get(i,0.1)
            if val == 0.1:
                count+=1
                map[i] = count
            
            string+=str(map[i])
        
        return string

    def wordPattern(self, pattern: str, s: str) -> bool:

        encodeds = self.encode(s.split())
        encodedt = self.encode(pattern)

        return encodeds == encodedt
