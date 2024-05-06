# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from functools import lru_cache 

class Solution(object):
    @lru_cache(maxsize=None)
    def maxPath(self, root):
        if not root:
            return(0)
        return(1+max(self.maxPath(root.left), self.maxPath(root.right)))

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
        l = self.maxPath(root.left)
        r = self.maxPath(root.right)
        return(max(l+r, self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right)))