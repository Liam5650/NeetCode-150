class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        # Since we can access matrix properties with O(1) time, we can simply
        # grab the m*n values and map the 2D matrix to a 1D array
        rows = len(matrix)
        cols = len(matrix[0])

        # Set pointers as in a normal binary search
        bottom = 0
        top = (rows * cols) - 1

        while bottom <= top:

            # Select the middle point as normal
            middle = ((top-bottom) // 2) + bottom

            # Map the 1D middle value to a 2D matrix coordinate
            row = middle // cols
            col = middle - (row*cols)

            # Truncate half of the values based on the target value, or return if found
            if matrix[row][col] > target: top = middle - 1
            elif matrix[row][col] < target: bottom = middle + 1
            else: return True

        # If we iterate through the whole matrix, the target does not exist in the matrix
        return False