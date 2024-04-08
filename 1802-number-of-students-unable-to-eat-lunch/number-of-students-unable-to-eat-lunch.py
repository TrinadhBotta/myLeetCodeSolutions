from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ans=len(students)
        zero = students.count(0)
        one = ans-zero
        for i in sandwiches:
            if i==0:
                if zero == 0:
                    return(ans)
                zero-=1
            else:
                if one == 0:
                    return(ans)
                one-=1
            ans-=1
        return(0)