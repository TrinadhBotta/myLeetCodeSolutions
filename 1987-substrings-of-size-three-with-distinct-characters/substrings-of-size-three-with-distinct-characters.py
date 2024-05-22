class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        if len(s)<3:
            return(0)
        d[s[0]]=d.get(s[0],0)+1
        d[s[1]]=d.get(s[1],0)+1
        d[s[2]]=d.get(s[2],0)+1

        ans = 1 if len(d)==3 else 0

        for i in range(3,len(s)):
            d[s[i]]=d.get(s[i],0)+1
            d[s[i-3]]-=1
            if d[s[i-3]]==0:
                del d[s[i-3]]
            if len(d)==3:
                ans+=1
        
        return(ans)
            

        