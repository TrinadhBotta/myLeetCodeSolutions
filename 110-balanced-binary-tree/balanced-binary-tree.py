# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findHeight(self,root):
        if not root:
            return(0)
        return(1+max(self.findHeight(root.left),self.findHeight(root.right)))
    

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return(True)
        l = self.findHeight(root.left)
        r = self.findHeight(root.right)
        if abs(l-r)>1:
            return(False)
        return(self.isBalanced(root.left) and self.isBalanced(root.right))