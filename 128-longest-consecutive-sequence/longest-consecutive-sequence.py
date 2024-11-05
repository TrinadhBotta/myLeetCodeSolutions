class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for i in nums:
            c = 1
            if i-1 not in s:
                while i+1 in s:
                    i+=1
                    c+=1
            ans = max(c,ans)
        
        return(ans)