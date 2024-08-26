class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(len(s)):
            if not dp[i]:
                continue
            for j in range(len(wordDict)):
                if i+len(wordDict[j])<=len(s) and s[i:i+len(wordDict[j])]==wordDict[j]:
                    dp[i+len(wordDict[j])] = True
        
        return(dp[-1])
