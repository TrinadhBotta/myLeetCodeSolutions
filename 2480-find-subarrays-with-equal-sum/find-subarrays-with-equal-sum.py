class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s=set()
        for i in range(len(nums)-1):
            a = nums[i]+nums[i+1]
            if a in s:
                return(True)
            s.add(a)
        return(False)