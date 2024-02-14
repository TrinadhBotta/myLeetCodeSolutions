class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_string = s.lower()
        my_final_string = ''.join(ch for ch in my_string if (ch.isalpha() or ch.isdigit()))
        print(my_final_string)
        return my_final_string == my_final_string[::-1]
        