class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_string = ''.join(str.lower(i) if i.isalnum() else '' for i in s)
        return(my_string==my_string[::-1])