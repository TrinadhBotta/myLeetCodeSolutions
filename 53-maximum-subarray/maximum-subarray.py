class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        s=0
        for i in nums:
            s+=i
            ans=max(ans,s)
            if s<0:
                s=0
        return(ans)