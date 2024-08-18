class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rmax=[-float('inf')]
        n=len(prices)
        for i in range(len(prices)):
            rmax.append(max(rmax[-1],prices[n-i-1]))
        ans=0
        for i in range(n):
            ans=max(ans,rmax[n-i]-prices[i])
        return(ans)