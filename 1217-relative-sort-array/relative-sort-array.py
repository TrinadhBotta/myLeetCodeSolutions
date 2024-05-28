from collections import Counter
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        c = Counter(arr1)
        c2 = Counter(arr2)
        left = []
        ans = []
        for i in arr2:
            if i in c:
                for j in range(c[i]):
                    ans.append(i)
        
        for i in arr1:
            if i not in c2:
                left.append(i)
        
        left.sort()
        ans.extend(left)

        return(ans)