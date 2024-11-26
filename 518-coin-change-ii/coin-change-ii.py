class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return(1)
        dp = [0]*(amount+1)
        
        for i in coins:
            if i > amount:
                continue
            dp[i]+=1
            for j in range(i+1, amount+1):
                dp[j]+= dp[j-i]
        
        return(dp[-1])
