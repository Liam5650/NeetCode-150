from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
       # Set up a temp node for the None pointer at the end of the linked list
        prevNode = None

        # Iterate through the nodes until we reach None, which is the end
        while head != None:

            # Store a reference for the next node in the chain
            nextNode = head.next

            # Set the current nodes next node to be the previous node
            head.next = prevNode

            # We have reversed the head node, so now set it to be the previous
            prevNode = head

            # Continue with the next node as the head
            head = nextNode

        return prevNode    