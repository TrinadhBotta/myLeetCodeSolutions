class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        d={}
        c,ans,s=0,0,0
        max_num = max(nums)
        for i in range(n):
            if nums[i]!=max_num:
                continue
            c+=1
            d[c]=i
            if c>=k:
                right_side = n-i-1+1
                left_side = d[c-k+1]-s+1
                s=d[c-k+1]+1
                ans+=right_side*left_side
        return(ans)




            
