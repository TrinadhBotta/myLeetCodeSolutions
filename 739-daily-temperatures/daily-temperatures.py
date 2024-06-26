class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0],0)]
        ans = [0]*len(temperatures)
        for i in range(1, len(temperatures)):
            while stack and temperatures[i]>stack[-1][0]:
                ans[stack[-1][1]] = i-stack[-1][1]
                stack.pop()
            stack.append((temperatures[i],i))
        return(ans)