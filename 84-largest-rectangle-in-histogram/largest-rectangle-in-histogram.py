class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights)==1:
            return(heights[0])
        stack = [(heights[0],0)]
        ans = max(heights)
        
        for i in range(1,len(heights)):
            st = i
            while stack and stack[-1][0]>heights[i]:
                val, st = stack.pop()
                ans = max(ans, val*(i-st))
            stack.append((heights[i],st))
        
        for i in range(len(stack)):
            ans = max(ans, stack[i][0]*(len(heights)-stack[i][1]))
        
        return(ans)