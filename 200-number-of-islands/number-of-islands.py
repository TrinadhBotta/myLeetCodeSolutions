class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ones = []
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    ones.append((i,j))
        
        if len(ones)==0:
            return(0)
        
        di = [[0,1],[0,-1],[1,0],[-1,0]]
        m,n = len(grid), len(grid[0])
        ans=0

        while len(ones)>0:
            ci,cj = ones.pop()
            if (ci,cj) in seen:
                continue
            ans+=1
            stack = [(ci,cj)]
            seen.add((ci,cj))
            while stack:
                ci, cj = stack.pop()
                for i, j in di:
                    ti,tj = ci+i, cj+j
                    if -1<ti<m and -1<tj<n and (ti,tj) not in seen and grid[ti][tj]=="1":
                        stack.append((ti,tj))
                        seen.add((ti,tj))
        
        return(ans)