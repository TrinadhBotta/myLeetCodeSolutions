# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0
        self.k = k
        def rec(root):
            if not root:
                return
            rec(root.left)
            if self.k==1:
                self.ans = root.val
            self.k-=1
            rec(root.right)
        rec(root)
        return(self.ans)