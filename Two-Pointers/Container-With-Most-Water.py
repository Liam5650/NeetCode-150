class Solution:
    def maxArea(self, heights: list[int]) -> int:

        # Initialize two pointers and a variable to store the max found area
        left, right = 0, len(heights) - 1
        maxArea = 0

        # Iterate the pointers until they intersect, getting the area containable
        while left != right:
            maxArea = max(maxArea, (right - left) * min(heights[left], heights[right]))

            # Now we can simply move the smaller of the two to continue to the search, as we
            # have already explored the max area it can create when spanning the whole distance
            # between the pointers
            if heights[left] >= heights[right]: right -= 1
            else: left += 1

        return maxArea