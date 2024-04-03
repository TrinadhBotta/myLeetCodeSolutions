class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check1 = {}
        check2 = {}
        for i in range(len(s)):
            if s[i] not in check1 and t[i] not in check2:
                check1[s[i]]=i
                check2[t[i]]=i
            elif s[i] in check1 and t[i] in check2:
                if check1[s[i]]!=check2[t[i]]:
                    return(False)
            else:
                return(False)
        return(True)