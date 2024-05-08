class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return(0)
        i=0
        j=1
        ans = max(0, prices[1]-prices[0])

        while j<len(prices):
            if prices[j]>prices[i]:
                ans = max(ans, prices[j]-prices[i])
                j+=1
            else:
                i=j
                j+=1
        return(ans)