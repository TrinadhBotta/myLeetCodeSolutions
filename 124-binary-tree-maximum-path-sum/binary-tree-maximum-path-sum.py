# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.ans = -float('inf')

        def rec(root):
            if not root:
                return(-1000000)
            
            l=rec(root.left)
            r=rec(root.right)
            self.ans=max(l,r,l+r+root.val,l+root.val,r+root.val, root.val,self.ans)

            return(max(l+root.val,r+root.val, root.val))
        
        rec(root)
        return(self.ans)