from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return(False)
        d1 = Counter(s1)

        d2 = {}
        for i in range(len(s1)):
            d2[s2[i]] = d2.get(s2[i], 0)+1
        
        if d1==d2:
            return(True)

        print(d1,d2)
        for i in range(len(s1), len(s2)):
            d2[s2[i]] = d2.get(s2[i],0)+1
            d2[s2[i-len(s1)]] = d2.get(s2[i-len(s1)],0)-1
            if d2[s2[i-len(s1)]]==0:
                del d2[s2[i-len(s1)]]


            if d1==d2:
                return(True)
        
        return(False)