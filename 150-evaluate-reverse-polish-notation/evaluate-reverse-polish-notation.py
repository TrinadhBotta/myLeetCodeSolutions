from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = set(["+","-","*","/"])

        for i in tokens:
            if i in s:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(b-a)
                elif i == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(int(i))
        return(stack[0])
                