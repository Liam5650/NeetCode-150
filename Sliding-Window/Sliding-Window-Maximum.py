# We will use a deque to be able to access and modify values on both ends in O(1) time
from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        
        # Initialize the result and deque
        result = []
        queue = deque()

        # Create the window bounds for comparison
        l, r = 0, 0

        # Iterate until we have reached the end of the list
        while r < len(nums):

            # Calculate our current window size, and remove items from the deque if their
            # index falls outside the current window range as the window has grown too large
            windowSize = r - l + 1
            if windowSize > k: 
                l += 1
                while len(queue) != 0 and l > queue[0]:
                    queue.popleft()
                windowSize -= 1
            
            # Process the new value
            newVal = nums[r]

            if len(queue) == 0:
                queue.append(r)
            else:
                # Remove all values that are smaller than the current, then add the val
                while len(queue) != 0 and newVal >= nums[queue[-1]]:
                    queue.pop()
                queue.append(r)
            
            # If we are at the correct window size, append the value at the start of the deque
            # to the result as it is the largest in the descending-value queue
            if (windowSize == k):
                result.append(nums[queue[0]])

            r += 1

        return result