class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        l = len(set(nums))
        if l==1:
            return((len(nums)*(len(nums)+1))//2)

        for i in range(len(nums)-l+1):
            s = set([nums[i]])
            cur_len = 1
            for j in range(i+1, len(nums)):
                if nums[j] not in s:
                    s.add(nums[j])
                    cur_len+=1
                if cur_len == l:
                    ans+=1
                elif cur_len>l:
                    break
        
        return(ans)