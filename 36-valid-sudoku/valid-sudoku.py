class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = [set() for i in range(9)]
        c = [set() for i in range(9)]

        rc = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                curr = board[i][j]
                rc_str = str(i//3)+str(j//3)

                if (curr in r[i]) or (curr in c[j]) or (rc_str in rc and curr in rc[rc_str]):
                    return(False)
                
                r[i].add(curr)
                c[j].add(curr)
                rc[rc_str] = rc.get(rc_str, set()) | set(curr)
        
        return(True)