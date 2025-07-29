class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for i in text1] for j in text2]

        flag = False
        for i in range(len(dp)):
            if text1[0] == text2[i]:
                flag = True
            if flag:
                dp[i][0] = 1
        
        flag = False
        for i in range(len(dp[0])):
            if text1[i] == text2[0]:
                flag = True
            if flag:
                dp[0][i] = 1


        for i in range(1,len(text2)):
            for j in range(1,len(text1)):
                if text2[i]==text1[j]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j-1], dp[i-1][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return(dp[-1][-1])