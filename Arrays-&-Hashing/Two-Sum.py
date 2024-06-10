class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        # Create a hashtable to store checked values and their index
        hashtable = {}
        i = 0

        # Check to see if the complement of the val exists in the hashtable, otherwise add val:index pair
        for val in nums:
            complement = target - val
            if complement in hashtable:
                return [hashtable.get(complement), i]
            else:
                hashtable.update({val:i})
                i+=1