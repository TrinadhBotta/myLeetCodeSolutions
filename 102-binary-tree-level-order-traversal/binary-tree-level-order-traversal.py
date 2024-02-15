from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return([])
        ans=[[]]
        queue = deque([])
        queue.append((root,0))
        while queue:
            r,l = queue.popleft()
            if len(ans)<=l:
                ans.append([])
            ans[l].append(r.val)
            if r.left:
                queue.append((r.left,l+1))
            if r.right:
                queue.append((r.right,l+1))
        return(ans)
