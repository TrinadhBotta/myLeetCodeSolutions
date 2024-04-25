class Solution:
    def trap(self, nums: List[int]) -> int:
        l_max = [0]
        r_max = [0]*len(nums)
        for i in range(len(nums)-1):
            l_max.append(max(nums[i],l_max[-1]))
        for j in range(len(nums)-2,-1,-1):
            r_max[j]=max(r_max[j+1],nums[j+1])
        ans=0
        for i in range(len(nums)):
            ans+=max(0, min(l_max[i],r_max[i])-nums[i])
        return(ans)
