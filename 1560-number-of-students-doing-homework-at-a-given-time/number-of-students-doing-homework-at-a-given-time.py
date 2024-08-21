class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        ans = 0
        for i in range(len(startTime)):
            if startTime[i]<=queryTime and endTime[i]>=queryTime:
                ans+=1
        
        return(ans)
        