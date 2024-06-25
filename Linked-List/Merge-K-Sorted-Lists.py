from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        
        # This solution is O(n*k). Will return to implement O(n*log(k))

        # Create a dummy node for returning
        result = head = ListNode()

        # Iterate until all lists have been processed
        while lists != [None] * len(lists):

            # Find the minimum node
            minimum = float("inf")
            minimumHead = None
            i = 0
            index = None
            for linkedList in lists:
                if linkedList != None and linkedList.val < minimum:
                    minimum = linkedList.val
                    minimumHead = linkedList
                    index = i
                i += 1
            
            # Attach a node to the result with the min value and continue
            head.next = ListNode(minimum)
            head = head.next
            lists[index] = minimumHead.next

        # Return the node starting after the dummy node
        return result.next