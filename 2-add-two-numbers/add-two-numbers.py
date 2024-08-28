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
        carry = 0
        head = ListNode(0)  # Dummy node to start the linked list
        temp = head

        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            # Calculate the sum and carry
            total = value1 + value2 + carry
            carry = total // 10
            value = total % 10

            # Create a new node with the computed value
            temp.next = ListNode(value)
            temp = temp.next

            # Move to the next nodes in l1 and l2
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next

        return head.next  # Return the real head (next of the dummy node)
