class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        
        ans = []
        begin = 0
        curr = 0
        end = 0
        while curr<len(s):
            if d[s[curr]]>end:
                end = d[s[curr]]
            elif curr==end:
                ans.append(end-begin+1)
                begin = curr+1
                end = curr+1
            curr+=1   
        return(ans)