import copy
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp={}
        dp[nums[0]] = 1
        dp[-nums[0]] = dp.get(-nums[0],0)+1

        for j in range(1,len(nums)):
            i = nums[j]
            keys = list(dp.keys())
            dp2 = {}
            for k in keys:
                dp2[k+i]= dp2.get(k+i,0) + dp[k]
                dp2[k-i]= dp2.get(k-i,0) + dp[k]
            dp = copy.deepcopy(dp2)
        
        return(dp[target] if target in dp else 0)


