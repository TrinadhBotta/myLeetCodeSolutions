class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = [1 for i in nums]
        rp = [1 for i in nums]

        n = len(nums)

        for i in range(1,len(nums)):
            lp[i] = lp[i-1]*nums[i-1]
            rp[n-i-1] = rp[n-i]*nums[n-i] 

        ans = [lp[i]*rp[i] for i in range(n)]
        return(ans)