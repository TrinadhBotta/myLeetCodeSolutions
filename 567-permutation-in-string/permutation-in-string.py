class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            print('hoiio')
            return(False)
        d = {}
        e = {}
        for i in range(len(s1)):
            d[s1[i]]=d.get(s1[i],0)+1
            e[s2[i]]=e.get(s2[i],0)+1
        
        if d==e:
            return(True)
        
        for i in range(len(s1),len(s2)):
            e[s2[i]]=e.get(s2[i],0)+1
            e[s2[i-len(s1)]]=e.get(s2[i-len(s1)],0)-1
            if e[s2[i-len(s1)]]==0:
                del e[s2[i-len(s1)]]
            if d==e:
                return(True)
        return(False)
        

