class Solution:

    def countsort(self,A):

        maxelement = max(A)

        newarr = [0]*(maxelement+1)

        for i in A:
            newarr[i] += 1
        
        for i in range(1,len(newarr)):
            newarr[i] += newarr[i-1]
        
        B = [0]*len(A)

        for i in range(len(A)-1,-1,-1):
            newarr[A[i]]-=1
            B[newarr[A[i]]] = A[i]
        
        return B

    def heightChecker(self, heights: List[int]) -> int:

        sortedarr = self.countsort(heights)

        count = 0

        for i in range(len(heights)):
            if heights[i] != sortedarr[i]:
                count+=1

        return count