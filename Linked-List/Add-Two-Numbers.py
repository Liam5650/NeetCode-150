from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a carry bit and an array to store the computed digits
        carry = 0
        head1 = l1
        head2 = l2
        digits = []

        # Iterate through the lists, calculating the digit total and the carry value
        while head1 and head2:
            total = head1.val + head2.val + carry
            carry = int(total / 10)
            value = total % 10
            digits.append(value)
            head1 = head1.next
            head2 = head2.next
        
        # Iterate through the rest of the lists if they are not of equal length
        while head1:
            total = head1.val + carry
            carry = int(total / 10)
            value = total % 10
            digits.append(value)
            head1 = head1.next

        while head2:
            total = head2.val + carry
            carry = int(total / 10)
            value = total % 10
            digits.append(value)
            head2 = head2.next 
        
        # If we have carry at the end, append it
        if carry == 1: digits.append(carry)

        # Create the new list from the calculated digits
        output = head = ListNode(digits[0])

        for i in range(1, len(digits)):
            node = ListNode(digits[i])
            head.next = node
            head = node
        
        # Set the end of the list to none
        head.next = None
        return output