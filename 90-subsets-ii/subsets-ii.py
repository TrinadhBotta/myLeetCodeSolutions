class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        u = set()

        def rec(l,s, start):
            if s not in u:
                ans.append(l)
                u.add(s)
            
            for i in range(start, len(nums)):
                rec(l+[nums[i]],s+str(nums[i]), i+1)
            
            return
        
        rec([],'',0)
        return(ans)
        
        