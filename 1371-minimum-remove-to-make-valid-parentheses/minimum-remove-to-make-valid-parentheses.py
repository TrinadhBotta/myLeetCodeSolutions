class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        a='('
        b=')'
        stack=[]
        
        for i in range(len(s)):
            if s[i]!=a and s[i]!=b:
                continue
            if stack and stack[-1][0]==a and s[i]==b:
                stack.pop()
            else:
                stack.append((s[i],i))
                
        
        ans=''
        del_set = set(i[1] for i in stack)
        for i in range(len(s)):
            if i not in del_set:
                ans+=s[i]

        return(ans)