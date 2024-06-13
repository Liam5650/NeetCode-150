from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Get a reference to the head of the linked list
        linkedList = head

        # Iterate through the list and get all the nodes
        nodeList = []

        while head != None:
            nodeList.append(head)
            head = head.next

        # Go through the node list and connect the pointers in the order as described

        offset = 0 # This describes the offset index from the front or end of the list
        flipBit = 1 # This is used to check whether we are grabbing the node from the front or back of the list
        processedNodes = 0
        head = linkedList

        while processedNodes < len(nodeList):

            if flipBit == 1:
                head.next = nodeList[-offset - 1]
                offset += 1
            else:
                head.next = nodeList[offset]

            # Restart the loop with the new node as the head, and flip the bit
            head = head.next
            processedNodes += 1
            flipBit = flipBit * -1

        # Finally, update the pointer at the end of the linked list to none
        head.next = None