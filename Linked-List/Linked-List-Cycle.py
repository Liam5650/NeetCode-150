from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Create a hashtable of the visited nodes
        visited = set()

        # Iterate through the list
        while head:

            # If the next node has been visited before, there is a cycle
            if head.next in visited:
                return True
            
            visited.add(head)
            head = head.next
        
        # If we make it to the end of the list and the pointer is null, there is no cycle
        return False