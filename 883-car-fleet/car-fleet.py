class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position)==0:
            return(0)
        ans = 1

        time = [(position[i],(target-position[i])/speed[i]) for i in range(len(position))]
        time.sort()
    

        cur = time.pop()[1]
        while time:
            while time and cur>=time[-1][1]:
                time.pop()
            if time:
                cur = time.pop()[1]
                ans+=1
        
        return(ans)