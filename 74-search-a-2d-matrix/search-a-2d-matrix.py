import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix)-1
        r = -1
        while l<=h:
            m = (l+h)//2
            if matrix[m][0]<=target and matrix[m][-1]>=target:
                r = m
                break
            elif matrix[m][0]>target:
                h=m-1
            else:
                l=m+1
        
        if r==-1:
            return(False)
        
        ind = bisect.bisect_left(matrix[r], target)
        return(True if matrix[r][ind]==target else False)