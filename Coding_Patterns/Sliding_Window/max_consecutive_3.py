# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        
        n = len(arr)

        start = 0
        end = 0

        currlength = 0
        maxlength = 0

        zero = 0

        while end<n:
            if arr[end] == 0:
                zero+=1
            
            currlength+=1

            if zero == k:
                if currlength > maxlength:
                    maxlength = currlength
            elif zero>k:
                while zero>k and start<=end:
                    if arr[start] == 0:
                        zero-=1
                    currlength-=1
                    start+=1
            else:
                pass
            end+=1
        
        return maxlength