import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                ind = bisect.bisect_left(matrix[i], target)
                return(True if matrix[i][ind]==target else False)
        return(False)