import re
class Solution:
    def count_substrings(self,string, substring):
        string_size = len(string)
        substring_size = len(substring)
        count = 0
        for i in range(0,string_size-substring_size+1):
            if string[i:i+substring_size] == substring:
                count+=1
        return count
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        s=''
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                s+='0'
            elif nums[i]>nums[i-1]:
                s+='1'
            else:
                s+='2'
        
        t=''.join(['2' if i==-1 else str(i) for i in pattern])
        return(self.count_substrings(s,t))
