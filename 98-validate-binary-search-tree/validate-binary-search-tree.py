# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def rec(root, left, right):
            if not root:
                return(True)
            
            if not( root.val<right and root.val>left):
                return(False)
            
            return(rec(root.left, left, root.val) and
                rec(root.right, root.val, right))
        
        return(rec(root, -float('inf'), float('inf')))

