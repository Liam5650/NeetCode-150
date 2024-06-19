class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        # Use Floyd's algorithm
        slow, fast = 0, 0

        # Find the intersection point of the two pointers
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find the intersection from the start
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break

        return slow