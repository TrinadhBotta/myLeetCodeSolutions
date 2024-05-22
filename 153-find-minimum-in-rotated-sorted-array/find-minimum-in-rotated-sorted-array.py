class Solution:
    def findMin(self, nums: List[int]) -> int:
        self.ans = nums[0]
        def rec(l,r):
            if l>=r:
                return()
            m=(l+r)//2
            if nums[m]>nums[m+1]:
                self.ans = nums[m+1]
            elif nums[m-1]>nums[m]:
                self.ans = nums[m]
            else:
                rec(l,m-1)
                rec(m+1,r)

        rec(0,len(nums)-1)
        return(self.ans)