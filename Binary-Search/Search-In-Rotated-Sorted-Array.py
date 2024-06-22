class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        # Set up pointers that mark the bounds of the search area
        l, r = 0, len(nums) - 1

        while l <= r:

            # Make our guess in the middle
            guessIndex = int((l + r) / 2)
            guess = nums[guessIndex]

            if guess == target:
                return guessIndex

            # This means we are in the left portion of the pivot. Everything to our left must 
            # be smaller than our guess
            if nums[l] <= guess:

                # If our guess is too high, but the target is still bigger than the left bound,
                # the target must also be in the left portion
                if guess > target and target >= nums[l]:
                    r = guessIndex - 1
                
                # Otherwise it is in the right portion
                else:
                    l = guessIndex + 1

            # This means we are in the right portion of the pivot. Everything to our right
            # must be larger than our guess
            else:

                # If the guess is too low, but the target is smaller than the right bound, 
                # the target must be in the right portion
                if guess < target and target <= nums[r]:
                    l = guessIndex + 1
                
                # Otherwise it is in th left portion
                else:
                    r = guessIndex - 1

        return -1