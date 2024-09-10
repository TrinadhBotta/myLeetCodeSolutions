import heapq

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return(False)
        elif groupSize == 1:
            return(True)
        
        heapq.heapify(hand)
        
        for i in range(len(hand)//groupSize):
            j=1
            cur = heapq.heappop(hand)
            l = []
            while j<groupSize and hand:
                nex = heapq.heappop(hand)
                print(i,j,nex)
                if nex > cur+1:
                    return(False)
                elif nex == cur:
                    l.append(nex)
                else:
                    print(i,j,nex,'hi')
                    j+=1
                    cur = nex
            if l:
                for k in l:
                    heapq.heappush(hand,k)
            if j!=groupSize:
                return(False)
        return(True)
        


