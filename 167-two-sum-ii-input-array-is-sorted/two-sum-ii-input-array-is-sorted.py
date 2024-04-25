class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            if target-numbers[i] in d:
                return([d[target-numbers[i]],i+1])
            d[numbers[i]]=i+1
        





