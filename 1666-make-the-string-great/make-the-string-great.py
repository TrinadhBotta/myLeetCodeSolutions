class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        
        for i in s:
            if stack and abs(ord(stack[-1])-ord(i))==32:
                stack.pop()
            else:
                stack.append(i)
        return("" if len(stack)==0 else ''.join(stack))
