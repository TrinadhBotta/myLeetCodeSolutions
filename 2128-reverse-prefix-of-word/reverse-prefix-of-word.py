class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind = word.find(ch)
        return(word[:ind+1][::-1]+word[ind+1:] if ind!=-1 else word)