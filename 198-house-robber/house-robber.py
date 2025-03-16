class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return(nums[0])
        if len(nums)==2:
            return(max(nums))
        ans = [0]*len(nums)
        ans[0],ans[1] = nums[0],max(nums[0],nums[1])
        i=2
        while i<len(nums):
            ans[i]=max(ans[i-1],nums[i]+ans[i-2])
            i+=1
        return(ans[-1])