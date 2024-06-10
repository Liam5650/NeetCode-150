class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        # Since the array is sorted, we can use two pointers to increment/decrement 
        # from the left/right side depending on the sum until we find the target
        leftPointer = 0
        rightPointer = len(numbers) - 1

        # The values must be unique, so the pointers should never cross
        while leftPointer < rightPointer:

            # If the sum is too big, decrement the right pointer to exclude the value
            if (numbers[leftPointer] + numbers[rightPointer] < target):
                leftPointer += 1
            
            # If the sum is too small, increment thr left pointer to exclude the value
            elif (numbers[leftPointer] + numbers[rightPointer] > target):
                rightPointer -= 1

            else:
                return [leftPointer + 1, rightPointer + 1] 