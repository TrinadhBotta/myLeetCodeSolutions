class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ct = [Counter(word) for word in words]
        ans=''
        for i,j in ct[0].items():
            m=j
            check = True
            for k in range(1,len(words)):
                if i not in ct[k]:
                    check = False
                    break
                m=min(m,ct[k][i])
            if check:
                ans+=m*i
        return([i for i in ans])
                