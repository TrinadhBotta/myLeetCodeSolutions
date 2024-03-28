class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l = heights.copy()
        l.sort()
        return(sum([0 if l[i]==heights[i] else 1 for i in range(len(l))]))