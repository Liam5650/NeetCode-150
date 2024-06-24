class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Create pointers to iterate, and a int array of char counts where the index 0 
        # maps to "A" and index 25 maps to "Z"
        r, l = 0, 0
        longest = 0
        vals = [0] * 26

        # Iterate until the right pointer reaches the end of the string
        while r < len(s):

            # For the substring to be valid, the window size minus the count of the most
            # common character must be less than or equal to K
            windowSize = r - l + 1

            # Add the latest character to the window
            vals[ord(s[r]) - ord("A")] += 1
            maxVal = max(vals)

            # Check if the window is valid
            if windowSize - maxVal <= k:
                longest = max(longest, windowSize)
                r += 1 

            # If it is not, remove the char and also the char on the leftmost part of the window
            # as we need to slide the window to the right by one
            else:
                print("Removing " + s[l])
                vals[ord(s[r]) - ord("A")] -= 1
                vals[ord(s[l]) - ord("A")] -= 1
                l += 1

        return longest