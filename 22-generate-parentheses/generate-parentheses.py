class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def getParenthesis(cur, o, c):
            if o==0 and c==0:
                ans.append(cur)
                return
            
            if o>0:
                getParenthesis(cur+"(",o-1,c)
            
            if c>o:
                getParenthesis(cur+")",o,c-1)

            return

        getParenthesis("",n,n)
        return(ans)