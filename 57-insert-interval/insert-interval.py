class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        for i in range(len(intervals)):
            if newInterval[0]>intervals[i][1]:
                ans.append(intervals[i])
        if len(ans)==len(intervals):
            ans.append(newInterval)
            return(ans)
        
        start = newInterval[0]
        end = newInterval[1]
        check = True
        for i in range(len(ans),len(intervals)):
            if check:
                if intervals[i][0]>end:
                    ans.append([start,end])
                    ans.append(intervals[i])
                    check=False
                    continue
                start = min(intervals[i][0],start)
                end = max(intervals[i][1],end)
            else:
                ans.append(intervals[i])
        if check:
            ans.append([start,end])
        return(ans)