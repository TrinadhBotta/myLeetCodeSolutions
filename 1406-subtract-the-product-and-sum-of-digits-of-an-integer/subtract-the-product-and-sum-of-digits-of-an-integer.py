class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l=[int(i) for i in str(n)]
        s=0
        p=1
        for i in l:
            s+=i
            p*=i
        return(p-s)