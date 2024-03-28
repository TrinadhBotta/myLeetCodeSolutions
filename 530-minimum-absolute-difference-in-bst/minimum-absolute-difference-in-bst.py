# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def level(self, root, l):
        if not root:
            return
        self.level(root.left,l)
        l+=[root.val]
        self.level(root.right,l)
        return(l)


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l=self.level(root, [])
        ans=1000000
        for i in range(len(l)-1):
            ans=min(ans,l[i+1]-l[i])
        return(ans)
