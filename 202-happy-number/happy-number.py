class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def square(x):
            x = str(x)
            ans = 0
            for i in x:
                ans+=int(i)*int(i)
            return(ans)
        
        v = set()
        v.add(n)

        while n!=1:
            n=square(n)
            if n in v:
                return(False)
            v.add(n)
        
        return(True)