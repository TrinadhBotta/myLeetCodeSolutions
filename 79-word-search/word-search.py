class Solution:
    def cal(self, board, word, i,j, check):
        if len(word)==0:
            return(True)
        if (i==len(board) or i==-1) or (j==len(board[0]) or j==-1) or ((i,j) in check):
            return(False) 
        if word[0]!=board[i][j]:
            return(False)
        check.add((i,j))
        found = (self.cal(board, word[1:], i + 1, j, check.copy()) or
                 self.cal(board, word[1:], i - 1, j, check.copy()) or
                 self.cal(board, word[1:], i, j + 1, check.copy()) or
                 self.cal(board, word[1:], i, j - 1, check.copy()))
        return found
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and self.cal(board,word,i,j, set()):
                    return(True)
        return(False)
                
        