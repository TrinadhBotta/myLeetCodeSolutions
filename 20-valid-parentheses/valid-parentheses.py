class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(":")", "{":"}", "[":"]"}
        
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if not stack or d[stack[-1]]!=i:
                    return(False)
                stack.pop()
        
        return(True if not stack else False)