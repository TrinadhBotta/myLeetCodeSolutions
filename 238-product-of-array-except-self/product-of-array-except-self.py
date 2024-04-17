class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]
        pre = 1
        for i in range(len(nums)-1):
            pre = pre*nums[i]
            ans.append(pre)
        post = 1
        for i in range(len(nums)-1,0,-1):
            post = post*nums[i]
            ans[i-1]*=post
        return(ans)