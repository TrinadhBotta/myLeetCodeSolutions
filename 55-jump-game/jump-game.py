class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return(True)
        curr = len(nums)-1
        upd = None
        while curr!=0:
            if curr == upd:
                return(False)
            pos = 0
            if upd!=None:
                curr = upd
            while pos<curr:
                if nums[pos]>=curr-pos:
                    upd = pos
                    break
                pos+=1
            if upd==None:
                return(False)
        return(True)
