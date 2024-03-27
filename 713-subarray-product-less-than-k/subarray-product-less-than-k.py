class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        pre = [1]
        ans=0
        for i in nums:
            if i<k:
                ans+=1
            pre.append(pre[-1]*i)
        if pre[-1]<k:
            return((len(nums)*(len(nums)+1))//2)

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if pre[j+1]//pre[i] >=k:
                    break
                ans+=1
        
        return(ans)
