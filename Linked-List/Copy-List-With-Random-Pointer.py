from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # If there is no head, return None
        if not head:
            return None

        # Create a hashtable that maps the existing node as a key to a new node value. This
        # creates the values of the new list so we can connect them later
        hashTable = {}
        old = head

        while head:
            newNode = Node(head.val)
            hashTable.update({head:newNode})
            head = head.next

        head = old

        # Go through the linked list again and connect all of the nodes
        while head:
            if head.next:
                hashTable[head].next = hashTable[head.next]
            else:
                hashTable[head].next = None
            if head.random:
                hashTable[head].random = hashTable[head.random]
            else:
                hashTable[head].random = None
            head = head.next
        
        return hashTable[old]