class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join([i.lower() if i.isalnum() else '' for i in s])
        return(st==st[::-1])