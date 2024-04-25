class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        n=len(nums)
        i=0
        not_first_check = False
        while i<n:
            if not_first_check and nums[i]==nums[i-1]:
                i+=1
                continue
            not_first_check = True
            j=i+1
            k=n-1
            if nums[i]>0:
                break
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
            i+=1
        return(ans)