class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval.copy())

        n = len(intervals)

        i = n-2

        while i>=0 and intervals[i][0] > newInterval[0]:
            intervals[i+1] = intervals[i]
            i-=1
        
        intervals[i+1] = newInterval
        
        newarr = [intervals[0]]

        prev = newarr[0]

        for curr in intervals[1:]:

            if curr[0] <= prev[1]:
                prev[1] = max(curr[1],prev[1])
            else:
                newarr.append(curr)
                prev = curr
        
        return newarr