class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        d = [0]*(n+1)
        d[1] = 1
        num_people_know = 0
        
        x = 2
        while x<=n:
            val1 = d[x-delay] if x-delay>-1 else 0
            val2 = d[x-forget] if x-forget>-1 else 0
        
            num_people_know = (num_people_know+val1-val2)%1000000007
            d[x] = num_people_know
            x+=1
        return(sum(d[n-forget+1:])%1000000007)