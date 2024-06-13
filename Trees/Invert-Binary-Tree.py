from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Base case
        if root == None:
            return None

        # Swap the child nodes
        temp = root.right
        root.right = root.left
        root.left = temp

        # Recursively call on the child nodes and return
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root