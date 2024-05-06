class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return(len(nums))
        s = set(nums)
        ans=0
        for i in nums:
            #check if current number can be a start
            if i-1 not in s:
                c=1
                nex = i+1
                while nex in s:
                    c+=1
                    nex+=1
                ans=max(c,ans)
        return(ans)