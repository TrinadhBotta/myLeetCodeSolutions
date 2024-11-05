class Solution:
    def trap(self, nums: List[int]) -> int:
        lm = [0]*len(nums)
        rm = [0]*len(nums)
        ans = 0

        for i in range(len(nums)-1):
            lm[i+1] = max(lm[i],nums[i])
            rm[-i-2] = max(rm[len(nums)-i-1], nums[-i-1])
        
        for i in range(len(nums)):
            ans+= max(0, min(lm[i],rm[i])-nums[i] )
        
        return(ans)
