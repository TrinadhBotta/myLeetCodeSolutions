class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        def compute(n):
            return((n*(n+1)//2)%1000000007)
        
        ans = 0
        c = 0
        for i in range(len(s)):
            if s[i]=='1':
                c+=1
            else:
                ans+=compute(c)
                c = 0
        ans+=compute(c)
        return(ans)
