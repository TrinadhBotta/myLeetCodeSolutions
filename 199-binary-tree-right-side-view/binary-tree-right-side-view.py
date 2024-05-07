from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return([])
        q=deque([])
        q.append((root,1))
        ans=[]
        while q:
            r,l=q.popleft()
            if l>len(ans):
                ans.append(r.val)
            if r.right:
                q.append((r.right,l+1))
            if r.left:
                q.append((r.left,l+1))
        return(ans)
        