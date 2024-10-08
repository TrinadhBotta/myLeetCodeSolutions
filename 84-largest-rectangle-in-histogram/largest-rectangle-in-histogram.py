class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0,heights[0])]
        ans = max(heights)

        for i in range(1,len(heights)):
            start_idx = i
            while stack and stack[-1][1]>heights[i]:
                start_idx, hi = stack.pop()
                ans = max(ans, hi*(i-start_idx))
    
            stack.append((start_idx,heights[i]))
        
        for i in range(len(stack)):
            ans = max(ans, (len(heights)-stack[i][0])*stack[i][1])
        
        return(ans)