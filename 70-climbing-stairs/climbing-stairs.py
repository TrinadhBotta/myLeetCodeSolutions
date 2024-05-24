class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 or n==2:
            return(n)
        a=1
        b=2
        while n>2:
            n-=1
            t=b
            b=b+a
            a=t
        return(b)