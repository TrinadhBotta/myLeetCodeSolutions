class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = [1 for i in nums]
        rp = [1 for i in nums]

        for i in range(len(nums)-1):
            lp[i+1] = lp[i]*nums[i]
            rp[len(nums)-i-2] = rp[len(nums)-i-1]*nums[len(nums)-i-1]
        
        ans=[lp[i]*rp[i] for i in range(len(nums))]
        return(ans)