class Solution:
    def isPalindrome(self, s: str) -> bool:

        newstr = ""

        for i in s:
            if i.isalnum():
                newstr+=i
        
        newstr = newstr.lower()
        
        start = 0
        end = len(newstr)-1

        while start<end:
            if newstr[start] == newstr[end]:
                start+=1
                end-=1
            else:
                return False
        return True