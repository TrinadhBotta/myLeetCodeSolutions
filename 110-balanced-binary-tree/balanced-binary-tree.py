from functools import lru_cache
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return(True)
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh-rh)>1:
            return(False)
        return(self.isBalanced(root.left) and self.isBalanced(root.right))
    
    @lru_cache(maxsize=10000)
    def height(self,root):
        if not root:
            return(0)
        return(max(1+self.height(root.left), 1+self.height(root.right)))