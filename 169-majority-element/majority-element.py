class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        a = 0
        for i in nums:
            if c==0:
                a=i
                c=1
            elif a==i:
                c+=1
            else:
                c-=1
        return(a)