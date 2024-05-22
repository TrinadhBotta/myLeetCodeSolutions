class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]

        def rec(s,l):
            if len(l)==len(nums):
                ans.append(l)

            for i in range(len(nums)):
                if i not in s:
                    temp = s.copy()
                    temp.add(i)
                    rec(temp,l+[nums[i]])
        
        rec(set(),[])
        return(ans)
        