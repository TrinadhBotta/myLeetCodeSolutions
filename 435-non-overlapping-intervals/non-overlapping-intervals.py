class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        i=0
        j=1
        ans=0
        while j<len(intervals) and i<j:
            if intervals[j][0] < intervals[i][1]:
                ans+=1
                if intervals[j][1] < intervals[i][1]:
                    i=j
                j+=1
            else:
                i=j
                j+=1
        return(ans)