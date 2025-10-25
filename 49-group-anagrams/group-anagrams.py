class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in strs:
            x = ''.join(sorted(i))
            d[x] = d.get(x, [])+[i]

        ans = []
        for k in d:
            ans.append(d[k])
        
        return(ans)