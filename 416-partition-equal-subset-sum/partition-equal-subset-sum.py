from collections import Counter
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s%2==1:
            return(False)
        
        dp = set()
        dp.add(0)
        for i in nums:
            nex = set()
            for j in dp:
                nex.add(j+i)
                nex.add(j)
            dp = nex
        
        return(True if s//2 in dp else False)