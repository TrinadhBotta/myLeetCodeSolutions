# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def rev(root):
            curr, prev= root, None
            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return(prev)
        
        # l1, l2 = rev(l1), rev(l2)
        value = (l1.val+l2.val)%10
        carry = (l1.val+l2.val)//10

        head = ListNode(value)
        temp = head
        l1,l2 = l1.next, l2.next

        while l1 and l2:
            value = (l1.val+l2.val+carry)%10
            carry = (l1.val+l2.val+carry)//10
            temp.next = ListNode(value)
            temp = temp.next
            l1,l2 = l1.next, l2.next
        
        while l1:
            value = (l1.val+carry)%10
            carry = (l1.val+carry)//10
            temp.next = ListNode(value)
            temp = temp.next
            l1 = l1.next
        
        while l2:
            value = (l2.val+carry)%10
            carry = (l2.val+carry)//10
            temp.next = ListNode(value)
            temp = temp.next
            l2 = l2.next

        if carry!=0:
            temp.next = ListNode(carry)
        
        return(head)

        