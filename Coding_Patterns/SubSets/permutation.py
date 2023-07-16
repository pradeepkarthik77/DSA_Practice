class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        subsets = [[]]

        for elem in nums:

            i = 0

            curr = []

            n = len(subsets)

            while i<n:

                subset = subsets[i]

                m = len(subset)+1

                for j in range(m):
                    subs = subset.copy()
                    subs.insert(j,elem)
                    curr.append(subs)
            
                i+=1
            subsets = curr.copy()
        
        return subsets
                

            