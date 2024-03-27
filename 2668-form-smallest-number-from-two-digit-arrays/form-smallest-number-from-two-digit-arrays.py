class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = set(nums1).intersection(nums2)
        if intersection:
            return(min(intersection))
        return(min(nums1)*10+min(nums2) if min(nums1)<min(nums2) else min(nums2)*10+min(nums1))