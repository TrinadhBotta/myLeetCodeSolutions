# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return(None)
        start = head
        t = head
        while n>0:
            t = t.next
            n-=1
        end = t
        if not end:
            return(start.next)
            
        while end and end.next:
            end = end.next
            start = start.next
        
        start.next = start.next.next
        return(head)