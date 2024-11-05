class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        w = len(height)-1
        i, j = 0, len(height)-1

        while i<j:
            ans = max(ans, min(height[i], height[j])*w)
            w-=1
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        
        return(ans)