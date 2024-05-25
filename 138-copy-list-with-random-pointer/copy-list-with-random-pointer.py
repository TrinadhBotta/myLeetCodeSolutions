"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return(None)
        
        d = {}
        ans = Node(head.val)
        d[head] = ans
        t = ans
        
        while head:
            if head.next:
                if head.next in d:
                    t.next = d[head.next]
                else:
                    t.next = Node(head.next.val)
                    d[head.next] = t.next

            if head.random:
                if head.random in d:
                    t.random = d[head.random]
                else:
                    t.random = Node(head.random.val)
                    d[head.random] = t.random
            
            head = head.next
            t = t.next
        
        return(ans)
