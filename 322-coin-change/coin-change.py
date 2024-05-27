class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [100000]*(amount+1)
        dp[0] = 0
        for i in coins:
            if i>amount:
                continue
            dp[i] = 1
        
        for i in range(1,amount+1):
            for j in coins:
                if i-j<0:
                    continue
                dp[i] = min(dp[i], dp[i-j]+1)
        
        return(dp[-1] if dp[-1]!=100000 else -1)
                
        