class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return(n)
        if n==2:
            return(2)
        a = 1
        b = 2
        while n>2:
            temp = b
            b = a+b
            a = temp
            n-=1
        return(b)
        