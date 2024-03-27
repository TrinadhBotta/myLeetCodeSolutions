class Solution:
    def similarPairs(self, words: List[str]) -> int:
        s=[set(word) for word in words]
        c=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    c+=1
        return(c)