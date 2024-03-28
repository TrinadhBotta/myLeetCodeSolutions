from collections import deque
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d={}
        n=len(nums)
        ans=min(n,k)
        m={}
        s=0
        for i in range(n):
            v = nums[i]
            if nums[i] not in d:
                d[v]={}
                d[v][1]=i
                m[v]=1
            else:
                d[v][m[v]+1]=i
                m[v]+=1

            if m[v]>k:
                s=max(s,d[v][m[v]-k]+1)
            ans=max(ans, i-s+1)
        return(ans)