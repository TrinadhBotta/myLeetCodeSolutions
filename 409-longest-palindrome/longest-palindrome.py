from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        ans = 0
        odd = False
        for (i,j) in d.items():
            if j%2 == 0:
                ans+= j
            else:
                ans+= j-1
                odd = True
        if odd:
            ans+= 1
        return(ans)