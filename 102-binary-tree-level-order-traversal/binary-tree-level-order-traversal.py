# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        ans.append([])
        
        q = deque([(root,0)])

        while q:
            r,l = q.popleft()
            if not r:
                continue
            if len(ans)<l+1:
                ans.append([])
            ans[-1].append(r.val)
            
            if r:
                q.append((r.left,l+1))
                q.append((r.right,l+1))
        
        return(ans)
