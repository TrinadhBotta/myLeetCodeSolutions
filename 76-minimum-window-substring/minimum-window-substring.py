class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t2 = Counter(t)
        need, have, ans = len(t2), 0, s
        flag = False
        d,l = {}, 0

        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0)+1
            if d[s[i]]==t2[s[i]]:
                have+=1
            
            while need == have:
                flag = True
                ans = s[l:i+1] if len(s[l:i+1])<len(ans) else ans
                d[s[l]]-=1
                if d[s[l]]<t2[s[l]]:
                    have-=1
                l+=1

        
        return(ans if flag else "")