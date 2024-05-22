from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter((s1+' '+s2).split())
        ans=[]
        for i in c:
            if c[i]==1:
                ans.append(i)
        return(ans)