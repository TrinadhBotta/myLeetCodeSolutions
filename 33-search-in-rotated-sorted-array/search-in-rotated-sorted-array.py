class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while h>=l:
            m = (l+h) // 2
            if nums[m]==target:
                return(m)

            if nums[m]>=nums[l]:
                if nums[m]>target>=nums[l]:
                    h=m-1
                else:
                    l=m+1
            else:
                if target>nums[m] and target<=nums[h]:
                    l=m+1
                else:
                    h=m-1
        return -1
        