from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        cnt = [[] for i in range(len(nums)+1)]

        for key in d:
            cnt[d[key]].append(key)
        
        ans = []

        for i in range(len(cnt)-1,-1,-1):
            for j in cnt[i]:
                if k>0:
                    ans.append(j)
                    k-=1
                else:
                    return(ans)
        
        return(ans)