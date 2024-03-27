class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        a=set(nums1)
        b=set(nums2)
        ans=100
        for i in a:
            if i in b:
                ans=min(ans,i)
        if ans!=100:
            return(ans)
        m1=min(nums1)
        m2=min(nums2)
        s=str(m1)+str(m2) if m1<m2 else str(m2)+str(m1)
        return(int(s))