# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        
        def check(r, mx):
            if not r:
                return
            
            if r.val>=mx:
                self.ans+=1
            
            check(r.left, max(mx,r.val))
            check(r.right, max(mx,r.val))
            return
        
        check(root, -10000000)

        return(self.ans)