class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        removed = set()
        for i in range(len(s)):
            if stack and stack[-1][0]=="(" and s[i]==")":
                removed.add(stack[-1][1])
                removed.add(i)
                stack.pop()
            elif s[i]!="*":
                stack.append((s[i],i))
        
        if len(stack)==0:
            return(True)
        
        stack = []
        for i in range(len(s)):
            if i in removed:
                continue
            if stack and stack[-1]=="*" and s[i]==")":
                stack.pop()
            elif stack and stack[-1]=="(" and s[i]=="*":
                stack.pop()
            else:
                stack.append(s[i])
        
        return(False if "(" in stack or ")" in stack else True)