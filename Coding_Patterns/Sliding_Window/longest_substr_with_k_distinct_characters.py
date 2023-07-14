# Given a string, find the length of the longest substring in it with no more than K distinct characters.

#User function Template for python3
from collections import defaultdict
class Solution:

    def longestKSubstr(self, s, k):
        # code here
        hashmap = defaultdict(int)
        
        n = len(s)
        
        discount = 0
        
        end = 0
        start = 0
        
        maxlength = -1
        
        currlength = 0
        
        while end<n:
            
            if hashmap[s[end]] == 0:
                discount+=1
            
            hashmap[s[end]]+=1
            
            currlength+=1
            
            if discount == k:
                
                if currlength > maxlength:
                    maxlength = currlength
            
            elif discount > k:
                
                while discount > k and start<=end:
                    
                    hashmap[s[start]]-=1
                    currlength-=1
                    
                    if hashmap[s[start]] == 0:
                        discount-=1
                    
                    start+=1
            else:
                pass
            
            end+=1
        
        return maxlength
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends