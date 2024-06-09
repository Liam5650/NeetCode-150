class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashtable = set()
        for val in nums:
            if (val not in hashtable):
                hashtable.add(val)
            else:
                return True
        return False