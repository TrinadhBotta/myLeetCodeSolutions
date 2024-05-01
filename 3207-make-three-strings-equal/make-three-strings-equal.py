class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        try:
            if s1[0]!=s2[0] or s2[0]!=s3[0]:
                return(-1)
        except:
            pass
        ans=0
        n=min(len(s1),len(s2),len(s3))
        total = len(s1)+len(s2)+len(s3)
        
        for i in range(n):
            if s1[i]!=s2[i] or s2[i]!=s3[i]:
                return(total-(ans*3))
            ans+=1
        return(total-(ans*3))

        