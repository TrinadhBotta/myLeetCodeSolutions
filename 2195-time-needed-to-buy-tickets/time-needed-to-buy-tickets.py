class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        shuffle = [(tickets[i],i) for i in range(len(tickets))]
        shuffle.sort()
        ans=0
        cur = 0 
        for i,j in shuffle:
            cur+=1
            if i<tickets[k] or (i<=tickets[k] and j<k):
                ans+=i
            elif j<=k:
                ans+=tickets[k]
            else:
                ans+=tickets[k]-1
        return(ans)