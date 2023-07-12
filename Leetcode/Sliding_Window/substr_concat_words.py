class Solution:

    def __init__(self):
        self.globalhash = {}

    def checkstring(self,substr,words,wordtarget):
        
        arr = []

        for i in range(0,len(substr),wordtarget):
            arr.append(substr[i:i+wordtarget])
        
        localhash = self.globalhash.copy()
        
        for element in arr:
            if localhash.get(element,0) >= 1:
                localhash[element] -=1
            else:
                return False
        
        return True

    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        arr = []

        start = 0
        end = 0

        n = len(s)

        for word in words:
            self.globalhash[word] = self.globalhash.get(word,0)+1

        targetlength = len(words[0])*len(words)
        wordtarget = len(words[0])

        substring = ""
        currlength = 0

        for end in range(n):
            substring+=s[end]
            currlength+=1
            
            if currlength > targetlength:
                while currlength > targetlength and start<=end:
                    substring = substring[1:]
                    start+=1
                    currlength-=1
            
            if currlength == targetlength:
                # function to check if the substr is a permutation
                if self.checkstring(substring,words,wordtarget):
                    arr.append(start)
        
        return arr

            