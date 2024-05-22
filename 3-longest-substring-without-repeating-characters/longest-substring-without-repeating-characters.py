class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return(len(s))
        
        start, ans, c = 0,0,0
        d = {}
        for i in range(len(s)):
            if s[i] not in d or d[s[i]]<start:
                c+=1
                ans=max(ans,c)
            else:
                start = d[s[i]]+1
                c = i-start+1
            d[s[i]]=i
        return(ans)