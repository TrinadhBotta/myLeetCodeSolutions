from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat[0])
        m = len(mat)
        dis = [[0 if mat[i][j] == 0 else float('inf') for j in range(n)] for i in range(m)]
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
        
        dr = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            ci,cj,cd = queue.popleft()
            for (i,j) in dr:
                x = ci+i
                y = cj+j
                if m>x>-1 and n>y>-1 and dis[x][y]>cd+1:
                    queue.append((x,y,cd+1))
                    dis[x][y]=cd+1
        return(dis)
                    