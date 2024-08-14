class Solution:
    def rec(self, s, o, c):
        if o==0 and c==0:
            self.ans.append(s)
            return
        if o>=1:
            self.rec(s+"(",o-1,c)
        if c>o:
            self.rec(s+")",o,c-1)
        return


    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.rec('',n,n)
        return(self.ans)