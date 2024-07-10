class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [1]*n
        for i in range(m-1):
            for j in range(n):
                if j!=0:
                    l[j] = l[j-1] + l[j]
        
        return(l[-1])