class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return(n)
        
        a=1
        b=2
        while n>2:
            b,a = a+b, b
            n=n-1
        
        return(b)
