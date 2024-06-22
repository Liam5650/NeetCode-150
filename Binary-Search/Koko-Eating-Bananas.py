import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        # Use binary search for the best value between the max and 1, as the worst case
        # scenario needs each pile to be finished in one iteration which needs the max size
        # as a rate
        upper = max(piles)
        lower = 1
        result = []

        # Wait until the bounds cross, as that means we have reached the smallest option
        while lower <= upper:

            guess = int((upper + lower) / 2)
            hoursTaken = 0
            for pile in piles:
                hoursTaken += math.ceil(float(pile) / guess)
            
            # If it is an invalid guess, update the lower bound as we need to eat faster
            if hoursTaken > h:
                lower = guess + 1
            
            # Otherwise append the guess and update the upper bound to see if we can eat slower
            else:
                result.append(guess)
                upper = guess - 1

        # Return the minimum result that is valid
        return min(result)