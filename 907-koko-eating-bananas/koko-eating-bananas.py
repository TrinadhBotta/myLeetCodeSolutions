import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(val):
            th = 0
            for i in piles:
                th+=math.ceil(i/val)
            if th<=h:
                return(True)
            return(False)
        
        l = 1
        hl = sum(piles)
        if hl<=h:
            return(1)

        while l<=hl:
            m = (l+hl)//2
            print(m,l,hl)
            if check(m):
                if not check(m-1):
                    return(m)
                hl=m-1
            else:
                l=m+1