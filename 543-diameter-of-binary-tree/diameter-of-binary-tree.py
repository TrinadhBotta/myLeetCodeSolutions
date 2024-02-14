# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMaxHeight(self, root):
        if not root:
            return(0)
        return(1+max(self.getMaxHeight(root.left),self.getMaxHeight(root.right)))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return(0)
        return(max(self.getMaxHeight(root.left)+self.getMaxHeight(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))
