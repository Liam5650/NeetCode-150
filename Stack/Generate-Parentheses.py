class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        # Create a recursive backtracking function to create the valid strings
        def backtrack(numLeft, numRight, string):

            # Reference the max amount of each kind of parentheses
            nonlocal n

            # If we reach this point, a valid string has been created. Add to results and end path
            if numLeft == numRight == n:
                nonlocal result
                result.append(string)
                return
            
            # Do not continue the path if the num of right brackets ever exceeds the left num
            if numLeft < numRight: 
                return
            
            # If the counts are equal, only move forward with the valid string, which adds a left bracket
            if numLeft == numRight:
                backtrack(numLeft + 1, numRight, string + "(")
            
            # If we are in a state where adding either bracket is valid, advance both paths
            elif numLeft > numRight and numLeft <= n:
                backtrack(numLeft, numRight + 1, string + ")")
                backtrack(numLeft + 1, numRight, string + "(")

        # Call recursive function and return result
        result = []
        backtrack(0, 0, "")
        return result