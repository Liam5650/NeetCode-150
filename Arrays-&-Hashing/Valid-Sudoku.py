from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        # Create a dict with the corresponding row/col/(row,col) as a key, and the value pair being
        # the set of values in that structure seen
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # Iterate through the board
        for row in range(9):
            for col in range(9):

                # Get our current value to process
                val = board[row][col]

                if val != ".":

                    # Check to see if this value exists already in any of the structures, otherwise add to each
                    if val in rows[row] or val in cols[col] or val in squares[(row//3, col//3)]: return False
                    rows[row].add(val)
                    cols[col].add(val)
                    squares[(row//3, col//3)].add(val)

        return True