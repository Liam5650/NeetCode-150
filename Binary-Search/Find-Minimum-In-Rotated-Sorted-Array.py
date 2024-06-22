class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        # Set up a boundary on the left and right side to define the search area
        l, r = 0, len(nums) - 1
        minimum = None

        while l <= r:

            # Search the middle of the area
            guess = int((l + r) / 2)

            # Update the minimum encountered val if necessary
            if minimum != None:
                minimum = min(minimum, nums[guess])
            else:
                minimum = nums[guess]

            # If the value on the right boundary is smaller, it means that the minimum must
            # be in that half of the values as the rotation must start after our curr guess
            if nums[guess] > nums[r]:
                l = guess + 1
            
            # Otherwise the value is in the left half of the values 
            else:
                r = guess - 1

        return minimum