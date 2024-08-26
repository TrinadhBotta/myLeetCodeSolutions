class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i]>buy:
                ans = max(ans, prices[i]-buy)
            elif prices[i]<buy:
                buy = prices[i]
        
        return(ans)