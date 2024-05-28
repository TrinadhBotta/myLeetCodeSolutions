class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_max_product(arr):
            if len(arr)==0:
                return(0)
            if len(arr)==1:
                return(arr[0])
            ans1 = 1
            ans2 = 1
            n = 0
            
            pro = 1
            for i in arr:
                if i<0:
                    n+=1
                pro*=i
            if n%2 == 0:
                return(pro)
            
            x=0
            for i in arr:
                if i<0:
                    x+=1
                    if x==n:
                        break
                ans1*=i
            
            x=0
            for i in arr:
                if i<0:
                    x+=1
                    if x==1:
                        continue
                if x<1:
                    continue
                ans2*=i
            
            return(max(ans1,ans2))
        
        s = 0
        ans=-float('inf')
        for i in range(len(nums)):
            if nums[i]==0:
                ans=max(ans,0,get_max_product(nums[s:i]))
                s=i+1
        if s!=len(nums):
            ans=max(ans,get_max_product(nums[s:]))
        return(ans)