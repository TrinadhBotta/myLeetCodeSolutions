class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==1 or len(nums)==0:
            return(nums)
        ans = [1 for i in nums]
        for i in range(len(nums)-1):
            ans[i+1] = nums[i]*ans[i]
        
        suff = 1
        for i in range(len(nums)-1,0,-1):
            suff = suff*nums[i]
            ans[i-1] = ans[i-1]*suff
        
        return(ans)