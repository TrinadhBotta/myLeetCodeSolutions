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
        if l not in self.data:
            self.data[l] = [0,0]
        self.data[l][0]+=root.val
        self.data[l][1]+=1
        self.level(root.left,l+1)
        self.level(root.right,l+1)
        return

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.data = {}
        self.level(root,0)
        ans = [0]*len(self.data)
        for i in self.data:
            ans[i]=self.data[i][0]/self.data[i][1]
        return(ans)