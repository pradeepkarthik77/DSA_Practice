class Solution:
    
    def lengthOfLongestSubstring(self, arr: str) -> int:

        hashmap = {}

        maxlength = 0

        currlength = 0

        start = 0
        end = 0
        n = len(arr)

        for end in range(n):
            hashmap[arr[end]] = hashmap.get(arr[end],0)+1
            currlength+=1

            if hashmap.get(arr[end],0)>1:
                while hashmap.get(arr[end],0)>1 and start<=end:
                    hashmap[arr[start]] = hashmap.get(arr[start],0)-1
                    currlength-=1
                    start+=1
            
            if currlength > maxlength:
                maxlength = currlength
        
        return maxlength

        

            