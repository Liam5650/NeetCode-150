from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Create a hashtable to map the char:occurences pairs of the substring
        hashTable = {}
        for char in t:
            if not char in hashTable:
                hashTable.update({char : 1})
            else:
                hashTable[char] += 1
            
        # Initialize pointers to represent the bounds of our current search window
        l, r = 0, 0

        # Initialize a second hashtable that we will use to build substrings to match to target
        hashTable2 = {}

        # Initialize a deque so we can remove values from the substring if a more recent
        # char is found vs the one at the front of the deque
        visitedOrder = deque()

        # Iterate through the string
        smallest = ""
        while r < len(s):
            char = s[r]

            # If we have no current substring and the char doesn't belong in it, skip
            if len(hashTable2) == 0 and char not in hashTable:
                l += 1
                r += 1
            
            # If we have a current substring, only increment the right pointer to include new val in window
            elif len(hashTable2) != 0 and char not in hashTable:
                r += 1
            
            # Add the char to further build the substring to match, and update our deque
            elif char in hashTable:
                if char not in hashTable2:
                    hashTable2.update({char : 1})
                else:
                    hashTable2[char] += 1
                visitedOrder.append(char)
                r += 1
            
            # If the current value we added exceeds the count in the string we are trying to match, and
            # that val is at the start of the deque, we can safely discard it to use the new val as it will be smaller
            while len(visitedOrder) != 0 and hashTable[visitedOrder[0]] < hashTable2[visitedOrder[0]]:
                while l < len(s) and s[l] != visitedOrder[0]:
                    l += 1
                hashTable2[visitedOrder[0]] -= 1
                visitedOrder.popleft()
                l += 1
                while s[l] != visitedOrder[0]:
                    l += 1

            # Test to see if our substring is valid and update smallest
            if self.isValid(hashTable, hashTable2):
                if smallest == "" or len(s[l:r]) < len(smallest):
                    smallest = s[l:r]

                # Pop our oldest value and slide the left side of the window to the next
                # valid char
                if hashTable2[s[l]] == 1:
                    hashTable2.pop(s[l])
                else:
                    hashTable2[s[l]] -= 1
                l += 1
                visitedOrder.popleft()
                while l < len(s) and len(visitedOrder) != 0 and s[l] != visitedOrder[0]:
                    l += 1

        return smallest

    # For a string to be valid, the substring must have the same keys and an equal or higher
    # occurence vs the target string (as this means we can handle repeated characters in the substring)
    def isValid(self, dict1, dict2):

        for key in dict1:
            if key not in dict2:
                return False
            elif dict1[key] > dict2[key]:
                return False
        return True