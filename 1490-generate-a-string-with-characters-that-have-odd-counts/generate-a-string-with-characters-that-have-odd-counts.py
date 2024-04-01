class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            return('s'*(n-1)+'a')
        return('s'*n)