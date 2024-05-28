class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans=1
        count = {}
        l = 0
        r = 0
        count[s[r]]=count.get(s[r],0)+1


        while r<len(s):
            if (r-l+1) - max(count.values())<=k:
                ans=max(ans,r-l+1)
                r+=1
                if r<len(s):
                    count[s[r]]=count.get(s[r],0)+1
            else:
                count[s[l]]-=1
                l+=1
        return(ans)