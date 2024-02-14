# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def get_path(self, r, node, l):
        if r.val == node:
            return(l+[r])
        if r.val > node:
            return(self.get_path(r.left, node, l+[r]))
        else:
            return(self.get_path(r.right, node, l+[r]))
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p1 = self.get_path(root,p.val,[])
        p2 = self.get_path(root,q.val,[])
        for i in range(min(len(p1),len(p2))):
            if p1[i]!=p2[i]:
                return(p1[i-1])
        return(p1[i])

        