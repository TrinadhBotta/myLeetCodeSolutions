class Solution:
    def rec(self, s, o, c,n):
        if n==0:
            if o==c:
                self.ans.append(s)
            return
        if o>c:
            self.rec(s+")",o,c+1,n-1)
        self.rec(s+"(",o+1,c,n-1)


    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.rec('(',1,0,2*n-1)
        return(self.ans)