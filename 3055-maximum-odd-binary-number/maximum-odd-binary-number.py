class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ans=''
        zeros = s.count('0')
        ones = len(s)-zeros
        ans+=((ones-1)*'1') + (zeros*'0') + '1'
        return(ans)
