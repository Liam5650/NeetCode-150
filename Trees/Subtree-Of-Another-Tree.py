from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Initialize a reference that we will use DFS traversal of the tree to prove true
        same = False
        def dfs(node, subRoot):

            # Make sure we are referencing the non local variable
            nonlocal same

            # Base case
            if not node or same == True:
                return
            
            # Explore nodes using DFS 
            dfs(node.left, subRoot)
            dfs(node.right, subRoot)

            # Once we visit a node, check to see if it matches
            if self.sameTree(node, subRoot):
                same = True
            
        dfs(root, subRoot)
        return same

    # Helper function to compare two trees
    def sameTree(self, tree1, tree2) -> bool:

        # Base case
        if not tree1 and not tree2:
            return True
        
        # Recursive loop if the nodes are equal
        if tree1 and tree2 and tree1.val == tree2.val:

            # We want to use "and" since both sides have to be true for true to be returned
            return self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right)

        else:
            return False