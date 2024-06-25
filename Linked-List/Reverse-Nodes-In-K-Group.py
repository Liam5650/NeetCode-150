from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Get the length of the list to calculate how many iterations we need
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next

        # Begin the standard procedure of reversing a linked list. We keep a list
        # of the endpoints (which is the head of the subsection to be reversed) for
        # easy joining after each iteration
        iters = length // k
        currIter = 0
        endpoints = []
        result = None

        while currIter < iters:
            
            # Append the endpoint
            endpoints.append(head)

            # Reverse the current segment
            count = 0
            prev = None
            while head and count < k:
                nextNode = head.next
                head.next = prev
                prev = head
                head = nextNode
                count += 1

            # If this is the first segment, the node that we end on is the start of the final result
            if currIter == 0: result = prev

            # If we have processed two segments, we must attach them together
            if len(endpoints) == 2:
                endpoints[0].next = prev
                endpoints = [endpoints[1]]
            
            # Continue iterating
            currIter += 1 

        # If there is anything remaining, attach it to the last endpoint
        if length % k != 0:
            endpoints[0].next = nextNode

        return result