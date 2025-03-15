# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        if not root:
            return([])
        ans = []
        while q:
            for i in range(len(q)):
                r = q.popleft()
                val = r.val

                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            ans.append(val)
        return(ans)