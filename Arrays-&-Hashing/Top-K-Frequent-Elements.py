class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # First, we count the number of occurences of each value and store in a hashtable
        occurences = {}
        for val in nums:
            if not val in occurences:
                occurences.update({val:1})
            else:
                occurences[val] += 1
        
        # Next, we create a list where each index (0 index is 1 count) represents the number
        # of occurences of a val and stores that val. This is O(n) space complexity since we know
        # the max length of the list only needs to be the size of nums as that is the largest frequency
        # of occurences we would need to store
        bucketList = [[] for i in range(len(nums))]
        for val in occurences:
            bucketList[occurences[val] - 1].append(val) # -1 since we want the 1 count to start at index 0

        # Now we simply work backwards through the list, appending to the output until it reaches the
        # specified size
        output = []
        i = len(nums) - 1
        while len(output) < k:
            if bucketList[i] != []:
                for val in bucketList[i]:
                    output.append(val)
            i -= 1

        return output