class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda k:k[0])

        newintervals = [intervals[0]]

        prev = newintervals[0]

        n = len(intervals)

        for i in range(1,n):

            curr = intervals[i]
            
            if prev[1] >= curr[0]:
                prev[1] = max(prev[1],curr[1])
            else:
                newintervals.append(curr)
                prev = curr
            
        return newintervals
