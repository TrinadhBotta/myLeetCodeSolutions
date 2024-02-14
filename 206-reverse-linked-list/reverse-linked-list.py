# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return(head)
        
        cur = head
        nex = None
        prev = None
        while cur:
            nex = cur.next
            temp = cur
            cur.next = prev
            prev = temp
            cur = nex
        return(prev)