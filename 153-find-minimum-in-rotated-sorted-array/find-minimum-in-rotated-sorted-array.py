class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            elif nums[l]<=nums[m]<=nums[r]:
                return(nums[l])
            else:
                r=m