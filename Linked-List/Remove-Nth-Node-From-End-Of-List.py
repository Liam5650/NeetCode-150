from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Iterate through the list to get the length
        linkedList = head
        size = 0
        while head:
            head = head.next
            size += 1

        # Navigate to the position of the node to be removed
        toRemove = size - n
        node = 0
        head = linkedList
        prev = None
        while head and node < toRemove:
            prev = head
            head = head.next
            node += 1

        # If it was not the item at the start of the list, join the previous and next nodes
        if prev:
            prev.next = head.next
            return linkedList
        
        # If it was the item at the start, return the node starting after the head
        else:
            return head.next