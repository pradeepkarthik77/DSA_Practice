class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        answer = []
        answer.append([])

        for elem in nums:

            n = len(answer)

            for i in range(n):
                set = list(answer[i])
                set.append(elem)
                answer.append(set)
        
        return answer