from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        count = [[] for i in range(len(nums)+1)]
        for i in d:
            count[d[i]].append(i)
        ans=[]
        for i in range(len(count)-1,0,-1):
            while len(count[i])>0 and k>0:
                ans.append(count[i].pop())
                k-=1
            if k==0:
                return(ans)
        