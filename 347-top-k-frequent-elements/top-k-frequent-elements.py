class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = Counter(nums)
        count = [[] for i in range(len(nums)+1)]
        for i in d:
            count[d[i]].append(i)
        ans=[]
        for i in range(len(count)-1,0,-1):
            for j in range(len(count[i])):
                ans.append(count[i][j])
                k-=1
                if k == 0:
                    return(ans)
        return(ans)
        