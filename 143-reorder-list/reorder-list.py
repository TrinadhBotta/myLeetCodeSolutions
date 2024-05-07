# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_reverse(self, root):
        curr = root
        prev = None
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        return(prev)

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find length
        l = 0
        curr = head
        while curr:
            l+=1
            curr=curr.next
        mid = l//2 if l%2==0 else (l//2)+1

        curr = head
        while mid>0:
            curr=curr.next
            mid-=1
        
        rev_head = self.get_reverse(curr)
        normal_head = head


        
        while rev_head:
            t = normal_head.next
            normal_head.next = ListNode(rev_head.val)
            rev_head = rev_head.next
            normal_head = normal_head.next
            normal_head.next = t
            normal_head = normal_head.next
        
        while head and head.next and head.next.next:
            head = head.next
        head.next = None