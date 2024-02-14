from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count1 = Counter(s)
        char_count2 = Counter(t)
        return(char_count1 == char_count2)
