class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans=letters[0]
        t=ord(target)
        x=max(t,ord(ans))
        for i in range(1,len(letters)):
            y=ord(letters[i])
            if y>t and (y<x or t==x):
                x=y
                ans=letters[i]
        return(ans)