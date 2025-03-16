class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1 for i in range(amount+1)]
        dp[0] = 0

        for i in coins:
            if i<len(dp):
                dp[i]=1
            for j in range(i, len(dp)):
                if dp[j-i]!=-1:
                    if dp[j]==-1:
                        dp[j] = dp[j-i]+1
                    else:
                        dp[j]=min(dp[j], dp[j-i]+1)
        
        return(dp[-1])