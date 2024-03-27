class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return(sum([1 if 9<i<100 or 999 < i < 10000 or i == 100000 else 0 for i in nums]))