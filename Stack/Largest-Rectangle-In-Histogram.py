class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        
        # Use a stack to store bar height in increasing order, along with the index. If 
        # a decreasing one is found, we can siimply pop bars from the stack and calculate the largest
        # area it could have made given it's position
        stack = []
        maxHeight = 0
        i = 0

        # Iterate through each bar
        while i < len(heights):

            # Initialize the stack if it is the first value
            if stack == []:
                stack.append((i, heights[i]))
                maxHeight = heights[i]
            
            # If it is a larger value, add it to the stack
            elif stack[-1][1] <= heights[i]:
                stack.append((i, heights[i]))
            
            # Iterate backwards through the stack, calculating the max area that could be created given
            # each value's start index, current index before popping, and height value
            else:
                startIndex = 0
                while stack != [] and heights[i] < stack[-1][1]:
                    startIndex = stack[-1][0]
                    maxHeight = max(maxHeight, stack[-1][1] * (i - startIndex))
                    stack.pop()
                
                # Add the new smallest value
                stack.append((startIndex, heights[i]))
            
            i += 1
        
        # If there are items left in the stack, they span the whole graph. Calculate their
        # area based on start index, final index, and height
        if stack != []:
            for val in stack:
                maxHeight = max(maxHeight, val[1] * (i - val[0]))

        return maxHeight