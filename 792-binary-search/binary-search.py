class Solution(object):
    def binsearch(self,arr,val,l,h):
        m = (l+h)//2
        if l>h:
            return(-1)
        if arr[m] == val:
            return(m)
        
        if arr[m]<val:
            return(self.binsearch(arr,val,m+1,h))
        else:
            return(self.binsearch(arr,val,l,m-1))
    
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return(self.binsearch(nums,target,0,len(nums)-1))