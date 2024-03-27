class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i]<0:
                nums[i]=0

        
        for i in nums:
            if abs(i)>n or i==0:
                continue
            i=abs(i)
            if nums[i-1]==0:
                nums[i-1]=-(n+1)
            elif nums[i-1]>0:
                nums[i-1]=-nums[i-1]
    
        
        for i in range(n):
            if nums[i]>=0:
                return(i+1)
        return(n+1)
