class Solution:
    def insert(self, intervals: List[List[int]], newInter: List[int]) -> List[List[int]]:
        intervals.append(newInter)
        intervals.sort()
        if len(intervals)<=1:
            return(intervals)
        newInterval = [intervals[0]]
        for i in range(1,len(intervals)):
            if newInterval[-1][1] >=  intervals[i][0]:
                if intervals[i][1]> newInterval[-1][1]:
                    newInterval[-1][1] = intervals[i][1]
            else:
                newInterval.append(intervals[i])
        return(newInterval)
