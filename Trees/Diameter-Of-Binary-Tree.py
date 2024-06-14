from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Initialize the max found diameter and a helper recursive function
        maxDiameter = 0
        def dfs(root) -> int:
            
            # Make sure we are referencing the variable outside the inner function
            nonlocal maxDiameter

            # Base case of height 0
            if not root:
                return 0
            
            # Do a DFS on each child, calculating the diameter at that step and updating the max
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            diameter = leftHeight + rightHeight
            maxDiameter = max(diameter, maxDiameter)

            # Return 1 for the height of this level, + the max height of either the right or left child
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return maxDiameter