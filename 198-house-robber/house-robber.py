class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return(max(nums))
        
        for i in range(2,len(nums)):
            x=nums[i]
            for j in range(i-1):
                x = max(x,nums[i]+nums[j])
            nums[i]=x
        return(max(nums))