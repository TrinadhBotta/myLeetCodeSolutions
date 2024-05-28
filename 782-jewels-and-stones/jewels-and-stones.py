class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        s=set([char for char in jewels])
        ans=0
        for i in stones:
            if i in s:
                ans+=1
        return(ans)