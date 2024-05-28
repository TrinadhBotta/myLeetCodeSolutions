class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            x = 0
            for j in range(i):
                if nums[i]>nums[j]:
                    x = max(x,dp[j])
            dp[i] = x+1
        
        return(max(dp))