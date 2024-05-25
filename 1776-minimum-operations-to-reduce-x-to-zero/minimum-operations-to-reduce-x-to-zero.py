class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums)
        if sum(nums)==x:
            return(n)
        elif sum(nums)<x:
            return(-1)

        ls = {}
        rs = {}
        ls[0], rs[0]=0,0

        val = 0
        for i in range(n):
            ls[i+1] = ls[i]+nums[i]
            val+=  nums[n-1-i]
            rs[val] = i+1
        
        ans = float('inf')
        for i in range(len(nums)+1):
            a = ls[i]
            if x-a in rs and i+rs[x-a]<n:
                ans = min(ans, i+rs[x-a])

        return(-1 if ans==float('inf') else ans)
