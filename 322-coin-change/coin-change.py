class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return(0)
        ans = [float('inf') for i in range(amount)]
        for i in coins:
            if i-1<len(ans):
                ans[i-1] = 1
        for i in range(amount):
            for j in coins:
                if i-j>=0:
                    ans[i]=min(ans[i],ans[i-j]+1)
        return(ans[-1] if ans[-1]!=float('inf') else -1)