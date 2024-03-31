class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        d={}
        ind = 0
        for i in range(len(strs)):
            s= ''.join(sorted(strs[i]))
            if s not in d:
                d[s]=ind
                ind+=1
                ans.append([])
            ans[d[s]]+=[strs[i]]
        return(ans)