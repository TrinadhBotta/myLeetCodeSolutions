class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    stack.append((i,j))
        if len(stack)==0:
            return(0)
        ans = 0
        seen = set()
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        while stack:
            ci,cj = stack.pop()
            if (ci,cj) in seen:
                continue
            queue = [(ci,cj)]
            ans+=1
            while queue:
                ci,cj = queue.pop()
                seen.add((ci,cj))
                for (i,j) in d:
                    x = ci+i
                    y = cj+j
                    if -1<x<len(grid) and -1<y<len(grid[0]):
                        if grid[x][y]=="1" and (x,y) not in seen:
                            queue.append((x,y))
        return(ans)