class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]
        for i in range(len(nums)-1):
            ans.append(ans[-1]*nums[i])
        post = 1
        for i in range(len(nums)-1,0,-1):
            post = post*nums[i]
            ans[i-1]*=post
        return(ans)