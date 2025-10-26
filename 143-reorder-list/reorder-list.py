# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        
            curr = head
            prev = None
            
            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            
            return(prev)
        
        if not head or not head.next:
            return(head)
        
        slow = head
        fast = head

        while slow and slow.next and fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        
        to_reverse = slow.next
        slow.next = None
        
        reversed_ = reverseList(to_reverse)
        
        curr = head
        head = head.next
        while head and reversed_:
            curr.next = reversed_
            reversed_ = reversed_.next
            curr = curr.next
            curr.next = head
            head = head.next
            curr = curr.next
        
        curr.next = reversed_