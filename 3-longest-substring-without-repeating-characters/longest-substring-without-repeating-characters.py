class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        if len(s)==0:
            return(0)
        d[s[0]] = 0
        start, ans = 0, 1
        
        for i in range(1,len(s)):
            if s[i] in d and start<=d[s[i]]:
                start = d[s[i]]+1
            d[s[i]] = i
            ans = max(ans, i-start+1)
        return(ans)
            

        