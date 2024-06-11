class Solution:
    def search(self, nums: list[int], target: int) -> int:

        # Use a pointer to mark the top and bottom of the search area
        top = len(nums) - 1
        bottom = 0

        # Iterate until the pointers cross
        while bottom <= top:

            # Calculate the middle point
            middle = ((top - bottom) // 2) + bottom

            # Update the pointers based on if the target is higher or lower, or return found index
            if nums[middle] < target: bottom = middle + 1
            elif nums[middle] > target: top = middle -1
            else: return middle
        
        # If we have visited every value without returning, it isn't in the list
        return -1