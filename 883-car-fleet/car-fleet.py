class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        
        pos_speed.sort()
        stack = []

        for i in range(len(position)):
            stack.append((target-pos_speed[i][0])/pos_speed[i][1])
        
        ans = 0
        while stack:
            cur = stack.pop()
            ans+=1
            while stack and stack[-1]<=cur:
                stack.pop()
        
        return(ans)