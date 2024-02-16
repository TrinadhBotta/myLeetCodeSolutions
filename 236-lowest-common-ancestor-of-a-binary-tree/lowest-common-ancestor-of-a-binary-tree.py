# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    @lru_cache(maxsize = None)
    def check(self, root, val):
        if not root:
            return(False)
        if root.val == val:
            return(True)
        return(self.check(root.left,val) or self.check(root.right,val))

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return(root)
        if ((self.check(root.left, p.val)) and (self.check(root.right, q.val)) or (self.check(root.left, q.val)) and (self.check(root.right, p.val))):
            return(root)
        if root.val == p.val or root.val == q.val:
            return(root)
        r1 = self.lowestCommonAncestor(root.left, p ,q)
        r2 = self.lowestCommonAncestor(root.right, p ,q)
        if not r1:
            return(r2)
        return(r1)
        
        