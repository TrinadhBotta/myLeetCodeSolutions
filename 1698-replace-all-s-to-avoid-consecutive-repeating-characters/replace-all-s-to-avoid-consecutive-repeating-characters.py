class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=''
        prev=''
        nex =''
        for i in range(len(s)):
            if s[i]!='?':
                ans+=s[i]
                prev=ans[-1]
                continue
            if i==len(s)-1:
                nex = ''
            else:
                nex = s[i+1]
            
            if prev!='a' and nex!='a':
                ans+='a'
            elif prev!='b' and nex!='b':
                ans+='b'
            else:
                ans+='c'
            prev=ans[-1]
        return(ans)