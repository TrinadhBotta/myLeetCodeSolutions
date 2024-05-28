class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans,l = s[0],1

        for i in range(len(s)):
            ci,cj = i,i
            
            while ci>-1 and cj<len(s) and s[ci]==s[cj]:
                if cj-ci+1>l:
                    ans = s[ci:cj+1]
                    l = cj-ci+1
                ci-=1
                cj+=1
            
            ci,cj = i,i+1
            
            while ci>-1 and cj<len(s) and s[ci]==s[cj]:
                if cj-ci+1>l:
                    ans = s[ci:cj+1]
                    l = cj-ci+1
                ci-=1
                cj+=1
            
        return(ans)
