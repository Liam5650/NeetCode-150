from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Assume the tree is balanced at first, and create a helper function to recursively prove that it is or is not
        balanced = True
        def dfs(root):

            # Make sure we are referencing the variable outside of the inner function
            nonlocal balanced

            # Base case of height 0
            if not root:
                return 0
            
            # Perform DFS on the left and right children
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            # If the height of the children differs more than 1, set the balanced flag to false
            if abs(leftHeight - rightHeight) > 1 : balanced = False

            # Return 1 (the current height of a node) + the maximum of its sub-trees
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return balanced