class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Initialize dictionaries to store char:count pairs for each string
        dict1 = {}
        dict2 = {}

        # Iterate through strings, creating keys for new chars and incrementing counts of chars already added
        for char in s:
            if char in dict1:
                dict1[char]+=1
            else:
                dict1.update({char:1})

        for char in t:
            if char in dict2:
                dict2[char]+=1
            else:
                dict2.update({char:1})

        # Return whether or not the two dictionaries have identical key:value pairs
        return dict1 == dict2