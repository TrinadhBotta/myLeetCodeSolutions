class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        sr_color = image[sr][sc]
        m = len(image)
        n = len(image[0])
        if sr_color == color:
            return(image)
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        stack = [(sr,sc)]
        seen = set()
        seen.add((sr,sc))
        
        while stack:
            ci, cj = stack.pop()
            image[ci][cj] = color
            for (i,j) in d:
                if m > ci+i >-1 and n > cj+j >-1 and image[ci+i][cj+j] == sr_color and (ci+i,cj+j) not in seen:
                    seen.add((ci+i,cj+j))
                    stack.append((ci+i,cj+j))
        return(image)