# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return([])
        q=deque([(root,1)])
        ans=[]
        while len(q)>0:
            r,l=q.popleft()
            if l>len(ans):
                ans.append([])
            ans[l-1].append(r.val)
            if r.left:
                q.append((r.left,l+1))
            if r.right:
                q.append((r.right,l+1))
        return(ans)