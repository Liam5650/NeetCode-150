class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Create a charset that maps character counts to their index, where 'a' is 0 and 
        # 'z' is 25
        charset = [0] * 26
        for char in s1:
            charset[ord(char) - ord("a")] += 1

        # Create a subset of the second string that uses the characters between the left and
        # right pointers, to check if the two sets match
        l, r = 0, 0
        subset = [0] * 26

        # Stop when we have gone through the whole string
        while r < len(s2):

            # Add the latest character to our set
            subset[ord(s2[r]) - ord("a")] += 1

            # If the two sets match we can break and simply return true
            if subset == charset: return True

            # Check to see if it is still possible to build the other string from our
            # current substring, ie if it is a substring of the other charset
            matches = True
            for i in range(26):
                if (charset[i] == 0 and subset[i] != 0) or charset[i] < subset[i]:
                    matches = False

            # If they can't match, increment the left pointer while removing characters 
            # until they match again
            if not matches:
                subset[ord(s2[l]) - ord("a")] -= 1
                subset[ord(s2[r]) - ord("a")] -= 1
                l += 1

            # Otherwise continue building the substring
            else:
                r += 1

        # We can safetly return false as a match was not found if this point is reached
        return False   