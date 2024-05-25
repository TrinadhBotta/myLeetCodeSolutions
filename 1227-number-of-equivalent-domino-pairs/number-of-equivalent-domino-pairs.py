class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        ans=0
        d={}
        for i in dominoes:
            a=min(i)
            b=max(i)
            if (a,b) in d:
                ans+=d[(a,b)]
            d[(a,b)] = d.get((a,b),0)+1
        
        return(ans)