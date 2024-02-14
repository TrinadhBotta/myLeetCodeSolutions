class Solution:
    def binary_check(self,l,h,target,arr):
        while h>=l:
            m = (l+h)//2
            if arr[m] == target:
                return(m)
            if arr[m]>target:
                h=m-1
            else:
                l=m+1
        return(-1)
    def search(self, nums: List[int], target: int) -> int:
        return(self.binary_check(0,len(nums)-1,target,nums))
