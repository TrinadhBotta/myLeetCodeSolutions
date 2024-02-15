class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x,y = points[i][0], points[i][1]
            d = (x**2) + (y**2)
            heap.append([d,x,y])
        heapq.heapify(heap)
        ans=[]
        while k>0:
            d,x,y = heapq.heappop(heap)
            ans.append([x,y])
            k-=1
        return(ans)