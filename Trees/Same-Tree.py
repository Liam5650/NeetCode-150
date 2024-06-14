from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Base case
        if not p and not q:
            return True
        
        # Recursive loop if the nodes are equal
        if p and q and p.val == q.val:

            # We want to use "and" since both sides have to be true for true to be returned
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        else:
            return False