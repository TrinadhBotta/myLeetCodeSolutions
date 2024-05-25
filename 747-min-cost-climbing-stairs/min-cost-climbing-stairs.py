class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)==2:
            return(min(cost))
        a, b = 0, 0
        j = 1

        while j<len(cost):
            t = b
            b = min(a+cost[j-1],b+cost[j])
            a = t
            j+= 1
        
        return(b)
