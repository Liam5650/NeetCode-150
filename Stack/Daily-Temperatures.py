class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        # Initialize a stack that stores tuples holding a temp and the day it occurred on, and an output
        stack = []
        output  = [0] * len(temperatures)

        # Iterate through every day
        i = 0
        while i < len(temperatures):
            temp = temperatures[i]

            # If the temp is lower than or equal to the top of the stack, add it to the stack
            if stack == [] or temp <= stack[-1][0]: 
                stack.append((temp, i))
            else:

                # Remove items from the stack, and update the difference in days
                while stack != [] and temp > stack[-1][0]:
                    output[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()

                # Append the new val, since it is now the new lowest
                stack.append((temp, i))
            i += 1
        
        return output 