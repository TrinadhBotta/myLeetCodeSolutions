class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')', '{':'}', '[':']'}
        stack = []
        for i in range(len(s)):
            if s[i] in d:
                stack.append(s[i])
            elif len(stack)>0 and d[stack[-1]]==s[i]:
                stack.pop()
            else:
                return(False)
        if len(stack)==0:
            return(True)
        return(False)
        