# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1 
        h = n
        while h>=l:
            m = (h+l+1)//2
            if m == 1:
                break
            if isBadVersion(m):
                if not isBadVersion(m-1):
                    return(m)
                h=m-1
            else:
                l=m+1
        return(1)