class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hashmap = {}

        n = len(s)
        m = len(t)

        for i in t:
            hashmap[i] = hashmap.get(i,0)+1
        
        start = 0
        end = 0

        hitcount = 0
        minlength = float('inf')
        currlength = 0

        currstr = ""
        minstr = ""

        while end < n:
            currstr+=s[end]
            currlength+=1

            val = hashmap.get(s[end],0.1)

            if val != 0.1:

                hashmap[s[end]]-=1

                if hashmap[s[end]] > -1:
                    hitcount+=1
            
            if hitcount == m:

                if currlength < minlength:
                    minlength = currlength
                    minstr = currstr

                while hitcount == m and start<=end:

                    val = hashmap.get(s[start],0.1)

                    if val!=0.1:
                        hashmap[s[start]]+=1

                        if hashmap[s[start]]>0:
                            hitcount -=1

                    currstr = currstr[1:]
                    currlength-=1
                    start+=1

                    if hitcount == m:
                        if minlength > currlength:
                            minlength = currlength
                            minstr = currstr
                
            end+=1
        
        return minstr

