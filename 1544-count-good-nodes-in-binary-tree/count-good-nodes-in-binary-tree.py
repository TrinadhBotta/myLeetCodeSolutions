# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, root, cmax):
        if not root:
            return
        if root.val>=cmax:
            self.ans+=1
        self.rec(root.left, max(cmax,root.val))
        self.rec(root.right, max(cmax,root.val))


    def goodNodes(self, root: TreeNode) -> int:
        self.ans=0
        self.rec(root, root.val)
        return(self.ans)