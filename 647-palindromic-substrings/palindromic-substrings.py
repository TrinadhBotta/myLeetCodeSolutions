class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for i in range(len(s)):
            ci,cj = i,i
            
            while ci>-1 and cj<len(s) and s[ci]==s[cj]:
                ans+=1
                ci-=1
                cj+=1
            
            ci,cj = i,i+1
            
            while ci>-1 and cj<len(s) and s[ci]==s[cj]:
                ans+=1
                ci-=1
                cj+=1
            
        return(ans)
