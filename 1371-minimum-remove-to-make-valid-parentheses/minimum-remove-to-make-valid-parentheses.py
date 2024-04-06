class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        a='('
        b=')'
        stack=[]
        del_set = set()
        for i in range(len(s)):
            if s[i]!=a and s[i]!=b:
                continue
            if stack and stack[-1][0]==a and s[i]==b:
                del_set.remove(stack[-1][1])
                stack.pop()
            else:
                stack.append((s[i],i))
                del_set.add(i)
        
        ans=''
        for i in range(len(s)):
            if i not in del_set:
                ans+=s[i]

        return(ans)