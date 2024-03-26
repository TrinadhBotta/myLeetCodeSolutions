class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in nums:
            if i>=a:
                b=a
                a=i
            elif i>b:
                b=i
        return((a-1)*(b-1))