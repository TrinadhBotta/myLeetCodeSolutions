class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=set()
        nums.sort()
        st = None
        for i in range(len(nums)):
            # if st == nums[i]:
            #     continue
            st = nums[i]
            j = i+1
            k = len(nums)-1
            tar = nums[i]
            while j<k:
                if tar+nums[j]+nums[k]==0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j+=1
                elif tar+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
        return(list(ans))                    