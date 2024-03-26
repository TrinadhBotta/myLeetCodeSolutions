class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return(1)
        ans=50000
        d={}
        m=0
        for i in range(len(nums)):
            a = nums[i]
            if a not in d:
                d[a]=[i,0]
          
            d[a][1]+=1
            if d[a][1]>=m:
                if d[a][1]>m:
                    ans=50000
                m=d[a][1]
                ans=min(ans,i-d[a][0]+1)
        return(ans)