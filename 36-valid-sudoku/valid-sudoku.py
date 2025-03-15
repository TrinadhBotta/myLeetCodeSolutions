class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r = {}
        c = {}
        rc = {}

        for i in range(9):
            r[i] = set()
            c[i] = set()
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if (i//3,j//3) not in rc:
                    rc[(i//3,j//3)] = set()
                if val in r[i] or val in c[j] or val in rc[(i//3,j//3)]:
                    return(False)
                r[i].add(val)
                c[j].add(val)
                rc[(i//3,j//3)].add(val)

        return(True)
