from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        ans=[]
        l = [[] for i in nums]
        
        for i in d:
            l[d[i]-1].append(i)
        
        for i in range(len(l)-1,-1,-1):
            for j in range(len(l[i])):
                k-=1
                ans.append(l[i][j])
                if k==0:
                    return(ans)
        