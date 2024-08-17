import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def compute(k):
            s=0
            for i in piles:
                s+=math.ceil(i/k)
            print(s)
            return(True if s<=h else False)
        
        low = 1
        high = max(piles)

        ans = high
        while high>=low:
            mid = (low+high)//2
            if compute(mid):
                ans=mid
                high = mid-1
            else:
                low = mid+1
        
        return(ans)