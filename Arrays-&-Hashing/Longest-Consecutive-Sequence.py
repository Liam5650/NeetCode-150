class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        # Create a hashtable for all of the nums, as well as ones we have processed
        numSet = set(nums)     
        totalVisited = set()
        longest = 0

        for num in numSet:

            # Only process a value if it hasn't been previously
            if not num in totalVisited:
                totalVisited.add(num)

                # We are going to search in both the positive and negative direction of the
                # current value for a sequence, so initialze a hashTable for the current search
                currVisited = set()
                currVisited.add(num)
                leftOffset, rightOffset = -1, 1

                # Search above the value
                while num + rightOffset in numSet:
                    totalVisited.add(num + rightOffset)
                    currVisited.add(num + rightOffset)
                    rightOffset += 1

                # Search below the value
                while num - leftOffset in numSet:
                    totalVisited.add(num - leftOffset)
                    currVisited.add(num - leftOffset)
                    leftOffset -= 1      

                # See if it is the longest current consecutive segment of values
                longest = max(longest, len(currVisited))

        return longest