class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # L and R represent the left and right indices of the substring
        l,r = 0, 0

        # Track the length of the longest currently found, and initialize a set of seen chars
        # in the current substring
        longest = 0
        seen = set()

        # End when we have gone through the whole string
        while r < len(s):

            # If we haven't seen the character, add it to the set
            if s[r] not in seen:
                seen.add(s[r])

            # If we have seen the character, increment the left pointer until it reaches the same
            # character as the right pointer, removing values in between from the set. We don't bother
            # removing the duplicate char as it is part of the next substring
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                
                # Increment the left pointer to start the new substring after the duplicate value
                l+=1

            # Check to see if the current substring is the longest, and then increment the right pointer
            if len(seen) > longest: longest = len(seen)
            r += 1

        return longest              