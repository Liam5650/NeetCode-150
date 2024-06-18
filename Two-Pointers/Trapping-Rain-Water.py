class Solution:
    def trap(self, height: list[int]) -> int:

        # Use two pointers while keeping track of the max height of the left
        # and right barriers seen so far. We can do this since we always evaluate
        # the total volume a spot can hold based on the smaller of its left and right 
        # barrier
        total = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        # Wait for the pointers to cross
        while l <= r:

            # If the left max is the smallest, evaluate the total volume storable above the l pointer block
            if leftMax <= rightMax:
                area = leftMax - height[l]

                # If the area is not positive, the block must be as high or higher than the leftMax. Update
                if area > 0: total += area
                else: leftMax = height[l]
                l += 1

            # If the right max is the smallest, evaluate the total volume storable above the r pointer block
            else:
                area = rightMax - height[r]

                # If the area is not positive, the block must be as high or higher than the rightMax. Update
                if area > 0: total += area
                else: rightMax = height[r]
                r -= 1
            
        return total    