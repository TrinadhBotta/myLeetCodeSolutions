class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s=set()
        ans=-1
        for i in nums:
            if -i in s:
                ans=max(ans,abs(i))
            else:
                s.add(i)
        return(ans)