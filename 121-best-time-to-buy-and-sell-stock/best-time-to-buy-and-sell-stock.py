class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left_min = [float('inf') for i in range(n)]
        left_min[0] = prices[0]
        right_max = [-float('inf') for i in range(n)]
        right_max[-1] = prices[-1]
        ans = -float('inf')
        for i in range(1,n):
            left_min[i] = min(left_min[i-1], prices[i])
            right_max[n-i-1] = max(right_max[n-i], prices[n-i-1])
        for i in range(n):
            ans = max(ans, right_max[i]-left_min[i])
        return(ans)