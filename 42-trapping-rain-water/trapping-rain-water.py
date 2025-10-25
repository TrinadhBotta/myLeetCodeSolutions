class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [0 for i in height]
        rmax = [0 for i in height]

        for i in range(1, len(height)):
            lmax[i] = max(lmax[i-1], height[i-1])
            rmax[len(height)-1-i] = max(rmax[len(height)-i], height[len(height)-i])
        
        ans = 0

        for i in range(len(height)):
            ans+=max(0, min(lmax[i],rmax[i])-height[i])
        
        return(ans)