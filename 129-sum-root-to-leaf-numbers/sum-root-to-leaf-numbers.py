# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def cal(self, root,s="0"):
        if not root.left and not root.right:
            self.ans+=int(s+str(root.val))
            return
        if root.left:
            self.cal(root.left, s+str(root.val))
        if root.right:
            self.cal(root.right, s+str(root.val))
        return
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        self.cal(root)
        return(self.ans)