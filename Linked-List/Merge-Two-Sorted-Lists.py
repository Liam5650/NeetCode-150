from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Initialize a new linked list dummy node to start attaching to
        mergedHead = ListNode()

        # Set the tail to start at the same ListNode object
        mergedTail = mergedHead

        # Iterate until we are through at least one linked list
        while list1 != None and list2 != None:

            # Connect the node based on the value
            if list1.val < list2.val:
                mergedTail.next = list1
                list1 = list1.next

            else:
                mergedTail.next = list2
                list2 = list2.next
            
            # Advance the tail to start at the added node
            mergedTail = mergedTail.next
        
        # If one of the lists still has values, attach at the tail
        if list1: mergedTail.next = list1
        elif list2: mergedTail.next = list2

        # Return the merged lists next node as the first was a dummy
        return mergedHead.next