from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dis = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        l = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    dis[i][j] = 1000
                elif grid[i][j]==2:
                    l.append((i,j))
        
        di = [[0,1],[0,-1],[1,0],[-1,0]]
        m,n = len(grid), len(grid[0])
        while l:
            ci,cj = l.pop()
            q = deque([(ci,cj,0)])
            while q:
                ci,cj,cd = q.popleft()

                for i,j in di:
                    ti,tj = ci+i, cj+j
                    if -1<ti<m and -1<tj<n and grid[ti][tj]==1 and cd+1<dis[ti][tj]:
                        q.append((ti,tj,cd+1))
                        dis[ti][tj]=cd+1
        ans = -1
        for i in dis:
            ans=max(ans,max(i))
        
        return(-1 if ans==1000 else ans)