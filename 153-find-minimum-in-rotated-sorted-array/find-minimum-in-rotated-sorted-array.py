class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = 10000
        l = 0
        h = len(nums)-1
        while l<=h:
            m = (l+h)//2
            if nums[m]>=nums[h]:
                mn = nums[h]
                l = m+1
            else:
                h = m
        return(mn)

        