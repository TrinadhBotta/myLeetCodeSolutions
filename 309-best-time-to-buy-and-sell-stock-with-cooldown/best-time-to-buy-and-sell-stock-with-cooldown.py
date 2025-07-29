from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(maxsize=1000)
        def dfs(i, state):
            if i >= len(prices):
               return 0

            cooldown = dfs(i + 1, state)
            if state=="canBuy":
                buy = dfs(i + 1, "canSell") - prices[i]
                return(max(buy, cooldown))
            else:
                sell = dfs(i + 2, "canBuy") + prices[i]
                return(max(sell, cooldown))

        return dfs(0, "canBuy")