# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def rec(root,a,b):
    if not root:
        return
    
    if root.val > a and root.val>b:
        return(rec(root.left,a,b))
    elif root.val < a and root.val<b:
        return(rec(root.right,a,b))
    else:
        return(root)
    
    
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return(rec(root, p.val, q.val))