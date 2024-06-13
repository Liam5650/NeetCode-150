from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Base case
        if root == None:
            return 0

        # Add 1 for our current level, and get the max of the depth of the nodes right and left children
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))