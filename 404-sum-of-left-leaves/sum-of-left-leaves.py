# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        
        def rec(r):
            if not r:
                return
            
            if r.left and not r.left.left and not r.left.right:
                self.ans+=r.left.val
            
            rec(r.left)
            rec(r.right)
            return
        
        rec(root)
        return(self.ans)