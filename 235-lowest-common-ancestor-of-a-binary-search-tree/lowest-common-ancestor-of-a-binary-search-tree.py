# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def ancestor(root,l,n):
    if root.val==n:
        l.append(root)
        return(l)
    if root.val>n:
        return(ancestor(root.left,l+[root],n))
    else:
        return(ancestor(root.right,l+[root],n))

def rec(root,a,b):
    if not root:
        return
    
    if root.val > a and root.val>b:
        return(rec(root.left,a,b))
    elif root.val < a and root.val<b:
        return(rec(root.right,a,b))
    else:
        return(root)
    
    
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return(rec(root, p.val, q.val))
        l1 = ancestor(root,[],p.val)
        s=set(i.val for i in l1)
        l2 = ancestor(root,[],q.val)
        l2=l2[::-1]
        for i in l2:
            if i.val in s:
                return(i)