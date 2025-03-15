class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs2 = [''.join(sorted(i)) for i in strs]
        print(strs2)
        d={}
        ans=[]
        for i in range(len(strs)):
            if strs2[i] in d:
                ans[d[strs2[i]]].append(strs[i])
            else:
                ans.append([strs[i]])
                d[strs2[i]]=len(ans)-1
        return(ans)