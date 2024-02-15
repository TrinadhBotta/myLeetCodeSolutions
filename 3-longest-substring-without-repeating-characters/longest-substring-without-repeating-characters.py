class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return(len(s))
        d = {}
        d[s[0]]=0
        ans = 1
        start = 0
        c = 1
        for i in range(1,len(s)):
            if s[i] not in d or d[s[i]]<start:
                c+=1
                ans=max(c,ans)
                d[s[i]] = i
            else:
                start = d[s[i]]+1
                c = i-start+1
                d[s[i]] = i
        return(ans)