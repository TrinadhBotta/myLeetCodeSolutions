# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return(True)
        if (p and not q) or (q and not p) or (p.val!=q.val):
            return(False)   
        return(self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

    def getList(self, root, v):
        if not root:
            return
        
        if root.val==v:
            self.ans.append(root)
        self.getList(root.left,v)
        self.getList(root.right,v)
        return

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ans=[]
        self.getList(root, subRoot.val)

        for i in self.ans:
            if self.isSameTree(i, subRoot):
                return(True)
        return(False)