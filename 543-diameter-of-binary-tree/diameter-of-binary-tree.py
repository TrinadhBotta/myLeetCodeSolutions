# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from functools import lru_cache 

class Solution(object):
    @lru_cache(maxsize=1000)
    def maxDepth(self, root):
        if not root:
            return(0)
        return(1+max(self.maxDepth(root.left), self.maxDepth(root.right)))

    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return(0)
        lmax = self.maxDepth(root.left)
        rmax = self.maxDepth(root.right)

        return(max(lmax+rmax, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))