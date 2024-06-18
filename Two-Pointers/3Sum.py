class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # For this problem, we can think of it as built upon two-sum. We can sort the list,
        # then iterate through and use each value as the target of a two-sum problem using
        # the rest of the list
        nums.sort()

        # Processed is a set of each value used as a target, whereas triplet set is used to store
        # triplets and catch duplicates 
        processed = set()
        tripletSet = set()

        for i in range(len(nums)):
            val = nums[i]

            # Do a basic 2-sum now using the value as the target
            if val not in processed:
                target = -val
                subList = nums[i+1:]
                subSet = set(subList)
                visited = set()

                # Iterate through the sublist and try to find a complement to each value
                for j in range(len(subList)):
                    subVal = subList[j]
                    complement = target - subVal
                    
                    # If there is a complement, sort the result to make sure only unique 
                    # solutions are added to the set
                    if complement in visited:
                        triplet = [val, subVal, complement]
                        triplet.sort()
                        triplet = tuple(triplet)
                        tripletSet.add(triplet)

                    # Continue through the sublist
                    visited.add(subVal)

            # Continue through the list
            processed.add(val)

        # Convert the triplet set into the list format as specified by the problem
        result = []
        for triplet in tripletSet:
            result.append(list(triplet))

        return result