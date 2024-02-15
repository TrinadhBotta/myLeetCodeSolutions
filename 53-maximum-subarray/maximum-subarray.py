class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=max(nums)
        cur_sum = 0
        for i in nums:
            cur_sum+=i
            if cur_sum<0:
                cur_sum = 0
            else:
                ans=max(ans,cur_sum)
        return(ans)