class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        # Create a set to add new values of the list to
        hashtable = set()

        # Add new to values to the set, or return true if the value already exists in the set as it is a duplicate
        for val in nums:
            if (val not in hashtable):
                hashtable.add(val)
            else:
                return True

        # If we have made it through the entire list, no duplicates must have been found    
        return False