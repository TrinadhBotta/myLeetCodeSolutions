class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        l = []
        m,n = len(board), len(board[0])
        di = [[0,1], [0,-1], [1,0], [-1,0]]

        for i in [0,m-1]:
            for j in range(n):
                if board[i][j]=="O":
                    l.append((i,j))
        
        for i in range(m):
            for j in [0,n-1]:
                if board[i][j]=="O":
                    l.append((i,j))
        
        seen = set()
        while len(l)>0:
            ci,cj = l.pop()
            if (ci,cj) in seen:
                continue
            stack=[(ci,cj)]
            seen.add((ci,cj))
            while stack:
                ci,cj = stack.pop()
                for i,j in di:
                    ti,tj = ci+i, cj+j
                    if -1<ti<m and -1<tj<n and board[ti][tj]=="O" and (ti,tj) not in seen:
                        stack.append((ti,tj))
                        seen.add((ti,tj))
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in seen:
                    board[i][j]="X"
    
        return(board)

