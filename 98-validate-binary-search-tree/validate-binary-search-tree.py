from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,node,l):
        if not node:
            return(l)
        l = self.preorder(node.left,l)
        l.append(node.val)
        l = self.preorder(node.right,l)
        return(l)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = self.preorder(root,[])
        if not l:
            return(True)
        if l == sorted(l):
            d = Counter(l)
            if len(d)==len(l):
                return(True)
        return(False)