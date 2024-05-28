# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = head

        while r:
            t = r
            while t.next:
                if t.next.val != r.val:
                    r.next = t.next
                    break
                t = t.next
            
            if not t or not t.next:
                r.next = None
                break
            r = r.next
        
        return(head)