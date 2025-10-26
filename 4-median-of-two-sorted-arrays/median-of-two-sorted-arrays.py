import bisect
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums2)<len(nums1):
            nums1, nums2 = nums2, nums1
        

        n, m = len(nums1), len(nums2)
        half = (n+m)//2
        
        l,r = 0, len(nums1)-1
        while True:
            i = (l+r)//2
            j = half-i-2
            
            Aleft = nums1[i] if i>=0 else float("-infinity")
            Aright = nums1[i+1] if i+1<n else float("infinity")
            Bleft = nums2[j] if j>=0 else float("-infinity")
            Bright = nums2[j+1] if j+1<m else float("infinity")

            if Bleft<=Aright and Aleft<=Bright:
                if (n+m)%2!=0:
                    return(min(Aright,Bright))
                else:
                    x = max(Aleft, Bleft)
                    y = min(Aright, Bright)
                    return((x+y)/2)
            
            if Aleft>Bright:
                r=i-1
            else:
                l=i+1
            