class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def square(n):
            ans = 0
            while n:
                d = n%10
                ans+=d*d
                n = n//10
            return(ans)
        
        v = set()
        v.add(n)

        while n!=1:
            n=square(n)
            if n in v:
                return(False)
            v.add(n)
        
        return(True)